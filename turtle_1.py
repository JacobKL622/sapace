import turtle

#setting up the screen
scr1 = turtle.Screen()
scr1.bgcolor("black")
scr1.title("HOMEINVADERS")

#border stuff
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()





delay = input("Enter")