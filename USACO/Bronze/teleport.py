a, b, x, y = list(map(int, input().split()))

raw_dist = abs(a - b)
if abs(a - x) < abs(a - y):
    dist = abs(a - x) + abs(y - b)
else:
    dist = abs(a - y) + abs(x - b)
    
if dist < raw_dist:
    print(dist)
else:
    print(raw_dist)