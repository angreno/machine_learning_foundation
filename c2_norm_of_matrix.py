import numpy as np

m=np.mat('3,3;8,8')
print(m)

output = np.linalg.norm(m)
print(output)
print(type(m))