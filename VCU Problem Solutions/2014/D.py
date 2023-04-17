"""
# sample input

2
6
34
"""

instances = int(input())

for i in range(instances):
	answer = ""
	num = int(input())
	divisors = []
	
	for i in range(1, num):
		if num % 2 == 1 and i % 2 == 0: #if the number is odd dont bother trying even numbers
			continue
		if num % i == 0:
			divisors.append(i)

	if sum(divisors) == num:
		answer = "YES"
	else:
		answer = "NO"

	divisor_str = ""
	for i in divisors:
		if i == 1:
			divisor_str += "1"
		else:
			divisor_str += " " + str(i)

	print(divisor_str, answer)
