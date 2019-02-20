from collections import deque

numbrid = deque([])
result = [0]
index, cur_marble = 1, 0
elves = dict()

for i in range (1,100):
    numbrid.append(i)

for turns in range (1,4):
    for player in range (1,10):
        index +=2
        # if len(result) == 0:
        #     index = 1

        if index > len(result):
            while index > len(result):
                index -= len(result)

        result.insert(index, numbrid.popleft())
        cur_marble = result[index]

        if cur_marble % 23 == 0:
            print ("siin")

            if player not in elves:
                elves[player] = cur_marble
            else:
                elves[player] += cur_marble



        print ("p" + str(player)+ " " + str(result) + " Cur: " + str(cur_marble))



print (str(elves))
