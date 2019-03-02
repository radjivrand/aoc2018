import re
import time
import numpy as np

ms = time.time()*1000.0

start, notes, start_row, notes_input = [],[],[],[]

np_start = np.array([])


with open('12a_input_demo_start.txt',"rt") as input_file:
    test = input_file
    for line in input_file:
        start.append(line.rstrip('\n'))

np_start = np.array(list(start[0]))

print (np_start)

with open('12a_input_notes.txt',"rt") as input_file:
    for line in input_file:
        notes_input.append(line.rstrip('\n'))

regex = r"(.....) => (.)"
subst = "\\1 \\2"
for element in notes_input:
    s = re.sub(regex, subst, element, 0, re.MULTILINE)
    t = s.split()
    notes.append(t)

ok_notes = []

for row in notes:
    # print row[1]
    if row[1] == "#":
        ok_notes.append(row[0])

np_notes = np.array(ok_notes)

print (np_notes)

def count_pots(input_string, shifter):
    inp_list = list(input_string)
    counter = 0
    pot_sum = 0
    for pot in inp_list:
        counter += 1
        if pot == "#":
            pot_sum += counter + shifter
            # print (counter)
    return pot_sum

pots = ".........................." + start[0] + "......................."

def get_next_row(input_string, input_notes):
    result_numbers = []
    for i in range(0, len(input_string)):
        cur_sel = input_string[i:i+5]
        for n in range(0, len(input_notes)):
            if cur_sel == input_notes[n][0] and input_notes[n][1] != ".":
                result_numbers.append(i)
    result_string = ""
    for i in range(0,len(input_string)):
        if i in result_numbers:
            result_string += "#"
        else:
            result_string += "."
    return (".." + result_string[:-2], result_numbers)

nums = []
for i in range (0,20000):
    # print (pots)
    res  = get_next_row(pots, notes)
    pots = res[0]
    nums = res[1]

print count_pots(pots, -27)
# print (pots)

new_ms = time.time()*1000.0 - ms

print (new_ms)
