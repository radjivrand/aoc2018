import numpy as np
np.set_printoptions(threshold=4000)

data = []
data_text = []

with open('10a_demo.txt',"rt") as input_file:
    for line in input_file:
        data_text.append(line.rstrip('\n'))

for element in data_text:
    s = element.replace("position=<", "")
    t = s.replace("> velocity=<", ",")
    u = t.replace(" ", "")
    v = u.replace(">", "")
    x = v.split(",")
    # print (x[0])
    data.append(x)

    # print element

# print (len(data))

# for row in range(0, len(data)):
#     # print (data[row])
#     print (int(data[row][1]) + 5 * int(data[row][3]))
#     #max x 12, min x -4
#     # max y 11, min y -3

stars = np.chararray((5,5))
stars[:] = '#'

print (stars)
# print (data_text)


#
# print ('''
# Tere
# Minu
# Uus
# Vihik''')
