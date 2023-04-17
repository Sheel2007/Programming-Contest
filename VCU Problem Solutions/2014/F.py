"""
# sample input

5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
"""

instances = int(input())
answers = []

for i in range(instances):
	#athletes = int(input())
	scores = input().split()
	scores = [int(i) for i in scores]
	athletes = int(scores[0])
	scores.pop(0)
	average = sum(scores) / athletes
	above = 0
	for score in scores:
		if score > average:
			above += 1

	answers.append(round(above / athletes * 100))

for answer in answers:
	print(answer)
