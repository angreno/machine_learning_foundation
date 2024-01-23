import numpy as np


def isOrthogonal(a, m, n):
    if (m != n):
        return False
#A*At = I
    trans = [[0 for x in range(n)]
             for y in range(n)]

    # Find transpose
    for i in range(0, n):
        for j in range(0, n):
            trans[i][j] = a[j][i]

    prod = [[0 for x in range(n)]
            for y in range(n)]

    # Find product of a[][]
    # and its transpose
    for i in range(0, n):
        for j in range(0, n):

            sum = 0
            for k in range(0, n):
                # Since we are multiplying
                # with transpose of itself.
                # We use
                sum = sum + (a[i][k] *
                             a[j][k])

            prod[i][j] = sum

    # Check if product is
    # identity matrix
    for i in range(0, n):
        for j in range(0, n):

            if (i != j and prod[i][j] != 0):
                return False
            if (i == j and prod[i][j] != 1):
                return False

    return True


a = [[1, 0, 0],
     [1, 0, 1],
     [1, 0, 1]]

if (isOrthogonal(a, 2, 2)):
    print("Yes its ortho")
else:
    print("No")

    