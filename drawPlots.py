import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from Problem  import *
from Operators import *
show_convergences = True 
rewardType = "extreme"
W = 25
eps = 0.3
alpha = 0.9
gama = 0.5
reward_func = 0
o="CLRL"
operator_pool = [ flipABC(), nABC(), ibinABC(), NBABC() ]
operator_size = len(operator_pool)

for i in range(3500,5001, 250):
    pName=i
# for i in range(0,30):
#     prob = SetUnionKnapsack('Data/SUKP',i)
#     pName=prob.dosyaAdi
    # pName=prob.dosyaAdi
    file_path = f"results_27june/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{W}-{alpha}-{gama}--1-False-1-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df_0= pd.read_csv(file_path, header=None,names=columns)
    data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
    data_0['mod'] = "Random"
    data = pd.DataFrame(data_0)

    file_path = f"results_27june/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{W}-{alpha}-{gama}-0-False-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df_0= pd.read_csv(file_path, header=None,names=columns)
    data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
    data_0['mod'] = "One Run w-L"
    data = data.append(data_0, ignore_index=True)

    file_path = f"results_27june/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{W}-{alpha}-{gama}-0-True-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df_0= pd.read_csv(file_path, header=None,names=columns)
    data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
    data_0['mod'] = "One Run w/L"
    data = data.append(data_0, ignore_index=True)

    file_path = f"results_27june/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{W}-{alpha}-{gama}-1-False-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df_0= pd.read_csv(file_path, header=None,names=columns)
    data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
    data_0['mod'] = "All Run w-L"
    data = data.append(data_0, ignore_index=True)

    file_path = f"results_27june/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{W}-{alpha}-{gama}-1-True-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df_0= pd.read_csv(file_path, header=None,names=columns)
    data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
    data_0['mod'] = "All Run w/L"
    data = data.append(data_0, ignore_index=True)

    figss = sns.lineplot(data=data, x="iteration", y="cg", hue="mod", palette="tab10")
    figss.set_xlabel('Iteration')
    figss.set_ylabel('Objective Value')
    figss.set(yscale='log')

    plt.show()