from cmath import inf
import numpy as np
import pandas as pd

class Operator:
    def __init__(self):
        
        self.success = [0]
        self.total_success = 0
        self.trial = [0]
        self.cluster_update_count = 1
        self.reset()

    def next_iteration(self):
        self.rewards.append(0)
        self.success.append(0)
        self.reward_history.append(0)
        self.trial.append(0)
        
    def reset(self):
        self.rewards = [0]
        self.reward_history = [0]
        self.trial.append(0)
        


class Period:
    def __init__(self, operator_size):
        self.op = [ Operator() for i in range(operator_size)]
    
    def reset(self):
        for o in self.op:
            o.reset()

class CLRL:
    def __init__(self, parameters):
        #General informations
        self.parameters = parameters
        self.parameters["max_period"] = 10
        self.informations = dict({'iteration_number':0, 'period_number':0})
        self.cluster_history = []
        self.credit_history = []

    def load_information(self):
        self.periods = [Period(self.parameters["operator_size"]) for _ in range(self.parameters["max_period"])]
        if self.parameters["load_file"] == None:
            clusters = np.full((self.parameters["max_period"],self.parameters["operator_size"], self.algorithm.feature_size),np.inf)
            credits = np.full((self.parameters["max_period"],self.parameters["operator_size"]),-inf)
            cluster_update_count = np.full((self.parameters["max_period"],self.parameters["operator_size"]),1)
        else:
            with open(f"results/clusters-{self.parameters['load_file']}", 'r',) as f:
                row = f.readlines()
                clusters=[]
                for r in row:
                    clusters.append( np.fromstring(r, dtype=np.float32, sep=',') )
                clusters = clusters[-self.parameters["max_period"]*self.parameters["operator_size"]:]
            with open(f"results/credits-{self.parameters['load_file']}", 'r',) as f:
                row = f.readlines()
                credits=[]
                for r in row:
                    credits.append( np.fromstring(r, dtype=np.float32, sep=',') )
                credits = credits[-1]
            with open(f"results/cluster_update_counts-{self.parameters['load_file']}", 'r',) as f:
                row = f.readlines()
                cluster_update_count=[]
                for r in row:
                    cluster_update_count.append( np.fromstring(r, dtype=np.float32, sep=',') )
                cluster_update_count = cluster_update_count[-1]
        clusters = np.reshape(clusters,(self.parameters["max_period"],self.parameters["operator_size"],self.algorithm.feature_size))
        credits = np.reshape(credits,(self.parameters["max_period"],self.parameters["operator_size"]))
        cluster_update_count = np.reshape(cluster_update_count,(self.parameters["max_period"],self.parameters["operator_size"]))

        for p,period in enumerate(self.periods):
            for ind,o in enumerate(period.op):
                o.clusters = np.array(clusters[p][ind])
                o.credits = [credits[p][ind]]
                o.cluster_update_count = cluster_update_count[p][ind]


    def reset(self):
        #Reset or load internal variables.
        self.load_information()
            

    def start(self):
        # Initial definitions..
        self.operator_informations = []
        if (self.parameters["learning_mode"] == 1):
            if(self.informations['run_number'] == 0):
                self.reset()
        else:
            self.reset()

    def finished(self):
        self.clusters = []
        self.credits = []
        self.cluster_update_counts = []
        for p in self.periods:
            for o in p.op:
                self.clusters.append(o.clusters)
                self.credits.append(o.credits[-1])
                self.cluster_update_counts.append(o.cluster_update_count)
            p.reset()
        
    
    def set_algorithm(self,algorithm, run_number):
        #Assign algorithm and run number and start...
        self.algorithm = algorithm
        self.informations["run_number"] = run_number
        self.informations['iteration_number'] = 0
        self.informations['period_number'] = 0
        self.start()

    #Calculate reward according to candidate and current solution    
    def get_reward(self, new_cost, old_cost):
        if(new_cost==0):
            return 0
        r = float(( new_cost - old_cost)) * (self.algorithm.global_best.cost/new_cost)
        return max(0,r)

    #Operator used and supply feedback
    def add_reward(self, op, candidate, current):
        #Increase the number of times the operator is used
        self.periods[self.informations["period_number"]].op[op].trial[-1] += 1
        reward = self.get_reward(candidate.cost, current.cost)
        self.periods[self.informations["period_number"]].op[op].reward_history[-1] += reward
        self.periods[self.informations["period_number"]].op[op].rewards.append(reward)
        self.set_credit(op,self.get_distance(op, current))
        if reward > 0:
            self.periods[self.informations["period_number"]].op[op].success[-1] += 1
            self.periods[self.informations["period_number"]].op[op].total_success += 1
            candidate.calculate_features(self.algorithm)
            self.set_cluster(op, current)

    def apply_rewards(self, op):
        if self.parameters["reward_type"] == "insta":
            reward = self.periods[self.informations["period_number"]].op[op].rewards[-1]
        elif self.parameters["reward_type"] == "average":
            start_pos = max(0, len(self.periods[self.informations["period_number"]].op[op].rewards) - self.parameters["W"])
            reward = np.average(self.periods[self.informations["period_number"]].op[op].rewards[start_pos:])
        elif self.parameters["reward_type"] == "extreme":
            start_pos = max(0, len(self.periods[self.informations["period_number"]].op[op].rewards) - self.parameters["W"])
            reward = np.max(self.periods[self.informations["period_number"]].op[op].rewards[start_pos:])
        return reward

    def set_credit(self, op, distance=0):
        r = self.apply_rewards(op)
        if(distance==inf):
            distance =0
        if self.periods[self.informations["period_number"]].op[op].credits[-1] == -inf:
            credit = self.parameters["alpha"] * (r+self.parameters["gama"]*distance)
        else: 
            credit = (1 - self.parameters["alpha"]) * self.periods[self.informations["period_number"]].op[op].credits[-1] + self.parameters["alpha"] * (r+self.parameters["gama"]*distance)
        self.periods[self.informations["period_number"]].op[op].credits.append(credit)

    def next_period(self):
        self.informations["period_number"] += 1

    def roulette_wheel(self, probs):
        sumProbs = sum(probs)
        probs = [item / sumProbs for item in probs]
        op = np.random.choice(len(probs), p=probs)
        return op

    def next_iteration(self):
        #Adaptive randomness
        # self.parameters['eps'] = self.parameters["eps"] * np.exp(-4*self.informations["iteration_number"]/self.algorithm.max_iteration)
        
        #Check period 
        if(int(np.floor(self.informations["iteration_number"]/(self.algorithm.max_iteration/self.parameters["max_period"]))) != self.informations["period_number"]):
            self.next_period()

        #Apply iteration changes to the operators     
        for i in range(self.parameters["operator_size"]):
            #Reporting
            self.operator_informations.append([i, self.informations["run_number"], self.algorithm.global_best.cost, self.informations["iteration_number"], self.periods[self.informations["period_number"]].op[i].credits[-1], 
            self.periods[self.informations["period_number"]].op[i].reward_history[-1], self.periods[self.informations["period_number"]].op[i].trial[-1], self.periods[self.informations["period_number"]].op[i].success[-1]])
            self.credit_history.append([i, self.informations["iteration_number"], self.informations["run_number"], self.periods[self.informations["period_number"]].op[i].credits[-1]])
            self.cluster_history.append(np.concatenate( (np.array([i, self.informations["iteration_number"], self.informations["run_number"]]), self.periods[self.informations["period_number"]].op[i].clusters),axis=0))
            self.periods[self.informations["period_number"]].op[i].next_iteration()
        self.informations["iteration_number"] += 1

    def get_distance(self, op, y):
        dist = 0
        if self.informations["iteration_number"]==0 or len(y.features)==0:
            return dist
        dist += (1/self.algorithm.feature_size)*np.linalg.norm(self.periods[self.informations["period_number"]].op[op].clusters - y.features)
        return  dist

    def set_cluster(self, op, solution):
        if len(solution.features) == 0:
                return

        if np.sum(self.periods[self.informations["period_number"]].op[op].clusters) == np.inf :
            self.periods[self.informations["period_number"]].op[op].clusters = np.array(solution.features)
            return
        for i in range(len(solution.features) ) :
            self.periods[self.informations["period_number"]].op[op].clusters[i] = self.periods[self.informations["period_number"]].op[op].clusters[i] + ((solution.features[i]-self.periods[self.informations["period_number"]].op[op].clusters[i]) / (self.periods[self.informations["period_number"]].op[op].cluster_update_count + 1))
        self.periods[self.informations["period_number"]].op[op].cluster_update_count += 1
        

    def operator_selection(self, candidate):
        #Epsilon-greedy random selection
        if np.random.rand() < self.parameters['eps'] or self.parameters["learning_mode"] == -1:
            return np.random.randint(0, self.parameters["operator_size"])
            
        #AOS
        credits = [self.periods[self.informations["period_number"]].op[ind].credits[-1] for ind in range(self.parameters["operator_size"])]
        for i in range(len(credits)):
            if credits[i] == -inf:
                return np.random.randint(0, self.parameters["operator_size"])
        
        if(np.std(credits)!= 0):
            credits = (credits - np.min(credits))/(np.max(credits)-np.min(credits))
        else:
            return np.random.randint(0, self.parameters["operator_size"])
        

        
        # for i in range(len(credits)):
        #     print( [-1* credits[i] , self.parameters["gama"] * self.get_distance(i, candidate) ] )
        values = [(-1* credits[ind] + self.parameters["gama"] * self.get_distance(ind, candidate)) for ind in range(self.parameters["operator_size"])]
        best_op = np.argmin(values)
        return best_op

    def __conf__(self):
        return ['CLRL', self.parameters["operator_size"] ,self.parameters["reward_type"],  self.parameters["eps"], self.parameters["W"], self.parameters["alpha"],self.parameters["gama"]  ,self.parameters["learning_mode"] , self.parameters["load_file"] != None]

