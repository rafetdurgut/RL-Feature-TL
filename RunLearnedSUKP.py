from itertools import product
import os
import threading
import time
import numpy as np
def thread_function(conf):
    time.sleep(1)
    print(conf)
    os.system(f"python ./Run_Experiment_SUKP.py {' '.join(map(str,conf.values()))}")
parameters = {"pNo":np.arange(0,30),"Method": ["average"], "W": [25], "eps": [0.4], "alpha": [0.5],"gama": [0.3],"learning_mode":[0,1],"loadFileName":["CLRL-4-average-0.4-25-0.5-0.3-1-False-1000.csv"]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
for c in configurations:
    x = threading.Thread(target=thread_function, args=(c,))
    x.start()
    