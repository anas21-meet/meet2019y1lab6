import turtle
x=0
while x<300:
    y=x**2/300
    turtle.goto(x,y)
    x=x+1
turtle.mainloop()
