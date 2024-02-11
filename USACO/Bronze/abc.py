line = sorted(list(map(int, input().split())))

a = line[0]
b = line[1]

c = line[-1] - (a + b)

print(a, b, c)
