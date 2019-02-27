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

def add_to_start(string_in):
    counter = 0
    regex = r"\A\.\.\."
    matches = re.search(regex, string_in)
    while not matches:
        string_in = "." + string_in
        counter +=1
        matches = re.search(regex, string_in)
    return (string_in, counter)
def add_to_end(string_in):
    counter = 0
    regex = r"\.\.\.\Z"
    matches = re.search(regex, string_in)
    while not matches:
        string_in = string_in + "."
        counter +=1
        matches = re.search(regex, string_in)
    return (string_in, counter)

front_add, end_add = 0, 0
flag = False
result = {}

# print (start_row[0])

for o in range (1,21):
    result[o] = []
    fr_dots = add_to_start(start_row[0])
    start_row[0] = fr_dots[0]
    front_add += fr_dots[1]

    end_dots = add_to_end(start_row[0])
    start_row[0] = end_dots[0]
    end_add += end_dots[1]

    for i in range(0, len(start_row[0])):
        cur_sel = start_row[0][i:i+5]
        # print (i, cur_sel)
        for note in notes:
            if note[0] == cur_sel:
                result[o].append(note[1])
                flag = True
                break
        if flag != True:
            result[o].append(".")
        flag = False


for row in result:
    print (row[0])

print (start_row[0])
print (front_add)
