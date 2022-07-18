
import csv
from itertools import product
from re import I
from scipy.stats import rankdata

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
c["reward"] = 0



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
all_results = []
# for pno in np.arange(500,5001,250):
for pno in np.arange(0,30):
    
    problem=SetUnionKnapsack('Data/SUKP',pno)
    # problem = OneMax(pno)

    learned = False
    filenames.append(problem.dosyaAdi)
    
    file_name = f"results_27June/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}--1-False-0-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_random.append(data)
    data_random_max.append(np.max(data))
    data_random_mean.append(np.mean(data))
    data_random_std.append(np.std(data))
    
    file_name = f"results_27June/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{learned}-{c['reward']}-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_RL.append(data)
    data_RL_mean.append(np.mean(data))
    data_RL_max.append(np.max(data))
    data_RL_std.append(np.std(data))

    file_name = f"results_27June/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-{learned}-{c['reward']}-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_CRL.append(data)
    data_CRL_mean.append(np.mean(data))
    data_CRL_max.append(np.max(data))
    data_CRL_std.append(np.std(data))

    file_name = f"results_27June/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-True-{c['reward']}-{problem.dosyaAdi}.csv"
    data =get_best_data(file_name, 3)
    data_RL_L.append(data)
    data_RL_L_mean.append(np.mean(data))
    data_RL_L_max.append(np.max(data))
    data_RL_L_std.append(np.std(data))

    file_name = f"results_27June/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-True-1-{problem.dosyaAdi}.csv"
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
    # data_means[ind][0] = data_RL_mean[ind]
    # data_means[ind][1] = data_CRL_mean[ind]
    # data_means[ind][2] = data_RL_L_mean[ind]
    # data_means[ind][3] = data_CRL_L_mean[ind]
    try:
        if (data_CRL_mean[ind] != data_RL_mean[ind]) and (len(data_RL_L[ind]) == len(data_CRL_L[ind])):
            print(len(data_random[ind]))
            # w,p1 = wilcoxon(data_random[ind],data_RL[ind])
            # w,p2 = wilcoxon(data_random[ind],data_CRL[ind])
            w,p1 = wilcoxon(data_RL_L[ind],data_RL[ind])
            w,p2 = wilcoxon(data_CRL_L[ind],data_CRL[ind])
            ss.append(p1)
        else:
            ss.append(1)
    except: 
         ss.append(1)
    
    # ranks = (4 - rankdata([data_random_mean[ind],data_RL_mean[ind],data_CRL_mean[ind]]).astype(int) )
    ranks = (5 - rankdata([data_RL_max[ind],data_RL_L_max[ind],data_CRL_max[ind],data_CRL_L_max[ind]]).astype(int) )
    # all_results.append([ranks[0],data_random_max[ind], data_random_mean[ind] ,data_random_std[ind], ranks[1],data_RL_max[ind], data_RL_mean[ind] ,data_RL_std[ind],p1, ranks[2],data_CRL_max[ind], data_CRL_mean[ind] ,data_CRL_std[ind],p2])
    all_results.append([ranks[0],data_RL_max[ind], data_RL_mean[ind] ,data_RL_std[ind], ranks[1],data_RL_L_max[ind], data_RL_L_mean[ind] ,data_RL_L_std[ind],p1, ranks[2],data_CRL_max[ind], data_CRL_mean[ind] ,data_CRL_std[ind],ranks[3],data_CRL_L_max[ind], data_CRL_L_mean[ind] ,data_CRL_L_std[ind],p2])
    ind += 1

ps = []
# print([data_random_max,data_random_mean , data_random_std])
# print([data_RL_max,data_RL_mean , data_RL_std])
# print([data_CRL_max, data_CRL_mean , data_CRL_std])
# print(data_random_mean)
print(data_means)
with open('myfile.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(all_results)
print(ranks)
print(np.mean(ranks,axis=0))
