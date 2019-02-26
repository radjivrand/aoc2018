start = []
start_row = []

with open('12a_input_demo_start.txt',"rt") as input_file:
    for line in input_file:
        start.append(line.rstrip('\n'))

for element in start:
    start_row.append(element)

print (start_row)
