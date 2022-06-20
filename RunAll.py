from itertools import product
import os
import threading
import time
import numpy as np
def thread_function(conf):
    time.sleep(1)
    print(conf)
    os.system(f"python ./Run_Experiment.py {' '.join(map(str,conf.values()))}")
parameters = {"pNo":2500,"Method": ["average","average"], "W": [10,25,50,100], "eps": [0.3, 0.4, 0.5], "alpha": [0.1, 0.5, 0.9],"gama": [0.1 ,0.5, 0.9],"learning_mode":[0,1],"loadFileName":["None"],'reward_func':[0,1]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
for c in configurations:
    x = threading.Thread(target=thread_function, args=(c,))
    x.start()