from art import logo
import random

# global variables
play = True

# a function for find the number
def is_bigger(x, y):
    return x>y

while play:
    # start the game
    print(logo)
    print("Welcome to the number guessing game!!")
    print("I am thinking of a number between 1 and 100.")
    random_number = random.randint(1, 101)
    win = False
    
    # ask the level
    diff = input("Choose a diffuculty. Type 'easy' or 'hard': ")
    attempt = 0
    if diff=='easy':
        attempt=10
    else:
        attempt=5
    
    # start guessing
    for guess in range(attempt):
        print(f"You have {attempt-guess} attempts to guess the number")
        num = int(input("Make a guess: "))
        if num==random_number:
            win=True
            break
        elif is_bigger(num, random_number):
            print("Too high.")
        else:
            print("Too low.")
    
    # define whether player win
    if win:
        print(f"You made the correct guess, the number was {random_number}")
        print("You win!!!")
    else:
        print(f"You could not make the correct guess, the number was {random_number}")
        print("You lost!!!")

    # ask for another turn
    ask = input("Do you want to play another game. Type 'yes' or 'no': ")
    if ask=='no':
        play=False
    
    
    
    
