def calculate_score(rolls):
    # Sort the rolls in descending order
    rolls.sort(reverse=True)

    # Check for Mia
    if rolls == [1, 2] or rolls == [2, 1]:
        return 120
    # i dedcided to return 120 because there won't be any higher score
    elif rolls[0] == rolls[1]:
        return rolls[0] * 10 + rolls[1]
    else:
        return (rolls[0] * 10 + rolls[1]) / 100
    # i decided to divide by 100 because if I didnt then 65 would beat 11.

def determine_winner(player1, player2):
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)

    if score1 > score2:
        return "Player 1 wins."
    elif score1 < score2:
        return "Player 2 wins."
    else:
        return "Tie."

while True:
    s0, s1, r0, r1 = map(int, input().split())

    if s0 == s1 == r0 == r1 == 0:
        break

    player1 = [s0, s1]
    player2 = [r0, r1]

    result = determine_winner(player1, player2)
    print(result)
