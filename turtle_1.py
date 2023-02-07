import turtle
bullet_speed = 5
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
player = turtle.Turtle()
player.shape("images/rocket2.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)

#bullet
bullet=turtle.Turtle()
bullet.color("lightblue")
bullet.shape("triangle")
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

#invader turtle
invader=turtle.Turtle()
invader.shape("images/rocket3.gif")


#keyboard binds
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(shoot, "space")

while True:
    bullet.forward(bullet_speed)

delay = input("Enter")