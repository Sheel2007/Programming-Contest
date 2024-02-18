line = list(map(int, input().split()))
line.pop(0)

ones = []
for _ in range(len(line)):
    ones.append(1)

iterations = 0
while True:
    # Calculate the absolute differences
    line = [abs(line[i] - line[(i + 1) % len(line)]) for i in range(len(line))]
    iterations += 1
        
    if ones == line:
        break
    
print(iterations)