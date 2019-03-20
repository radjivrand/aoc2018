import numpy as np
import re
import time
ms = time.time()*1000.0
with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start_list = list(line.rstrip('\n'))
regex = r"(.....) => (.)"
subst = "\\1 \\2"
notes_list = []
with open('12a_input_demo_notes.txt',"rt") as input_file:
    for line in input_file:
        s = re.sub(regex, subst, line, 0, re.MULTILINE)
        s = s.split()
        if s[1] == "#":
            notes_list.append(list(s[0]))
new_ms = time.time()*1000.0 - ms

start_dict = {}
for d in range(0,len(start_list)):
    start_dict[d]=start_list[d]

print (start_dict)

def list_dots(input_list):
    counter = 0
    output_list = []
    for i in range(0,4):
        if input_list[i] == '#':
            output_list = ["."] * (4-i)
            # print ("+",i)
            break
    for j in range(1,5):
        # print (input_list[-1])

        if input_list[-j] == '#':
            output_end_list = ["."] * (5-j)
            # print("chech")
            break
    return output_list + input_list + output_end_list

# start_list = list(start)

add_dots = ["."] * 4

start_list = add_dots + start_list + add_dots

# print (''.join(start_list))
#
# start_list = list_dots(start_list)
print (''.join(start_list))

def get_next_row(input_start_list, input_notes_list):
# tsykkel mis viskab viiekaupa edasi ja leiab mis numbri ajal matchib
    newlist = []
    flag = False
    for i in range(0,len(input_start_list)):
        for nl in input_notes_list:
            if nl == input_start_list[i:i+5]:
                # newlist.append("#")
                flag = True
            # break
        if flag == True:
            newlist.append("#")
        else:
            newlist.append(".")
        flag = False
    # print (''.join(newlist))
    return newlist

# def get_next_list(input_start_list, input_notes_list):
#     for isl in range(0, len(input_start_list)):
        # print (isl)
        # for nl in input_notes_list:
        #     if isl == nl:
        #         print (key)

# get_next_list(start_list,notes_list)


# for i in range(1,41):
#     start_list = get_next_row(start_list,notes_list)
    # start_list = ["....."] + start_list
    # start_list = list_dots(start_list)
    # print (''.join(start_list))
