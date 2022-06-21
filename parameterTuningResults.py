from itertools import product
import os
import threading
import time
import numpy as np
import csv
from itertools import product
from Problem import *
from os.path import exists
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
from Problem import OneMax
from scipy.stats import wilcoxon

def thread_function(conf):
    time.sleep(1)
    print(conf)
    os.system(f"python ./Run_Experiment.py {' '.join(map(str,conf.values()))}")
parameters = {"pNo":[2500],"Method": ["average","average"], "W": [10,25,50,100], "eps": [0.3, 0.4, 0.5], "alpha": [0.1, 0.5, 0.9],"gama": [0.1 ,0.5, 0.9],"loadFileName":["None"],'reward_func':[0,1]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
ss = []

for c in configurations:
    data_RL =[]
    data_RL_mean =[]
    data_RL_max =[]
    data_RL_std =[]

    data_CRL=[]
    data_CRL_mean =[]
    data_CRL_max =[]
    data_CRL_std =[]
    ind = 0
    pno = 2500
    problem = OneMax(pno)
    learned = False

    file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{learned}-{c['reward_func']}-{problem.dosyaAdi}.csv"
    file_name2 = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-{learned}-{c['reward_func']}-{problem.dosyaAdi}.csv"
    if exists(file_name) and exists(file_name2):
        data =get_best_data(file_name, 3)
        data_RL.append(data)
        data_RL_mean.append(np.mean(data))
        data_RL_max.append(np.max(data))
        data_RL_std.append(np.std(data))

        file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-1-{learned}-{c['reward_func']}-{problem.dosyaAdi}.csv"
        data =get_best_data(file_name, 3)
        data_CRL.append(data)
        data_CRL_mean.append(np.mean(data))
        data_CRL_max.append(np.max(data))
        data_CRL_std.append(np.std(data))

        if len(data_CRL) == len(data_CRL):
            w,p = wilcoxon(data_RL[ind],data_CRL[ind])
            if p<0.05:
                print(p)
                print(c)
                print(data_CRL_mean)
            ss.append(p)
        else:
            ss.append(1)
print(ss)