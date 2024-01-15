import numpy as np
#we have created matrix through numpy
m=np.mat('3,3;8,8')
print(m)

output = np.linalg.norm(m)
print(output)
print(type(m))