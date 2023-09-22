import sys

for line in sys.stdin:
    line = line.split('\n')[0]

    line = list(map(int, list(line)))

    for i in range(len(line)):
        line[i] = (line[i]+5)%10
    line[0], line[3] = line[3], line[0]
    line[1], line[2] = line[2], line[1]
    
    print(line[0], line[1], line[2], line[3], sep='')
