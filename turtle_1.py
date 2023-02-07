import turtle
import time
import random

bullet_speed = 9
invader_speed = 3
speed=20
def move_left():
    x=player.xcor() -speed
    if x<-249:
        x=-249
    player.setx(x)
def move_right():
    x=player.xcor() +speed
    if x>249:
        x=249
    player.setx(x)

def shoot():
    x=player.xcor()
    y=player.ycor()
    bullet.setposition(x,y+40)
    bullet.showturtle()



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

#downloads image to shape database -- copy paste to shape()
turtle.register_shape("images/rocket2.gif")
turtle.register_shape("images/rocket3.gif")
turtle.register_shape("images/rocket4.gif")
player = turtle.Turtle()
player.shape("images/rocket2.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)

#bullet 
#Creates bullet and shape and postion etc
bullet=turtle.Turtle()
bullet.color("lightblue")
bullet.shape("images/rocket4.gif")
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

#invader turtle 
#Creates the invader turtle
invader=turtle.Turtle()
invader.shape("images/rocket3.gif")
invader.up()
invader.speed(0)
invader.setposition(-260,260)

#score stuff
score = 0

#creates scoreboard
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("Yellow")
score_pen.up()
score_pen.setposition(-290,310)
score_pen.write("Score %s" %score)
score_pen.hideturtle()

#keyboard binds
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(shoot, "space")

#I have no clue. detects if bullet hits enemy, updates score, and stuff :)
while True:
    bullet.forward(bullet_speed)
    invader.forward(invader_speed)
    if invader.xcor()>260 or invader.xcor()<-260:
        invader.right(180)
        invader.forward(invader_speed)

    if abs(bullet.xcor()-invader.xcor())<15 and abs(bullet.ycor()-invader.ycor())<15:
        bullet.hideturtle()
        score = score+10
        score_pen.clear()
        score_pen.write("Score %s" %score)
        invader.hideturtle()
        
        invader.showturtle()
        x=random.randint(-250,250)
        invader.setposition(x,250)

        player.setposition(0,-250)

delay = input("Enter")