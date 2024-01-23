import numpy as np

def isOrthogonal(a,m,n):
    if(m !=n):
        return False
    for i in range (0,n):
        for j in range (0,n):
            sum=0
            for k in range (0,n):
                sum=sum+(a[i][k] * a[j][k])
                if (i == j and sum !=1):
                    return False
                if (i !=j and sum !=0):
                    return False

                return True

        a = [[1, 1, 0],
             [1, 0, 1],
             [1, 1, 1]]

        if (isOrthogonal(a, 3, 3)):
            print("Yes its ortho")
        else:
            print("No")
