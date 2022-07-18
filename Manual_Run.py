#%% Run Experiment
# Not only cluster center, But also cluster power.
import sys
from tkinter import W

from Experiment import Experiment
from Problem import *
from Operators import *
from BinaryABC import BinaryABC
from CLRL import CLRL
 

problem= OneMax(2000)
abc = BinaryABC(problem, pop_size=20, maxFE=250*40, limit=50)
operator_pool = [ flipABC(), nABC(), ibinABC(), NBABC() ]
# parameters = {'operator_size': len(operator_pool),"pNo":2500,"reward_type": "extreme", "W": 25, "eps": 0.3, "alpha": 0.5,"gama": 0.9,"learning_mode":0,"load_file": "CLRL-4-extreme-0.3-25-0.5-0.9-1-None-1-2500.csv","reward_func":1}
parameters = {'operator_size': len(operator_pool),"pNo":2500,"reward_type": "extreme", "W": 25, "eps": 0.3, "alpha": 0.9,"gama": 0.5 ,"learning_mode":1,"load_file": "CLRL-4-extreme-0.3-25-0.9-0.5-1-None-1-2000.csv","reward_func":1}
# parameters = {'operator_size': len(operator_pool),"pNo":2500,"reward_type": "average", "W": 100, "eps": 0.3, "alpha": 0.5,"gama": 0.5,"learning_mode":0,"load_file": "CLRL-4-average-0.3-100-0.5-0.5-1-None-1-2500.csv","reward_func":1}
operator_selectors = CLRL(parameters)
alg_outs = ["convergence"]
aos_outs = ["cluster_history","operator_informations","clusters","credits","cluster_update_counts"]
exp = Experiment(abc,operator_pool,operator_selectors,
problem,algortihm_outs=alg_outs, aos_outs=aos_outs, runs=10, clear_history=True)
exp.Run()