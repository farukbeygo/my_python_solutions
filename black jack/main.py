from art import logo
import random

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


deposit = 10000
playjack = True
while playjack:
  extra = True
  player_total = 0
  dealer_total = 0
  playercardstr = ""
  print(logo)
  print("Welcome to the blackjack!!")
  print(f"Your current money: ${deposit}")
  money = int(input("How much do you want to play? $"))
  player_cards = []
  dealers_cards = []
  player_1 = random.choice(list(cards))
  player_cards.append(player_1)
  computer_1 = random.choice(list(cards))
  dealers_cards.append(computer_1)
  player_2 = random.choice(list(cards))
  player_cards.append(player_2)
  computer_2 = random.choice(list(cards))
  dealers_cards.append(computer_2)

  dealer_total = cards[computer_1] + cards[computer_2]
  
  print("Cards are drawing!!")
  print(f"Dealer's cards: {computer_1}, X")
  print(f"Your cards: {player_1}, {player_2}")
  while extra:
    extracard = input("Do you want to draw an extra card? Yes ('Y') or No ('N')")
    if extracard == 'Y':
      playercardstr = ""
      extra_card = random.choice(list(cards))
      player_cards.append(extra_card)
      print("Cards are drawing!!")
      print(f"Dealer's cards: {computer_1}, X")
      loop=0
      for card in player_cards:
        loop+=1
        playercardstr+=card
        player_total+=cards[card]
        if (len(player_cards) > loop):
          playercardstr+=", "

      
      print(f"Your cards: {playercardstr}")
      
    else:
      extra = False
      print("Cards are opening!!")
      print(f"Dealer's cards: {computer_1}, {computer_2}")
      print(f"Your cards: {playercardstr}")
      if (('A' in player_cards) and player_total>21):
        player_total-10
      if (('A' in dealers_cards) and dealer_total>21):
        dealer_total-10

      playercardstr = ""
  
  loop=0
  for card in player_cards:
    loop+=1
    playercardstr+=card
    player_total+=cards[card]
    if (len(player_cards) > loop):
      playercardstr+=", "
  
  print("Cards are opening!!")
  print(f"Dealer's cards: {computer_1}, {computer_2}")
  print(f"Your cards: {playercardstr}")

  
  if (('A' in player_cards) and player_total>21):
    player_total-10
  if (('A' in dealers_cards) and dealer_total>21):
    dealer_total-10
  if ((22>player_total) and (player_total>dealer_total)):
    print("Player won the game!!")
    print(f"You won ${money*2}!!")
    deposit = (money*2)
  elif ((player_total>21 and dealer_total>21) or (player_total==dealer_total)):
    print("Draw!!")
    print("You got back your money!!")
  else:
    print("Dealer won the game!!")
    print(f"You lost ${money}!!")
    deposit-=money

  if deposit>0:
    cont = input("Do you want to play another game? Yes ('Y') or No ('N')")
    if cont=='N':
      playjack = False
      if (deposit-10000)>0:
        print(f"You won {deposit-10000} in total!!")
      else:
        print(f"You lost {deposit-10000} in total!!")
  else:
    print("You lost all your money, you can't play anymore!!")
    playjack = False