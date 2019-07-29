import turtle
#num_pts was 5 I changed it to 9 to increase sides.
num_pts=12
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.fd(100)
turtle.mainloop()

result=[]
for count in range(1,10):
    if count % 3==0:
        result.append('Fizz')
    else:
        result.append(count)
        

