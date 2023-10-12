import turtle
turtle.pensize(2)
for i in range(4):
    turtle.seth(90 * i)
    turtle.fd(150)
    turtle.right(90)
    turtle.circle(-150, 45)
    turtle.goto(0, 0)