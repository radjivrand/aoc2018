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

notes_list = []
for n in notes:
    notes_list.append(list(n))

def dots(input_string):
    regex = r"\A\.?\.?\.?\.*(#.*#)\.?\.?\.?\.*\Z"
    # test_str = "....#..#.#..##......###...###..."
    subst = "....\\1...."
    # You can manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, input_string, 0, re.MULTILINE)
    return result

def list_dots(input_list):
    counter = 0
    output_list = []
    for i in range(0,4):
        if input_list[i] == '#':
            print i
            output_list = ["."] * (4-i)
            print output_list

            break
    return output_list + input_list


start_list = list(start)

start_list = list_dots(start_list)

# tsykkel mis viskab viiekaupa edasi
for i in range(0,len(start_list)-4):
    for nl in notes_list:
        if nl == start_list[i:i+5]:
            print i

    print start_list[i:i+5]
