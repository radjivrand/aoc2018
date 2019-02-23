import numpy as np
np.set_printoptions(threshold=4000)

import time

data = []
data_text = []
# veloce = []

with open('10_real.txt',"rt") as input_file:
    for line in input_file:
        data_text.append(line.rstrip('\n'))

for element in data_text:
    s = element.replace("position=<", "")
    t = s.replace("> velocity=<", ",")
    u = t.replace(" ", "")
    v = u.replace(">", "")
    x = v.split(",")
    data.append(x)

input_data = np.array(data)
normal_data = input_data.astype(int)

position = np.hsplit(normal_data, 2)[0]
veloce = np.hsplit(normal_data, 2)[1]

for value in position:
    value[0] = int(value[0])
    value[1] = int(value[1])

# print (position + veloce)

smallest = 2000
smallest_i = 0

for i in range(0,10418):
    position += veloce
    # std_asi = np.std(position,axis=0)[1]
    # if  std_asi < smallest:
    #     # print ("on")
    #     smallest_i = i

print (position)

stars = np.chararray((600,600))
stars[:] = "."

for value in position:
    stars[value[1],value[0]] = "#"

for dot in stars:
    print (''.join(map(str, dot)))
