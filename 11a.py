import numpy as np

def getpower(a,b):
    rack_id = a + 10
    # fiksitud sisend 8199
    power_level = rack_id * b + 8199
    power_level *= rack_id
    hundreds_digit = int(list(reversed(str(power_level)))[2])
    result = hundreds_digit - 5
    return result

# test_asi = getpower(101,153)

maatriks = np.fromfunction(np.vectorize(getpower), (300,300), dtype=int)



x = np.array(maatriks)
def submatrix( matrix, startRow, startCol, size):
    return x[startRow:startRow+size,startCol:startCol+size]

# print maatriks

# print submatrix(maatriks, 0,0,3).sum()


max_level = 0
for z in range (1,50):
    for i in range(0,300-z):
        for j in range(0,300-z):
            if submatrix(maatriks, i,j,z).sum() > max_level:
                max_level = submatrix(maatriks, i,j,z).sum()
                out_x = i
                out_y = j
                out_z = z

print (str(out_x) + "," + str(out_y) + "," + str(out_z))
