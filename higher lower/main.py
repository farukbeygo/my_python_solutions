# import section
from gamedata import data
from art import logo
import random

# some initial globals
play = True

# function for control to who has more follower
def popular(x, y):
    return x['follower_count']>y['follower_count']

def right_choice(x, y, guess):
    """This function a bit messy, I know :P"""
    if popular(x, y):
        if guess=='A':
            return True
    else:
        if guess=='B':
            return True
    return False

while play:
    # start the game
    correct = True
    score = 0
    print(logo)
    print("\n\n")
    while correct:
        choice_A = random.choice(data)
        choice_B = random.choice(data)
        # check for if they are equal
        while choice_A == choice_B:
            choice_B = random.choice(data)
        
        # main game part, ask, print
        print(f"A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}")
        print(f"B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}")
        guess = input("Who has more followers? Type A or B: ")
        print("\n\n")
        if right_choice(choice_A, choice_B, guess):
            score+=1
            print(f"You are right!! Current score {score}")
        else:
            correct = False
            print(f"That's wrong!! Your final score {score}")
            
        
        
        
    # ask for another turn
    ask = input("Do you want to play again? Type 'yes' or 'no': ")
    if ask =='no':
        play = False