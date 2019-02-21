import ast

data = {}
data_text = []

with open('10a_demo.txt',"rt") as input_file:
    for line in input_file:
        data_text.append(line.rstrip('\n'))

for element in data_text:
    s = element.replace("position=<", "")
    t = s.replace("> velocity=<", ",")
    u = t.replace(" ", "")
    print u.split(",")
    # print element

# kekk = ast.literal_eval(element)

# print (data_text)


#
# print ('''
# Tere
# Minu
# Uus
# Vihik''')
