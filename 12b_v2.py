import numpy as np
import re
import time
ms = time.time()*1000.0
start_row = []
with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start_row.append(line.rstrip('\n'))
start = start_row[0]
regex = r"(.....) => (.)"
subst = "\\1 \\2"
notes = []
with open('12a_input_demo_notes.txt',"rt") as input_file:
    for line in input_file:
        s = re.sub(regex, subst, line, 0, re.MULTILINE)
        s = s.split()
        if s[1] == "#":
            notes.append(s[0])
new_ms = time.time()*1000.0 - ms

def dots(input_string):
    regex = r"\A\.?\.?\.?\.*(#.*#)\.?\.?\.?\.*\Z"
    # test_str = "....#..#.#..##......###...###..."
    subst = "....\\1...."
    # You can manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, input_string, 0, re.MULTILINE)
    return result
start = dots(start)

# list comprehension, nested, toimib
asi = [m.start() for n in notes for m in re.finditer(re.escape(n), start)]

print (asi)
juku = []

for z in asi:
    print (z)

# print(new_start)

# for n in notes:
#     print (n, start.find(n))



# print (new_ms)
