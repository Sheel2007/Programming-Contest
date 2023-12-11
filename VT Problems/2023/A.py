num_games = int(input())
num_friends = int(input())

games = {}
friends = []

for _ in range(num_games):
    line = input().split()
    games[line[0]] = [int(line[1]), 0]

# print(games)

for _ in range(num_friends):
    line = input().split()

    friends.append(int(line[0]))

    for game in line[1:]:
        games[game][1] += 1
# print(friends)
#print(games)

feasable_games = {}

low_cost = None
lowest_game = ""

for key, (price, count) in games.items():
    cost = (num_friends - count) * price

    can_afford = 0

    for f in friends:
        if f >= price:
            # print(f, price)
            can_afford += f // price

    if can_afford >= num_friends - count:
        if low_cost == None:
            low_cost = cost
            lowest_game = key
        elif cost < low_cost:
            low_cost = cost
            lowest_game = key
        

if low_cost == None:
    print("no games found")
else:
    print(lowest_game, low_cost)
