import turtle
import math
import random


# setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("HOMEINVADERS")
# BACKGROUND FILE HERE
wn.bgpic("images/rocket6.gif")

# register the shapes
wn.register_shape("images/rocket10.gif")
wn.register_shape("images/rocket11.gif")
wn.register_shape("images/rocket4.gif")
wn.register_shape("images/rocket6.gif")

# border stuff
border_pen = turtle.Turtle()
border_pen.speed(0)
# Border color
border_pen.color("white")
border_pen.penup()
# starts at bottom left
border_pen.setposition(-300,-300)
border_pen.pendown()
# inner border size
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# set score at 0
score= 0
lives = 2

# draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
# Sets font and font size
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Create MUSKET BOI
player = turtle.Turtle()
# changes color of MUSKET BOI
player.color("green")
#changes player thickness of MUSKETBOI
player.shape("images/rocket10.gif")
# MUSKET BOI STARTING POSITION
player.penup()
player.speed(0)
# starting position of MUSKET BOI
player.setposition(0, -250)
# angle of MUSKET BOI
player.setheading(90)
# MUSKET SPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED 
player.speed = 0

# choose a # of enemies
number_of_enemies = 5
# create empty list of enemies
enemies = []

# add enemies in list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # HOMEINVADER color
    enemy.color("red")
    # HOMEINVADER shape 
    enemy.shape("images/rocket11.gif")
    enemy.penup()
    # HOMEINVADER speed (currently set at fastest)
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    
enemyspeed = 10


# MUSKET BOI's MUCKET
bullet = turtle.Turtle()
bullet.color("red")
# bullet shape
bullet.shape("images/rocket4.gif") 
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# bullet speed
bulletspeed = 20

# Defines bullet state
# ready to fire
bulletstate = "ready"
# fire


# Move MUSKET BOI left and right
def move_left():
    player.speed = -15

def move_right():
    player.speed = 15
    x = player.xcor()
    x += player.speed
    player.setx(x)

def move_player():
    x = player.xcor()
    x += player.speed
    # Boundries
    if x < -280:
        x = - 280
    player.setx(x)
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # declares bulletstate as global when it needs to change
    global bulletstate    
    if bulletstate == "ready":
        bulletstate = "fire"
    # move the bullet just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y +15)
        bullet.showturtle()



# Key bindings    
wn.listen()
wn.onkeypress(move_left, "Left")

wn.onkeypress(move_right, "Right")

wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:

    move_player()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back down
        if enemy.xcor() > 280:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # change enemy direction
            enemyspeed *= -1
        
        if enemy.xcor() < -280:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # change enemy direction
            enemyspeed *= -1
    

        # check for collision between bullet and enemy
        if abs(bullet.xcor()-enemy.xcor())<20 and abs(bullet.ycor()-enemy.ycor())<20:
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # update the score
            score += 100
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        y = enemy.ycor            

        if enemy.ycor() <= -200: 
            player.hideturtle()
            
            enemy.hideturtle()
            print("GAME OVER")
            break

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    # check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    


   