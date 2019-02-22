import numpy as np
np.set_printoptions(threshold=4000)

import time

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
    data.append(x)

stars = np.chararray((31,31))
stars[:] = "."
clear = stars

for value in data:
    value[0] = int(value[0]) + 10
    value[1] = int(value[1]) + 10

# for value in data:
#     print (value[1])

for value in data:
    stars[value[0],value[1]] = "#"

    # for dot in stars:
    #     print (''.join(map(str, dot)))

for i in range(0,5):
    for value in data:
        value[0] = int(value[0]) + int(value[2])
        value[1] = int(value[1]) + int(value[3])
        stars = clear
        stars[value[0],value[1]] = "#"
    for dot in stars:
        print (''.join(map(str, dot)))
    time.sleep(0.2)
print (data)
