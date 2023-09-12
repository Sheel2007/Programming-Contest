# Function to check if a hand has the worst possible hand
def has_worst_hand(hand):
    # Count the occurrences of each card value
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    # Check for pairs
    removed_cards = 0
    duplicates = []
    for amount, count in card_counts.items():
        if count >= 2:
            duplicates.append(amount)

    if len(duplicates) >= 2: #if there are more than 2 duplicates fold
        return False
    else: #move max of 2 cards that are duplicates 
        for duplicate, value in zip(duplicates, hand):
            if duplicate == value:
                hand.remove(duplicate)
                removed_cards += 1

    
    while removed_cards < 2: #remove highest cards if there are no duplicates
        hand.remove(max(hand))
        removed_cards += 1

    
    # if removed_cards == 0: #remove highest cards if there are no duplicates
    #     hand.remove(max(hand))
    #     hand.remove(max(hand))
    # elif removed_cards == 1:
    #     hand.remove(max(hand))
    
    # Check for the lowest possible "high" card (maximum card value)
    max_card = max(hand)
    return max_card <= 5

# Read the number of hands to evaluate
num_hands = int(input())

# Evaluate each hand
for _ in range(num_hands):
    hand = list(map(int, input().split()))
    if has_worst_hand(hand):
        print("Bet")
    else:
        print("Fold")
