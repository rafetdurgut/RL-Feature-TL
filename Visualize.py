#%%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from Problem  import *
from Operators import *
show_features = False
show_datas = True
show_convergences = False 
eps = 0.4
alpha = 0.5
gama = 0.3
pNo = 2
max_run=4
w = 25
learning = 1
reward = 'average'
prob= SetUnionKnapsack('Data/SUKP',1)
pName = prob.ID

# prob = OneMax(750)
# pName='1000'
o="CLRL"
operator_pool = [ disABC(),  nABC(), bitABC(), ibinABC()]
operator_pool = [ flipABC(),  nABC(), BABC(), ibinABC()]
operator_size = len(operator_pool)

# operator_pool = [ disABC(),  binABC(), ibinABC()]

if show_features:
    sns.set_theme(palette="tab10")
    # Visualize Cluster Centers
    file_path = f"results/cluster_history-{o}-{operator_size}-{reward}-{eps}-{w}-{alpha}-{gama}-{learning}-False-{pName}.csv"
    columns = ["op_no","iteration","run"]
    for i in range(19):
        columns.append(f"f{i}")
    df = pd.read_csv(file_path, header=None,names=columns)
    for r in range(max_run):
        temp_df = df[df["run"]==r]
        fig, axes = plt.subplots(3,2)
        sns.scatterplot(data=temp_df, x="iteration", y="f0", hue="op_no", ax=axes[0][0], legend = True, palette="tab10")
        sns.scatterplot(data=temp_df, x="iteration", y="f1", hue="op_no", ax=axes[0][1] ,legend = False, palette="tab10")
        sns.scatterplot(data=temp_df, x="iteration", y="f2", hue="op_no", ax=axes[1][0], legend = False, palette="tab10")
        sns.scatterplot(data=temp_df, x="iteration", y="f3", hue="op_no", ax=axes[1][1] ,legend = False, palette="tab10")
        sns.scatterplot(data=temp_df, x="iteration", y="f4", hue="op_no", ax=axes[2][0], legend = False, palette="tab10")
        sns.scatterplot(data=temp_df, x="iteration", y="f5", hue="op_no", ax=axes[2][1], legend = False, palette="tab10")
        axes[0][0].set_ylim(bottom=0,top=1)
        plt.show()

if show_datas:
    #Visualize Operator Informations
    file_path = f"results/operator_informations-{o}-{operator_size}-{reward}-{eps}-{w}-{alpha}-{gama}-{learning}-False-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df = pd.read_csv(file_path, header=None,names=columns)
    for r in range(max_run):
        temp_df = df[df["run"]==r]
        temp_df['percent']=100*(temp_df['success']/temp_df['usages'])
        fig, axes = plt.subplots(3,2)
        sns.lineplot(data=temp_df, x="iteration", y="credits", hue="op_no", ax=axes[0][0], legend = True, palette="tab10")
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
    file_path = f"results/operator_informations-{o}-{operator_size}-{reward}-{eps}-{w}-{alpha}-{gama}-{learning}-{pName}.csv"
    columns = ["op_no","run","cg","iteration","credits","rewards","usages","success"]  
    df = pd.read_csv(file_path, header=None,names=columns)
    df["cg"] = df["cg"]
    figss = sns.lineplot(data=df, x="iteration", y="cg", hue="run",  legend=True, palette="tab10")
    figss.set(yscale='log')
    plt.show()