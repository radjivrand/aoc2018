import numpy as np


asi = np.array("..##..", dtype = 'string')

print asi

res = np.char.find(asi, "#")

print res
