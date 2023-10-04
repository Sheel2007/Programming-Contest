import math

def calculate(vi, theta, x):
    vx = vi * math.cos(theta)
    vy = vi * math.sin(theta)

    t = x / vx
    return (vy * t) - 1 /2 * 9.8 * (t ** 2)

test_cases = int(input())

for _ in range(test_cases):

    vi, theta, x = list(map(float, input().split()))

    number = calculate(vi, theta, x)

    print(math.floor(number * 1000) / 1000) # rounds down
