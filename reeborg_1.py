#reborg try to manage big obstacles
def passwall():    
    turn_left()
    move()
    turn_right()

def downwall():
    if wall_length>0:
        turn_right()
        for i in range(wall_length):
            move()
        turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
wall_length=0
while(not at_goal()):
    if wall_in_front():
        passwall()
        wall_length+=1
    else:
        move()
        downwall()
        wall_length=0
