line = input()

positive = 0
negative = 0
neutral = 0

for character in line:
    if character == 'D' or character == 'E':
        negative += 1
    elif character == 'K' or character == 'R':
        positive += 1
    else:
        neutral += 1
        
print(positive, negative, neutral)