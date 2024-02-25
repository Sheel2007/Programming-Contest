line = input().split()
num_cities = int(line[0])
num_uni = int(line[1])

unis = list(map(int, input().split())) # cities with universities

cities = list(range(num_cities)) # 0, 1, 2, 3, 4

answer = []
final_answer = []

for i in cities:
    answer = []
    for uni in unis:
        answer.append(abs(uni - i))
        
    final_answer.append(min(answer))
    
print(max(final_answer))