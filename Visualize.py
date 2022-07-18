#%%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from Problem  import *
from Operators import *
show_features = True
show_datas = True
show_convergences = False 
rewardType = "extreme"
eps = 0.3
alpha = 0.1
gama = 0.9
pNo = 10
reward_func = 1
max_run=5
w = 25
learning = 0
# prob= SetUnionKnapsack('Data/SUKP',pNo)
# pName = prob.ID
# prob = OneMax(750)
pName='2500'
o="CLRL"

operator_pool = [ flipABC(), ibinABC(), NBABC() ]
operator_size = len(operator_pool)

if show_features:
    sns.set_theme(palette="tab10")
    # Visualize Cluster Centers
    file_path = f"results/cluster_history-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-{learning}-CLRL-4-extreme-0.3-25-0.9-0.9-1-None-1-2500.csv-{reward_func}-{pName}.csv"
    file_path = f"results/cluster_history-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-{learning}-None-{reward_func}-{pName}.csv"
    columns = ["op_no","iteration","run"]
    for i in range(19):
        columns.append(f"f{i}")
    df = pd.read_csv(file_path, header=None,names=columns)
    for r in range(max_run):
        temp_df = df[df["run"]==r]
        
        fig, axes = plt.subplots(5,4)
        for i in range(5):
            for j in range(4):
                if (i*4+j)>18:
                    continue
                sns.scatterplot(data=temp_df, x="iteration", y=f"f{i*4+j}", hue="op_no", ax=axes[i][j], legend = False, palette="tab10")
                # axes[i][j].set_ylim(bottom=0,top=1)
        plt.show()

if show_datas:
    #Visualize Operator Informations
    file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-{learning}-None-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df = pd.read_csv(file_path, header=None,names=columns)
    for r in range(max_run):
        temp_df = df[df["run"]==r]
        temp_df['percent']=100*(temp_df['success']/temp_df['usages'])
        fig, axes = plt.subplots(5,2)
        sns.lineplot(data=temp_df, x="iteration", y="credits", hue="op_no", ax=axes[0][0], legend = False, palette="tab10")
        sns.lineplot(data=temp_df, x="iteration", y="rewards", hue="op_no", ax=axes[0][1] ,legend = False, palette="tab10")
        sns.lineplot(data=temp_df, x="iteration", y="usages", hue="op_no", ax=axes[1][0], legend = False, palette="tab10")
        sns.lineplot(data=temp_df, x="iteration", y="success", hue="op_no", ax=axes[1][1] ,legend = False, palette="tab10")
        sns.lineplot(data=temp_df, x="iteration", y="percent", hue="op_no", ax=axes[2][1] ,legend = False, palette="tab10")
        sns.lineplot(data=temp_df, x="iteration", y="cg", hue="op_no", ax=axes[2][0] ,legend = False, palette="tab10")
        plt.legend(labels=operator_pool)
        plt.show()


if show_convergences:
    sns.set_theme(palette="tab10")
    # Visualize Cluster Centers
    file_path = f"results/operator_informations-{o}-{operator_size}-{rewardType}-{eps}-{w}-{alpha}-{gama}-{learning}-{reward_func}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df = pd.read_csv(file_path, header=None,names=columns)
    df["cg"] = df["cg"]
    figss = sns.lineplot(data=df, x="iteration", y="cg", hue="run",  legend=True, palette="tab10")
    figss.set(yscale='log')
    plt.show()