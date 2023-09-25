test_cases = int(input())

for _ in range(test_cases):
    pairs, gods = list(map(int, input().split()))
    stuff = {} # holds the gods as the key and what they are gods of as the value 

    for _ in range(pairs):
        god, attribute = input().split()
        stuff[god] = attribute

    for _ in range(gods):
        print(stuff[input()])

