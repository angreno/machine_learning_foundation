import numpy as np
a=[[12,7],[4,5],[3,8]]
result=[[0,0,0],[0,0,0],[0,0,0,]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[j][i]=a[i][j]
for r in result:
    print(r)

