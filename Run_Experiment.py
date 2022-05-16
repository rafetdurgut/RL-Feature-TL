
#%% Run Experiment
# Her bir reward atamasından sonra kredi değerlerini tekrar hesapla.
# Reward sıfırdan küçükse de kredileri güncelle.
# Average ve min rewards 
from Experiment import Experiment
from Problem import *
from Operators import *
from BinaryABC import BinaryABC
from AOS import *

problem = SetUnionKnapsack('Data/SUKP', 8)
# problem = OneMax(1000)
operator_pool = [ nABC(), ibinABC(), disABC(), binABC()]
operator_selectors = ClusterRL(len(operator_pool), 'extreme', 25,0.5, 0.1,0.3)
abc = BinaryABC(problem, pop_size=10, maxFE=2000,
                        limit=100)
alg_outs = ["convergence"]
aos_outs = ["credits","rewards","usage_counter","success_counter","cluster_history","operator_informations"]

exp = Experiment(abc,operator_pool,operator_selectors,
problem,algortihm_outs=alg_outs, aos_outs=aos_outs, runs=1, clear_history=True)
exp.Run()


