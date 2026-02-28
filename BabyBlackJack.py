# jack , queen , king , club reprents 10 and ace represnets 11
import random
cards= [2,3,4,5,6,7,8,9,10,10,10,10,11,]
player_hand=[]
dealer_hand=[] 
player_turn=True
def calculate_total(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total
#dealing card to the player]
player_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

#dealing 2nd card to the player and dealer
player_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

#player turn hit or stand
print("Player hand:", player_hand, "Total:", sum(player_hand))
print("Dealer shows:", dealer_hand[0])

while player_turn: 
    #checking if the player allready burested
    player_total = calculate_total(player_hand)
    if player_total>21:
        print('you busted yourself gameover')
        player_turn=False
        break
    ask=input('would you like to hit or stand').strip().lower()
    if ask=="hit":
        player_hand.append(random.choice(cards))
        print('Players hand',calculate_total(player_hand))
    elif ask=="stand":
        player_turn=False
    else:
        print('please try again')
#dealers turn (only if player did not burst 
player_turn=calculate_total(player_hand)
if player_total <= 21:
    print("\nDealer reveals:", dealer_hand, "Total:", calculate_total(dealer_hand))

while calculate_total(dealer_hand) <17:
    dealer_hand.append(random.choice(cards))
    print ("dealers hit" ,dealer_hand,"total",calculate_total(dealer_hand))

dealer_total = calculate_total(dealer_hand)
print("\nFinal Hands:")
print("Player:", player_hand, "Total:", player_total)
print("Dealer:", dealer_hand, "Total:", dealer_total)

    # Decide winner
if dealer_total > 21:
        print("Dealer busted! You win!")
elif player_total > dealer_total:
        print("You win!")
elif player_total < dealer_total:
        print("Dealer wins!")
else:
        print("It's a tie (push)!")