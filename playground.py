import numpy as np
import time

a_ms = time.time()*1000.0

asi = np.string("..##..")

# print (asi)

for i in range(0,1000):

    res = np.char.find(asi, "#")

# print (res)

new_ms = time.time()*1000.0 - a_ms

print (new_ms)
