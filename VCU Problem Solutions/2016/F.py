line = input().split()

for index, item in enumerate(reversed(line)):
    if item not in '0123456789':
        break
    
numbers = line[(len(line) - index):] # 4, 5, 6, 7
symbols = list(reversed(line[:(len(line) - index)]))# + + 3 * +
answer = ""
answer += numbers[0]
numbers.pop(0)

i = 0

while True:
    if i >= len(numbers):
        break
    if symbols[i] in '0123456789':
        answer = "(" + symbols[i] + symbols[i + 1] + answer + ")"
        symbols.pop(i)
        
    else:
        # if it is a +
        answer  = "(" + answer + symbols[i] + numbers[i] + ")"
        
    i += 1

answer = "(" + answer + symbols[-1] + numbers[-1] + ")"
print(answer)