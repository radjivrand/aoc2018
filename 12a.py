import re

start, notes, start_row, notes_input = [],[],[],[]

with open('12a_input_demo_start.txt',"rt") as input_file:
    test = input_file
    for line in input_file:
        start.append(line.rstrip('\n'))

for element in start:
    u = element.split()
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




a = 2

juku = start_row[0][a:a+5]

for asi in notes:
    if asi[0] == juku:
        print (asi[0])
        print (asi[1])