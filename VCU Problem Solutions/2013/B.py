"""
For anyone who is reading this:
First of all wow
Second, when you look over this code and try to understand it
just keep in mind that this is by no means that optimal solution
and this code only works when the length is 3 or 4.
"""

length = int(input())

buildings = []

for _ in range(length):
    line = input().split()
    line = [int(i) for i in line]
    buildings.append(line)

def spiral(buildings):
    answers = []
    for index, building in enumerate(buildings):
        if index == 0:
            for item in building:
                answers.append(item)
            continue
        if index != 0 and index != len(buildings) - 1: #if not first or last row
            answers.append(building[-1])
            continue
        for i in reversed(building):
            answers.append(i) # add the bottom row backwards

    l = [buildings[x][0] for x in range(1, length)][:-1]
    for p in reversed(l):
        answers.append(p)

    temp = []
    for building in buildings:
        for num in building:
            temp.append(num)

    for index in range(len(answers)):
        if answers[index] in temp:
            temp.remove(answers[index])

    if len(temp) == 1:
        answers.append(temp[0])
    else:
        def alternate(temp):
            count = length - 2
            
            for item in temp:
                if count > 0:
                    answers.append(item)
                    count -= 1
                else:
                    break
        
        while True:
            alternate(temp)
            for a in answers:
                if a in temp:
                    temp.remove(a)
            if len(temp) != 0:
                temp = list(reversed(temp))
            else:
                break


    return answers


answer = spiral(buildings)
for number in answer:
    print(number, end=" ")
