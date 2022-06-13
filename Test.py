
from BinaryABC import BinaryABC
from CLRL import CLRL
from Problem import OneMax


parameters = {'operator_size':3, 'max_period':5, 'eps': 0.5, 'alpha': 0.5, 'gama': 0.5, 'load_file':'asd'}

problem= OneMax(100)
abc = BinaryABC(problem, pop_size=20, maxFE=250*40, limit=100)
c = CLRL(parameters)
c.set_algorithm(abc,0)
c.start()

for i in range(250):
    c.next_iteration()