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

pNo = int(sys.argv[1])
rewardType = sys.argv[2]
W = int(sys.argv[3])
eps = float(sys.argv[4])
alpha = float(sys.argv[5])
gama = float(sys.argv[6])
learning_mode = int(sys.argv[7])
loadFileName=sys.argv[8]
reward_func = int(sys.argv[9])
credit_func = int(sys.argv[10])
if loadFileName == "None":
    loadFileName = None


problem= OneMax(pNo)
abc = BinaryABC(problem, pop_size=20, maxFE=250*40, limit=50)
operator_pool = [ nABC(), ibinABC(), NBABC() ]
parameters = {'operator_size': len(operator_pool), 'reward_type': rewardType, 'W':W, 'alpha':alpha, 'gama':gama, 'eps':eps, 'learning_mode':learning_mode, 'load_file':loadFileName, 'reward_func':reward_func,'credit_func':credit_func}
operator_selectors = CLRL(parameters)
alg_outs = ["convergence"]
aos_outs = ["operator_informations","clusters","credits","cluster_update_counts"]
exp = Experiment(abc,operator_pool,operator_selectors,
problem,algortihm_outs=alg_outs, aos_outs=aos_outs, runs=30, clear_history=True)
exp.Run()