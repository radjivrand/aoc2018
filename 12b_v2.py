import numpy as np
import re
start_row = []
with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start_row.append(line.rstrip('\n'))
start = np.array(list(start_row[0]))

regex = r"(.....) => (.)"
subst = "\\1 \\2"

notes_list = []

with open('12a_input_notes.txt',"rt") as input_file:
    for line in input_file:
        s = re.sub(regex, subst, line, 0, re.MULTILINE)
        s = s.split()
        if s[1] == "#":
            inner_np = np.array(list(s[0]))
            notes_list.append(inner_np)

notes = np.array(list(notes_list))
