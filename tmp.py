import mymodel
import numpy

model = mymodel.Mymodel()

print(model.modeldata)
model.show_data()

data = [0,0,0,0,0,0,0,0,0]
model.write_data(numpy.array(data))

