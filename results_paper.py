
import csv
from itertools import product
from re import I

import pandas as pd
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
c["reward"] = 0.5


c2=dict()
c2["Method"] = "extreme"
c2["W"] = 25
c2["eps"] = 0.3
c2["alpha"] = 0.9
c2["gama"] = 0.5

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

data_RL_L=[]
data_RL_L_mean =[]
data_RL_L_max =[]
data_RL_L_std =[]

data_CRL_L=[]
data_CRL_L_mean =[]
data_CRL_L_max =[]
data_CRL_L_std =[]
ind = 0
data_means = np.zeros((30,4))
data_maxs = []
# for pno in np.arange(500,5001,250):
for pno in np.arange(0,30):
    
    problem=SetUnionKnapsack('Data/SUKP',pno)
    # problem = OneMax(pno)

    learned = False
    filenames.append(problem.dosyaAdi)
    
    # file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}--1-False-1-{problem.dosyaAdi}.csv"
    # data =get_best_data(file_name, 3)
    # data_random.append(data)
    # data_random_max.append(np.max(data))
    # data_random_mean.append(np.mean(data))
    # data_random_std.append(np.std(data))
    
    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{learned}-1-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_RL.append(data)
    data_RL_mean.append(np.mean(data))
    data_RL_max.append(np.max(data))
    data_RL_std.append(np.std(data))

    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-{learned}-1-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_CRL.append(data)
    data_CRL_mean.append(np.mean(data))
    data_CRL_max.append(np.max(data))
    data_CRL_std.append(np.std(data))

    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-True-1-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_RL_L.append(data)
    data_RL_L_mean.append(np.mean(data))
    data_RL_L_max.append(np.max(data))
    data_RL_L_std.append(np.std(data))

    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-True-1-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_CRL_L.append(data)
    data_CRL_L_mean.append(np.mean(data))
    data_CRL_L_max.append(np.max(data))
    data_CRL_L_std.append(np.std(data))

    # data_means[ind][0] = data_random_mean[ind]
    # data_means[ind][1] = data_RL_mean[ind]
    # data_means[ind][2] = data_CRL_mean[ind]
    # data_means[ind][3] = data_RL_L_mean[ind]
    # data_means[ind][4] = data_CRL_L_mean[ind]
    data_means[ind][0] = data_RL_mean[ind]
    data_means[ind][1] = data_CRL_mean[ind]
    data_means[ind][2] = data_RL_L_mean[ind]
    data_means[ind][3] = data_CRL_L_mean[ind]

    
    # print(data_random_mean[ind])
    # print(data_CRL_mean[ind])
    # print(data_RL_mean[ind])
    # print(len(data_RL[ind]))
    # print(len(data_CRL[ind]))
    # w,p = wilcoxon(data_RL[ind],data_random[ind])
    # if (data_CRL_mean[ind] != data_RL_mean[ind]) and (len(data_RL[ind]) == len(data_CRL[ind])):
    #     w,p = wilcoxon(data_RL[ind],data_CRL[ind])
    #     print(p)
    #     print(pno)
        
    # ss.append(p)
    # else:
    #     ss.append(1)
    ind += 1

ps = []
# print([data_random_max,data_random_mean , data_random_std])
# print([data_RL_max,data_RL_mean , data_RL_std])
# print([data_CRL_max, data_CRL_mean , data_CRL_std])
# print(data_random_mean)
print(data_means)
from scipy.stats import rankdata
ranks = []
for i in range(30):
    ranks.append(1+len(data_means[i]) - rankdata(data_means[i]).astype(int) )

# pd_data = pd.DataFrame(data_means,columns=['random','one run','all run','one run w/l','all run w/l'])
print(ranks)
print(np.mean(ranks,axis=0))
