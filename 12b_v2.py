import numpy as np
import re
import time
ms = time.time()*1000.0
start_row = []
with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start_row.append(line.rstrip('\n'))
start = np.array(list(start_row[0]))
regex = r"(.....) => (.)"
subst = "\\1 \\2"
notes_list = []
with open('12a_input_demo_notes.txt',"rt") as input_file:
    for line in input_file:
        s = re.sub(regex, subst, line, 0, re.MULTILINE)
        s = s.split()
        if s[1] == "#":
            inner_np = np.array(list(s[0]))
            notes_list.append(inner_np)
notes = np.array(list(notes_list))

def get_next_numbers(start_in, notes_in):
    result_numbers = []
    for i in range (0, (len(start_in)-4)):
        current_slice = (start_in[i:i+5])
        for n in notes_in:
            if (n == current_slice).all():
                result_numbers.append(i+2)
                break
    empty_start = np.chararray((len(start_in)))
    # print empty_start
    empty_start[:] = "."
    for a in result_numbers:
        # print (a)
        empty_start[a] = "#"
    return empty_start

print start
print get_next_numbers(start, notes)

new_ms = time.time()*1000.0 - ms

print (new_ms)
