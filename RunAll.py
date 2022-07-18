from itertools import product
import os
import threading
import time
import numpy as np
def thread_function(conf):
    time.sleep(1)
    print(conf)
    os.system(f"python ./Run_Experiment.py {' '.join(map(str,conf.values()))}")
parameters = {"pNo":np.arange(500,5001,250),"Method": ["extreme"], "W": [25,100], "eps": [0.3], "alpha": [0.9],"gama": [0.5],"learning_mode":[0,1],"loadFileName":["None"],"reward_func":[1]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
for c in configurations:
    x = threading.Thread(target=thread_function, args=(c,))
    x.start()