def calculate(r, c, k, t, starting_row, starting_col, grid):
    
    # print(starting_row, starting_col)
    
    starting_col -= 1
    starting_row -= 1
    
    kt = k * t
    
    lower_right_x = starting_col + kt
    lower_right_y = starting_row + kt
    
    lower_left_x = starting_col - kt
    lower_left_y = starting_row + kt
    
    upper_right_x = starting_col + kt
    upper_right_y = starting_row - kt
    
    upper_left_x = starting_col - kt
    upper_left_y = starting_row - kt

    # print(f"Upper Left: ({upper_left_y}, {upper_left_x}), Bottom Right ({lower_right_y}, {lower_right_x})")

    total = 0

    for i in range(upper_left_y, lower_left_y):
        try:
            for j in range(len(grid[i])):
                try:
                    # print(f"({i}, {j}): {grid[i][j]}")
                    total += grid[i][j]
                except:
                    # print(f"cant find cell at ({i}{j})")
                    continue;
        except:
            break
        
    return total


test_cases = int(input())

for _ in range(test_cases):
    line = input().split()
    
    r, c, k, t = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    
    line = input().split()
    
    starting_row, starting_col = int(line[0]), int(line[1])
    
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))
    
    grid = [line1] + [line2] + [line3]
    
    print(calculate(r, c, k, t, starting_row, starting_col, grid))
    # print('-----------------------')