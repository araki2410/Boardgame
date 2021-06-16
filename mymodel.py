import numpy as np


class Mymodel:
    filename = "./Model/mymodel.model" 
    modeldata = []
    

    def __init__(self, filename="./Model/mymodel.model"):
        self.filename = filename 
        try:
            file_ = open(filename, "a")
            self.modeldata = np.array(file_)
            file_.close()
        except Exception as ex:
            print(ex)

    def write_data(self, data, filename):
        # Data should be numpy array
        try:
            file_ = open(filename, "w+")
            file_.write(data)
        except Exception as ex:
            print(ex)
        finally:
            file_close()
    
    def show_data(self):
        print(self.modeldata)
        print(type(self.modeldata))




