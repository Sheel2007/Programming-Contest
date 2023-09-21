# You read this correctly, it is only 2 lines of code.

numbers = list(map(int, input().split()))

print(f'The largest number is {max(numbers)} and it occurs {numbers.count(max(numbers))} time(s).')
