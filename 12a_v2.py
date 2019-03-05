import re
import time

ms = time.time()*1000.0

start, notes, start_row, notes_input = [],[],[],[]

with open('12a_input_start.txt',"rt") as input_file:
    test = input_file
    for line in input_file:
        start_row.append(line.rstrip('\n'))
for element in start_row:
    u = element.split()
    start.append(element)
with open('12a_input_notes.txt',"rt") as input_file:
    for line in input_file:
        notes_input.append(line.rstrip('\n'))

regex = r"(.....) => (.)"
subst = "\\1 \\2"
for element in notes_input:
    s = re.sub(regex, subst, element, 0, re.MULTILINE)
    t = s.split()
    notes.append(t)

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

pots = ".........................." + start[0] + "................................................."

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
prev_pots = 0
for i in range (0,59):
    # print (pots)
    res  = get_next_row(pots, notes)
    pots = res[0]
    nums = res[1]
    # print (pots)


    cur_pots = count_pots(pots, -27)
    print (i, cur_pots - prev_pots)
    prev_pots = cur_pots

new_ms = time.time()*1000.0 - ms

print (new_ms)
