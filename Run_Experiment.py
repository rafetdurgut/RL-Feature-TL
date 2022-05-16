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
from AOS import *

# pNo = int(sys.argv[1])
# rewardType = sys.argv[2]
# W = int(sys.argv[3])
# eps = float(sys.argv[4])
# alpha = float(sys.argv[5])
# gama = float(sys.argv[6])

rewardType = "extreme"
W = 25
eps = 0.5
alpha = 0.5
gama = 0.3
pNo = 1

problem= SetUnionKnapsack('Data/SUKP',pNo)
abc = BinaryABC(problem, pop_size=20, maxFE=40*max(problem.m, problem.n), limit=100)

# loadFileName="results/clusters-CLRL-4-extreme-0.5-25-0.5-0.3-1-Sphere.csv"
loadFileName=None

# problem = Rosenbrock(5)
# problem = OneMax(1000)
# problem = Weierstrass(30)
# problem = Elliptic(30)
# abc = BinaryABC(problem, pop_size=20, maxFE=150*40, limit=100)
operator_pool = [ flipABC(),  nABC(), BABC(), ibinABC()]
# operator_pool = [ , binABC(), ibinABC()]
operator_selectors = ClusterRL(len(operator_pool), rewardType, W=W, alpha=alpha, gama=gama, Pmin=eps, learning_mode=-1, load_from_file=loadFileName)

alg_outs = ["convergence"]
aos_outs = ["credits","rewards","usage_counter","success_counter","cluster_history","clusters","credit_history","reward_history","feature_information"]

exp = Experiment(abc,operator_pool,operator_selectors,
problem,algortihm_outs=alg_outs, aos_outs=aos_outs, runs=1, clear_history=True)

exp.Run()