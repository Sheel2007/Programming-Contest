line = input().split()
temp = line.copy()
result = []

for index in range(len(temp)):
    l1 = sorted(temp[index])
    str1 = ""
    for i in l1:
        str1 += i
        
    temp[index] = str1
    
same = []

for i, element in enumerate(temp):
    if i == 0 or len(same) == 0:
        same.append(line[i])
    elif sorted(element) == sorted(same[-1]):
        same.append(line[i])
    else:
        result.append(same)
        same = [line[i]]
    
result.append(same)
print(result)