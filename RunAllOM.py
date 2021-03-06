from itertools import product
import os
import threading
import time
import numpy as np
def thread_function(conf):
    time.sleep(1)
    print(conf)
    os.system(f"python ./Run_Experiment.py {' '.join(map(str,conf.values()))}")
# parameters = {"pNo":[2500],"Method": ["extreme","average"], "W": [25,50,100], "eps": [0.3, 0.4], "alpha": [ 0.5, 0.9],"gama": [0.5, 0.9],"learning_mode":[0,1],"loadFileName":["None"],'reward_func':[0,1]}
parameters = {"pNo":np.arange(500,5001,250),"Method": ["average"], "W": [25], "eps": [0.3], "alpha": [ 0.5],"gama": [0.5],"learning_mode":[0,1],"loadFileName":["None"],'reward_func':[0]}
# parameters = {"pNo":np.arange(0,30),"Method": ["average"], "W": [25], "eps": [0.3], "alpha": [ 0.5],"gama": [0.5],"learning_mode":[-1,0,1],"loadFileName":["None"],'reward_func':[0]}
configurations = [dict(zip(parameters, v)) for v in product(*parameters.values())]
for c in configurations:
    x = threading.Thread(target=thread_function, args=(c,))
    x.start()