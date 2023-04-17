"""
#sample input
6
"""

seat_num = int(input())

seat_list = []

for i in range(seat_num):
	if i == 0:
		seat_list.append(1)
	else:
		seat_list.append(seat_list[i - 1] + 1)

print(seat_list)

i = 0

while True:
	if len(seat_list) == 1:
		break
	
	i += 2
	if i - len(seat_list) > 0:
		i = i - len(seat_list)
	
	print(seat_list, i)
	seat_list.pop(i)

print(seat_list[0])
