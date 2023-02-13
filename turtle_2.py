import turtle
import time
import random
import os

#VARIABLES
bullet_speed = 9
invader_speed = 20
speed=20
#PLAYER MOVEMENT AND SHOOTING
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

#PLAYER 
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
bullet.penup
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

#bullet state
#ready
bulletstate="ready"

#fire

def shoot():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 40
        bullet.setposition (x, y)
        bullet.showturtle()

#keyboard binds
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(shoot, "space")

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

#Main game loop
while True:

#Move the invader
    x=invader.xcor()
    x+= invader_speed
    invader.setx(x)
#Move the invader back down
    if invader.xcor() > 270:
        y = invader.ycor()
        y -= 40
        invader_speed *= -1
        invader.sety(y)
    if invader.xcor() < -270:
        y = invader.ycor()
        y -= 40
        invader_speed *= -1
        invader.sety(y)
#bullet
    y = bullet.ycor()
    y+= bullet_speed
    bullet.sety(y)
    #checks is bullet has gone up
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate="ready"

    #collision
    if abs(bullet.xcor()-invader.xcor())<15 and abs(bullet.ycor()-invader.ycor())<15:
        bullet.hideturtle()
        score_pen.clear()
        score = score+10
        score_pen.write("Score %s" %score)
        #invader.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,400) 
        #reset enemy
        invader.setposition(-200,250)
        
        #gameover stuff
    if abs(invader.xcor()-player.xcor())<15 and abs(invader.ycor()-player.ycor())<15:
        player.hideturtle()
        invader.hideturtle()
        print("GAME OVER")
        break
        




delay = input("Enter")