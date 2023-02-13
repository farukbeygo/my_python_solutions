""""
Here is my code for rock-paper-scissors game!!!
""""
import random as rd 

tkm = ''
stay_game = True
player_point = 0
computer_point = 0

while stay_game:
    choose = rd.randint(0,3)
    if choose==0:
        tkm = 'R'
    elif choose==1:
        tkm = 'S'
    else:
        tkm = 'P'

    playerTKM = input("rock ('R'), scissors ('S') or paper ('P')")
    if (playerTKM == tkm):
        print("computer: " + tkm + ", player: " + playerTKM + ", draw")
    else:
        if (tkm == 'R'):
            if (playerTKM == 'P'):
                print("computer: " + tkm + ", player: " + playerTKM)
                print("player won the round!")
                player_point+=1
            else:
                print("computer: " + tkm + ", player: " + playerTKM)
                print("computer won the round!")
                computer_point+=1
        elif (tkm == 'P'):
            if (playerTKM == 'S'):
                print("computer: " + tkm + ", player: " + playerTKM)
                print("player won the round!")
                player_point+=1
            else:
                print("computer: " + tkm + ", player: " + playerTKM)
                print("computer won the round!")
                computer_point+=1
        else:
            if (playerTKM == 'R'):
                print("computer: " + tkm + ", player: " + playerTKM)
                print("player won the round!")
                player_point+=1
            else:
                print("computer: " + tkm + ", player: " + playerTKM)
                print("computer won the round!")
                computer_point+=1
    print("player score: " + player_point*'x' + ", computer score: " + computer_point*'x')
    
    if (player_point==3):
        stay_game = False
        print("player won the game!!!!!")
    elif (computer_point==3):
        stay_game = False
        print("computer won the game!!!!!")
