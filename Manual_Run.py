#%% Run Experiment
# Her bir region'da farkli credit degerleri olacak.
# Not only cluster center, But also cluster power.
import sys
from tkinter import W

from numpy import flip
from Experiment import Experiment
from Problem import *
from Operators import *
from BinaryABC import BinaryABC
from CLRL import CLRL


rewardType = "average"
W = 25
eps = 0.4
alpha = 0.5
gama = 0.9
pNo = 1000
learning_mode = 1
# problem= SetUnionKnapsack('Data/SUKP',pNo)
# abc = BinaryABC(problem, pop_size=20, maxFE=40*max(problem.m, problem.n), limit=100)

problem= OneMax(pNo)
abc = BinaryABC(problem, pop_size=20, maxFE=250*40, limit=100)
# loadFileName="CLRL-4-average-0.4-25-0.5-0.3-1-False-1000.csv"
loadFileName=None
# learning_mode = 0
operator_pool = [ flipABC(),  nABC(), BABC(), ibinABC()]
parameters = {'operator_size': len(operator_pool), 'reward_type': rewardType, 'W':W, 'alpha':alpha, 'gama':gama, 'eps':eps, 'learning_mode':learning_mode, 'load_file':loadFileName}
operator_selectors = CLRL(parameters)
alg_outs = ["convergence"]
# alg_outs = []
# aos_outs = ["cluster_history","credit_history","operator_informations"]
# aos_outs = ["credits","rewards","usage_counter","success_counter","cluster_history","clusters","credit_history","reward_history","operator_informations"]

aos_outs = ["cluster_history","operator_informations","clusters","credits","cluster_update_counts"]
exp = Experiment(abc,operator_pool,operator_selectors,
problem,algortihm_outs=alg_outs, aos_outs=aos_outs, runs=30, clear_history=True)
exp.Run()