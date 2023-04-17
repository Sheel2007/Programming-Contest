"""
# sample input

2
40 20
20 40
"""

instances = int(input())
answers = []

for i in range(instances):
	sum, difference = input().split()
	sum = int(sum)
	difference = int(difference)

	if sum < difference:
		answers.append("impossible")
		continue

	num1 = (sum + difference) / 2
	num2 = sum - num1

	answers.append((int(num1), int(num2)))


for i in range(len(answers)):
	if answers[i] == "impossible":
		print(answers[i])
	else:
		num1, num2 = answers[i]
		print(num1, num2)
