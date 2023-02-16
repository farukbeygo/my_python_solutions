from art import logo
import random

# initial card list
cards = {
  "A":11,
  "2":2,
  "3":3,
  "4":4,
  "5":5,
  "6":6,
  "7":7,
  "8":8,
  "9":9,
  "10":10,
  "K":10,
  "Q":10,
  "J":10,
}


# some initial values for the game
playjack = True
deposit = 10000

# some function for the game
def draw():
    """This function will draw a card from the deck!"""
    return random.choice(list(cards))

def win(x, y):
    """This function will return true if x can win the game!"""
    if ((22>x) and (x>y)) or ((22>x) and (y>21)):
        return True
    return False
        
while playjack:
    # some initial data for player
    players_cards = []
    player_string = ""
    player_total = 0
    
    # some initial data for dealer
    dealers_cards = []
    dealers_string = ""
    dealer_total = 0
    
    # some initial values for the turn
    ask_extra = True
    
    # cards are drawing, this will draw two card
    for card in range(2):
        players_cards.append(draw())
        if card==0:
            player_string+=(players_cards[card])
        else:
            player_string+=(", " + players_cards[card])
        player_total+=cards[players_cards[card]]
        
        dealers_cards.append(draw())
        dealer_total+=cards[dealers_cards[card]]

        
    # now game can start
    print(logo)
    print("Welcome to the blackjack!!")
    print(f"Your current money: ${deposit}")
    bet = int(input("How much do you want to play? $"))
    
    # turning string into useful thing
    print("Cards are drawing!!")
    print(f"  Dealer's cards: {dealers_cards[0]}" + ", X"*(len(dealers_cards) - 1))
    print(f"  Your cards: {player_string}")
    
    # now ask whether player want to take another card
    while ask_extra:
        draw_extra = input("Do you want to draw an extra card? Yes ('Y') or No ('N') ")
        if draw_extra=='Y':
            players_cards.append(draw())
            player_string+=(", " + players_cards[-1])
            player_total+=cards[players_cards[-1]]
            if player_total>21:
                ask_extra = False
            
            # now print them out
            print("Cards are drawing!!")
            print(f"  Dealer's cards: {dealers_cards[0]}" + ", X"*(len(dealers_cards) - 1))
            print(f"  Your cards: {player_string}")
    
        else:
            ask_extra = False
    
    # now thinking about 'A'
    if (('A' in players_cards) and player_total>21):
        player_total-10
    if (('A' in dealers_cards) and dealer_total>21):
        dealer_total-10
    
    # now we can finish the game
    while win(player_total, dealer_total):
        if dealer_total<22:
            dealers_cards.append(draw())
            dealer_total+=cards[dealers_cards[-1]]
        else:
            break
        
    # for the finishing game write dealers card in a string
    for card in range(len(dealers_cards)):
        if card==0:
            dealers_string+=dealers_cards[card]
        else:
            dealers_string+=(", " + dealers_cards[card])
            
    
    # print the last deal
    print("Cards are opening!!")
    print(f"  Dealer's cards: {dealers_string}")
    print(f"  Your cards: {player_string}")
    
    # find the winner
    if win(player_total, dealer_total):
        print("Player won the game!!")
        print(f"You won ${bet}!!")
        deposit+=bet
    elif (player_total == dealer_total):
        print("Draw!!")
        print("You got back your money!!")
    else:
        print("Dealer won the game!!")
        print(f"You lost ${bet}!!")
        deposit-=bet
    
    # now we can finish the turn
    if deposit>0:
        continnue = input("Do you want to play another game? Yes ('Y') or No ('N') ")
        if continnue=='N':
            playjack = False
            if (deposit-10000)>0:
                print(f"You won {deposit-10000} in total!!")
            else:
                print(f"You lost {-(deposit-10000)} in total!!")
    else:
      print("You lost all your money, you can't play anymore!!")
      playjack = False
    
    
    
    
    
    
    
    
    
    
    