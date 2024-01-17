import numpy as np


#to create a vector we use numpy in following way
#basically we create a array

v = np.arange(9)
print(type(v))

output = np.linalg.norm(v)
print("vector norm ",output)


