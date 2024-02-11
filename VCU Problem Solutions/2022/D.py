from collections import Counter

instances = int(input())
lines = []

for _ in range(instances):
    lines.append(input())
    
for line in lines:
    character = Counter(line)
    character = max(character, key= character.get)
    count = 0
    for value in line:
        if value == str(character):
            count += 1
            
    print(f"{str(character)} {count}")