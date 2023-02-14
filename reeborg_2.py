#reborg try to excape from dungeon
def trace_right():
    if front_is_clear():
        move()
    else:
        turn_left()
        
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
emptiness=0
while(not at_goal()):
    if right_is_clear():
        turn_right()
        move()
        emptiness+=1
        if emptiness==4:
            emptiness=0
            move()
    else:
        trace_right()
