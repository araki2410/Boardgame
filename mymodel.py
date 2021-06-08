import numpy as np


class Mymodel:
    filedir = "./Model"
    filename = filedir + "mymodel.model"
    modeldata = []
    

    def __init__(self, filename="mymodel.model"):#self.filename):
        self.filename = filename
        try:
            file_ = open(filename, "r+")
            self.modeldata = np.array(file_)
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
    


