#%%
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
pNo = 15
reward_func = 0
max_run=5
w = 25
learning = 'False'
# prob= SetUnionKnapsack('Data/SUKP',pNo)
# pName = prob.ID

# prob = OneMax(750)
pName='2500'
o="CLRL"

operator_pool = [  flipABC(), ibinABC(), nABC(), BABC()]
operator_size = len(operator_pool)
file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-0-{learning}-{reward_func}-{pName}.csv"
columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
df_0= pd.read_csv(file_path, header=None,names=columns)
data_0 = df_0.groupby('iteration',as_index=False)['cg'].mean()
data_0['mod'] = "One Run"


file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-1-{learning}-{reward_func}-{pName}.csv"
columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
df_1= pd.read_csv(file_path, header=None,names=columns)
data_1 = df_1.groupby('iteration',as_index=False)['cg'].mean()
data_1['mod'] = "All Run"
data = data_0.append(data_1, ignore_index=True)

# file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}--1-{learning}-{reward_func}-{pName}.csv"
# columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
# df_1= pd.read_csv(file_path, header=None,names=columns)
# data_1 = df_1.groupby('iteration',as_index=False)['cg'].mean()
# data_1['mod'] = "Random"

# data = data.append(data_1, ignore_index=True)


figss = sns.lineplot(data=data, x="iteration", y="cg", hue="mod", palette="tab10")
figss.set(yscale='log')

plt.show()
# if show_convergences:
#     sns.set_theme(palette="tab10")
#     # Visualize Cluster Centers
#     file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-{learning}-{reward_func}-{pName}.csv"
#     columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
#     df = pd.read_csv(file_path, header=None,names=columns)
#     df["cg"] = df["cg"]
#     figss = sns.lineplot(data=df, x="iteration", y="cg", hue="run",  legend=True, palette="tab10")
#     figss.set(yscale='log')
#     plt.show()