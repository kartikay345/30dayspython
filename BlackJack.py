# Simplified Blackjack (Baby Blackjack)
# J, Q, K = 10 and Ace = 11 (but can become 1 if needed)

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def calculate_total(hand):
    """Return hand total with Ace adjustment (11 -> 1 if bust)."""
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

# --- Setup hands ---
player_hand = []
dealer_hand = []

# --- Deal initial 2 cards each ---
player_hand.append(random.choice(cards))
player_hand.append(random.choice(cards))

dealer_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

print("Welcome to Blackjack!")
print("Player hand:", player_hand, "Total:", calculate_total(player_hand))
print("Dealer shows:", dealer_hand[0])

# --- Player turn (Hit / Stand) ---
player_turn = True
while player_turn:
    player_total = calculate_total(player_hand)

    if player_total > 21:
        print("You busted! Game Over.")
        player_turn = False
        break

    ask = input("Would you like to hit or stand? ").strip().lower()

    if ask == "hit":
        player_hand.append(random.choice(cards))
        print("Player hand:", player_hand, "Total:", calculate_total(player_hand))
    elif ask == "stand":
        player_turn = False
    else:
        print("Please type only: hit or stand")

# Recalculate final player total after the turn ends
player_total = calculate_total(player_hand)

# --- Dealer turn (only if player didn't bust) ---
if player_total <= 21:
    print("\nDealer reveals:", dealer_hand, "Total:", calculate_total(dealer_hand))

    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
        print("Dealer hits:", dealer_hand, "Total:", calculate_total(dealer_hand))

    dealer_total = calculate_total(dealer_hand)

    print("\nFinal Hands:")
    print("Player:", player_hand, "Total:", player_total)
    print("Dealer:", dealer_hand, "Total:", dealer_total)

    # --- Decide winner ---
    if dealer_total > 21:
        print("Dealer busted! You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie (push)!")