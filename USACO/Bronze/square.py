rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))

high_x = max([rect1[0], rect1[2], rect2[0], rect2[2]])
low_x = min([rect1[0], rect1[2], rect2[0], rect2[2]])

high_y = max([rect1[1], rect1[3], rect2[1], rect2[3]])
low_y = min([rect1[1], rect1[3], rect2[1], rect2[3]])

if abs(high_y - low_y) ** 2 > abs(high_x - low_x) ** 2:
    print(abs(high_y - low_y) ** 2)

else:
    print(abs(high_x - low_x) ** 2)