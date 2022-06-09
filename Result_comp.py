
import csv
from itertools import product
from Problem import *
def get_best_data(fileName, operator_size):
    datas = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        line_count = 0
        previous_iter = 0
        previous_val = 0
        for row in csv_reader:
            if len(row) > 0:
                iteration, val = row
                if iteration < previous_iter:
                    datas.append((previous_val))
                else:
                    previous_val = val
                previous_iter = iteration
        datas.append((previous_val))
    return datas
import numpy as np
parameters = {"Method": ["average", "extreme"], "W": [5, 25], "Pmin": [0.1, 0.2], "Alpha": [0.1, 0.5, 0.9]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
ind = 0
data_maks = []
data_fe_means = []
data_rlabc_means = []
data_fe_std = []
data_rlabc_std= []
data_fe = []
data_rlabc= []

stds = []


c=dict()
c["Method"] = "extreme"
c["W"] = 25
c["eps"] = 0.5
c["alpha"] = 0.5
c["gama"] = 0.9


c2=dict()
c2["Method"] = "extreme"
c2["W"] = 25
c2["eps"] = 0.1
c2["alpha"] = 0.5
c2["gama"] = 0.9

filenames=[]
ss=[]
from scipy.stats import wilcoxon
ps = []

data_random=[]
data_random_mean =[]
data_random_std =[]

data_RL =[]
data_RL_mean =[]
data_RL_max =[]
data_RL_std =[]

data_CRL=[]
data_CRL_mean =[]
data_CRL_max =[]
data_CRL_std =[]

for pno in range(1):
    problem=SetUnionKnapsack('Data/SUKP',15)
    # problem = OneMax(2000)
    learned = True
    filenames.append(problem.dosyaAdi)
    
    # file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}--1-{problem.dosyaAdi}.csv"
    # data =get_best_data(file_name, 3)
    # data_random.append(data)
    # data_random_mean.append(np.mean(data))
    # data_random_std.append(np.std(data))
    
    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{learned}-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_RL.append(data)
    data_RL_mean.append(np.mean(data))
    data_RL_max.append(np.max(data))
    data_RL_std.append(np.std(data))

    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-{learned}-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_CRL.append(data)
    data_CRL_mean.append(np.mean(data))
    data_CRL_max.append(np.max(data))
    data_CRL_std.append(np.std(data))

    w,p = wilcoxon(data_RL[pno][0:30],data_CRL[pno])
    ss.append(p)
    ind += 1

ps = []
print([data_RL_max,data_RL_mean , data_RL_std])
print([data_CRL_max, data_CRL_mean , data_CRL_std])
print([ss])
