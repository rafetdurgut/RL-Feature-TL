
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


parameters = {"pNo":[0],"Method": ["extreme"], "W": [25], "eps": [0.3], "alpha": [0.9],"gama": [0.5],"learning_mode":[0],"loadFileName":["CLRL-4-extreme-0.3-25-0.9-0.5-1-None-1-1-2500.csv"],"reward_func":[1],"credit_func":[1],"load_func":[0,1]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
for c in configurations:

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
        # file_name = f"results/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}--1-False-0-{problem.dosyaAdi}.csv"
        # data =get_best_data(file_name, 3)
        # data_random.append(data)
        # data_random_max.append(np.max(data))
        # data_random_mean.append(np.mean(data))
        # data_random_std.append(np.std(data))
        
        file_name = f"results_27june/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{c['loadFileName']}-{c['reward_func']}-{c['credit_func']}-0-{problem.dosyaAdi}.csv"
        data =get_best_data(file_name, 3)
        data_RL.append(data)
        data_RL_mean.append(np.mean(data))
        data_RL_max.append(np.max(data))
        data_RL_std.append(np.std(data))

        file_name = f"results_27june/convergence-CLRL-4-{c['Method']}-{c['eps']}-{c['W']}-{c['alpha']}-{c['gama']}-0-{c['loadFileName']}-{c['reward_func']}-{c['credit_func']}-1--{problem.dosyaAdi}.csv"
        data =get_best_data(file_name, 3)
        data_CRL.append(data)
        data_CRL_mean.append(np.mean(data))
        data_CRL_max.append(np.max(data))
        data_CRL_std.append(np.std(data))
        # print(data_random_mean[ind])
        if (data_CRL_mean[ind] != data_RL_mean[ind]) and (len(data_RL[ind]) == len(data_CRL[ind])):
            w,p = wilcoxon(data_RL[ind],data_CRL[ind])
            ss.append(p)
        else:
            ss.append(1)
        ind += 1
    ps = []
    # print([data_random_max,data_random_mean , data_random_std])
    # print([data_RL_max,data_RL_mean , data_RL_std])
    # print([data_CRL_max, data_CRL_mean , data_CRL_std])
    # print(data_random_mean)
    print(c)
    print(data_RL_mean)
    print(data_CRL_mean)
    print('-'*50)
    print(data_RL_max)
    print(data_CRL_max)
    print('-'*50)
    print(sum(map(lambda x : x%2 == 1, listOfElems)))

