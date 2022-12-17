
import csv
from itertools import product
from re import I
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
c["eps"] = 0.3
c["alpha"] = 0.9
c["gama"] = 0.5
c["reward"] = 0


c2=dict()
c2["Method"] = "average"
c2["W"] = 50
c2["eps"] = 0.3
c2["alpha"] = 0.5
c2["gama"] = 0.9

filenames=[]
ss=[]
from scipy.stats import wilcoxon
ps = []

data_random=[]
data_random_max =[]
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
ind = 0
for pno in np.arange(500,5001,250):
# for pno in np.arange(0,30):
    
    # problem=SetUnionKnapsack('Data/SUKP',pno)
    problem = OneMax(pno)
    # learned = False
    # filenames.append(problem.dosyaAdi)
    
    file_name = f"results/convergence-CLRL-4-average-0.3-25-0.5-0.5-1-None-0-{problem.dosyaAdi}.csv"
    # data =get_best_data(file_name, 3)
    # data_RL.append(data)
    # data_RL_mean.append(np.mean(data))
    # data_RL_max.append(np.max(data))
    # data_RL_std.append(np.std(data))


ps = []
print(data_RL_mean)
print(data_RL_max)
