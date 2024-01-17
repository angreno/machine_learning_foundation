import numpy as np
a=[[1,2],[3,4]]
a_inv=np.linalg.inv(a)
print(a_inv)


#another way to create array  matrix

arr=np.array([[1,2],[3,4]])
print(type(arr))
print(np.linalg.inv(arr))

