import numpy as np

def printTriangle(number):
    if number >= 3:
        tri = np.zeros((number+2, number*2+3))
        for i in range(len(tri)):
            for j in range(len(tri[0])):
                if i == 0 and (j == 0 or j%2 == 0):
                    tri[i,j] = 1
                elif(i % 2 != 0):
                    tri[i,j] = 0
                else:
                    if i == j or j == len(tri[0])-i-1:
                        tri[i,j] = 3
        
        for i in tri:
            for j in i:
                print(" * ", end='') if j != 0 else print('   ', end='')
            print()
    else:
        print('minimum number is 3')
        
printTriangle(5)
