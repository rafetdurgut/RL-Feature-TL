import csv
import os

import numpy as np

class Log:
    def __init__(self, data, folder, file_name, configuration,pNo):
        file_name = folder + '/' + file_name + '-' + '-'.join(map(str, configuration)) + '-' + str(pNo) +'.csv'
        with open(file_name, 'a') as f:
            write = csv.writer(f)
            write.writerows(data)
            
class Logger:
    def __init__(self, object, outs, out_folder, conf, ID):
        self.object = object
        self.outs = outs
        self.out_folder = out_folder
        self.conf = '-'.join(map(str, conf))
        self.ID = ID
        if not os.path.exists(out_folder):
            os.makedirs(out_folder)

    def clear_history(self):
        for o in self.outs:
            file_name = self.out_folder + '/' + o + '-' + self.conf + '-' + self.ID +'.csv'
            if os.path.exists(file_name):
                os.remove(file_name)  
    def log(self):
        for o in self.outs:
            if hasattr(self.object, o):
                writing_data = getattr(self.object, o)
                if isinstance(writing_data,(list,np.ndarray)):
                    #writing_data = np.asarray(writing_data)
                    file_name = self.out_folder + '/' + o + '-' + self.conf + '-' + self.ID +'.csv'
                    # if writing_data.ndim > 2:
                    #     with open(file_name, 'a') as f:
                    #         write = csv.writer(f,z)
                    #         for data in writing_data:
                    #             write.writerows(data)
                    # else:
                    with open(file_name, 'a') as f:
                        write = csv.writer(f)
                        if isinstance(writing_data[0], (np.float64,np.int64,np.int32,np.float32)):
                            write.writerow(writing_data)
                        elif len(writing_data[0])>1 and isinstance(writing_data[0][0],(list,np.ndarray)):
                            for l in writing_data:
                                for o in l:
                                    write.writerow([*o])
                        else:
                            write.writerows(writing_data)




