iterations = int(input())

input_data = []

for i in range(1, iterations+1):
	input_data.append(input())


for i in input_data:
	data = []
	for j in i:
		j = (int(j) + 5) % 10
	
		data.append(j)
	
	data[0], data[3] = data[3], data[0]
	data[1], data[2] = data[2], data[1]
	answer = ""
	for num in data:
		answer += str(num)
	print(answer)
