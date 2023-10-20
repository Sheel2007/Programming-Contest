from itertools import combinations

def get_average_tax(people, taxes):
    total = 0
    total_combs = 0
    for n in range(1, people+1):
        # get all possible combinations for each num of taxes
        combinations_list = list(map(list, list(combinations(taxes, n))))

        for comb in combinations_list: # iterate through each combination
            total += sum(comb)
            total_combs += 1
    
    return total / total_combs

test_cases = int(input())

for _ in range(test_cases):
    people = int(input())
    taxes = list(map(int, input().split()))

    print(f'{round(get_average_tax(people, taxes), 3)}')

# there is a mistake in the sample output for the second test case, it should be 30.968 if they want us to round for the first one