""" Here is our question: We have first cordinates of queen(chess), and we want to 
    know whether queen can go to second cordinates that we have taken as input """


#quenn can move like rock, or move in a linear line
#so we must check this
#take input's firstly

#these are first cordinates for queen
column_1 = int(input())
row_1 = int(input())

#these are second cordinates for queen
column_2 = int(input())
row_2 = int(input())

#we must determine our input are between 1-8
if 0<column_1<9 and 0<row_1<9 and 0<column_2<9 and 0<row_2<9:
    #rock like, one of the coordinates must stay same while other one change
    if (column_1 == column_2) or (row_1 == row_2):
        print("YES")
    #consider lineer change
    elif abs(column_1 - column_2) == abs(row_1 - row_2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
