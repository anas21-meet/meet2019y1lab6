
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    stamp = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(stamp)



#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for x in range(0,START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
    new_stamp()
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
new_stamp()
def remove_tail():
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
snake.direction="Up"
UP_EDGE = 250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400
def up():
    snake.direction="Up"
    print("You pressed the up key!")
def down():
    snake.direction="Down"
    print("You pressed the down key!")
def right():
    snake.direction="Right"
    print("You pressed the right key!")
def left():
    snake.direction="Left"
    print("You pressed the left key")
    
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left, "Left")
turtle.listen()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
food_pos_num=0
for this_food_pos in food_pos :
    food.penup()
    food.goto(food_pos[food_pos_num])
    food.pendown()
    food_stamp_id=food.stamp()
    food_stamps.append(food_stamp_id)
    food_pos_num=food_pos_num+1
    if food_pos_num==4:
        break
    
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.penup()
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

def move_snake():
    for x in pos_list[0:-1]:
        if x==snake.pos():
            quit()
            
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if snake.direction=="Up":
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("You moved down!")
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("You move right!")
    elif snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("You moved left!")
    print(new_stamp())
    print(remove_tail())
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos>= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos>=UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index) 
        print("You have eaten the food!")
        if len(food_stamps) <= 6 :
                make_food()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()




    




    
    
    
        

    
        
                   
    
        
turtle.mainloop()



