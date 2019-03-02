import re

start, notes, start_row, notes_input = [],[],[],[]

with open('12a_input_start.txt',"rt") as input_file:
    test = input_file
    for line in input_file:
        start.append(line.rstrip('\n'))
for element in start:
    u = element.split()
    start_row.append(element)
with open('12a_input_notes.txt',"rt") as input_file:
    for line in input_file:
        notes_input.append(line.rstrip('\n'))

regex = r"(.....) => (.)"
subst = "\\1 \\2"
for element in notes_input:
    s = re.sub(regex, subst, element, 0, re.MULTILINE)
    t = s.split()
    notes.append(t)

def padding(input_string):
    regex_a = r"\A\.\.\."
    regex_z = r"\.\.\.\Z"
    pad_counter = 0
    matches_a = re.search(regex_a, input_string)
    while not matches_a:
        input_string = "." + input_string
        matches_a = re.search(regex_a, input_string)
        pad_counter += 1
    matches_z = re.search(regex_z, input_string)
    while not matches_z:
        input_string = input_string + "."
        matches_z = re.search(regex_z, input_string)

    return(input_string,pad_counter)

front_add, end_add = 0, 0
flag = False
result = []

for o in range (1,21):
    # print(start_row[0])
    pad_result = padding(start_row[0])
    start_row[0] = pad_result[0]
    # print(start_row[0])

    for i in range(0, len(start_row[0])):

        cur_sel = start_row[0][i:i+5]
        # print (i, cur_sel)
        for note in notes:
            if note[0] == cur_sel:
                result.append(note[1])
                flag = True
                break
        if flag != True:
            result.append(".")
        flag = False
    start_row[0] = ''.join(result)
    # print (str(o) + ": " + str(start_row[0]))
    result = []

def count_pots(input_string, shifter):
    inp_list = list(input_string)
    counter = 0
    pot_sum = 0
    for pot in inp_list:
        counter += 1
        if pot == "#":
            pot_sum += counter + shifter
    return pot_sum

print (start_row[0])
print pad_result[1]

print count_pots(start_row[0], 1)
