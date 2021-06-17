import numpy as np


class Mymodel:
    filename = "./Model/mymodel.model" 
    modeldata = []
    

    def __init__(self, filename_=filename):
        self.filename = filename_
        try:
            self.modeldata = np.loadtxt(filename_)
        except Exception as ex:
            print(ex)

    def write_data(self, data, filename_=filename):
        # Data should be numpy array
        try:
            np.savetxt(filename_, data)
        except Exception as ex:
            print(ex)
    
    def show_data(self):
        print(self.modeldata)
        print(type(self.modeldata))




