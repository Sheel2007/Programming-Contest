test_cases = int(input())

for _ in range(test_cases):
    oracle = input().split()
    real = input().split()

    count = 0

    for o, r in zip(oracle, real):
        if o == r:
            count += 1

    if count < 5:
        print("Fraud")
    elif count >= 8:
        print("Oracle")
    else:
        print("Draw")