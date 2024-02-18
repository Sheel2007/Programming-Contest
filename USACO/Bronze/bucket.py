grid = []

# handle input
for _ in range(10):
    temp = []
    line = input()
    for character in line:
        temp.append(character)
    grid.append(temp)
    
# for line in grid:
#     print(line)
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "B":
            start = (i, j)
        elif grid[i][j] == "L":
            end = (i, j)
        

print(abs(start[0] - end[0]) + abs(end[1] - start[1]) - 1)