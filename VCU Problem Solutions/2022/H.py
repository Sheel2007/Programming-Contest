line = list(map(int, input().split()))[:-1]
iterations = 0

while True:
    iterations = iterations + 1
    line[0] = abs(line[0] - line[1])
    line[1] = abs(line[1] - line[2])
    line[2] = abs(line[2] - line[3])
    line[3] = abs(line[3] - line[0])
    if line[0] == line[1] == line[2] == line[3]:
        break
    
print(iterations)