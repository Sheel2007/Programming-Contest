import math

test_cases = int(input())

for _ in range(test_cases):
    line = input().split()

    ballons = int(line[0])
    pack = int(line[1])

    print(math.ceil(ballons / pack))