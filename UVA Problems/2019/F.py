def get_list(dictionary, competitors):
    rankings = []
    while len(rankings) < competitors:
        minimum = min(dictionary.values())
        # gets competitor name based on time
        min_name = list(dictionary.keys())[list(dictionary.values()).index(minimum)]

        rankings.append(min_name)
        del dictionary[min_name]
    
    return rankings


test_cases = int(input())

for _ in range(test_cases):
    competitors = int(input())
    dictionary = {}

    for i in range(competitors):
        line = input().split()

        name = line[0]
        time = float(line[1])
        # creates a dictionary where the key is the name and the time is the value
        dictionary[name] = time

    rankings = get_list(dictionary, competitors)
    for player in rankings:
        print(player)
    