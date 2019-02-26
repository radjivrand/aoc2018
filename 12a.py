import re

start, notes, start_row, notes_input = [],[],[],[]

with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start.append(line.rstrip('\n'))

for element in start:
    start_row.append(element)

with open('12a_input_demo_notes.txt',"rt") as input_file:
    for line in input_file:
        notes_input.append(line.rstrip('\n'))

regex = r"(.....) => (.)"
subst = "\\1 \\2"

for element in notes_input:
    s = re.sub(regex, subst, element, 0, re.MULTILINE)
    t = s.split()
    notes.append(t)


lulla = "kabi"

lulla.append('s')

print lulla
