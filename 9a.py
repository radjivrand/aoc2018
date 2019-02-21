from collections import deque
from datetime import datetime
a = datetime.now()

numbrid = deque([])
result = [0]
index, cur_marble = 1, 0
elves = dict()

for i in range (1,300000000):
    numbrid.append(i)

first_marble = 1

while first_marble < 7216995 :
    for player in range (1,471):
        index +=2

        if index > len(result):
            while index > len(result):
                index -= len(result)

        result.insert(index, numbrid.popleft())
        cur_marble = result[index]

        if cur_marble % 23 == 0:

            if player not in elves:
                elves[player] = cur_marble
                last_marble = cur_marble
                first_marble = cur_marble

            else:
                elves[player] += cur_marble
                first_marble = cur_marble

            result.pop(index)
            index = index - 9

            if index < 0 or index == 0:
                index += len(result)

            second_marble = result.pop(index)
            elves[player] += second_marble
            last_marble += second_marble

            cur_marble = result[index-2]

        # print ("p" + str(player)+ " " + str(result) + " Cur: " + str(cur_marble) + " index: " + str(index))

print ("first: " + str(first_marble) + ", sec: " + str(second_marble))

data_sorted = {k: v for k, v in sorted(elves.items(), key=lambda x: x[1])}

print (data_sorted)

b = datetime.now()

c = b - a
print (c)

# 470 players; last marble is worth 7217000 points
