import turtle
import math
import random
import winsound


# setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("HOMEINVADERS")
# BACKGROUND FILE HERE
wn.bgpic("rocket6.gif")
wn.tracer(0)

# register the shapes
wn.register_shape("rocket10.gif")
wn.register_shape("rocket11.gif")
wn.register_shape("rocket4.gif")
wn.register_shape("rocket6.gif")
wn.register_shape("rocket13.gif")
wn.register_shape("rocket14.gif")
wn.register_shape("rocket15.gif")
wn.register_shape("rocket16.gif")
wn.register_shape("rocket17.gif")
wn.register_shape("rocket12.gif")


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
enemies_killed = 0

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
player.shape("rocket10.gif")
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
number_of_enemies = 27
# create empty list of enemies
enemies = []
enemyLives = 1
enemyBonus = 1
# add enemies in list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:
    # HOMEINVADER color
    enemy.color("red")
    # HOMEINVADER shape 
    enemy.shape("rocket11.gif")
    enemy.penup()
    # HOMEINVADER speed (currently set at fastest)
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    #update teh invader #
    enemy_number += 1
    if enemy_number == 9:
        enemy_start_y -= 50
        enemy_number = 0
enemyspeed = 0.1

#ENEMY BULLET
ebullet = turtle.Turtle()
ebullet.color("red")
ebullet.shape("rocket12.gif")
ebullet.penup()
ebullet.speed(0)
ebullet.setheading(90)
#ebullet.hideturtle()

ebulletspeed = .9
ebulletstate = "ready"



# MUSKET BOI's MUCKET
bullet = turtle.Turtle()
bullet.color("red")
# bullet shape
bullet.shape("rocket4.gif") 
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# bullet speed
bulletspeed = 1.5

# Defines bullet state
# ready to fire

bulletstate = "ready"
# fire


# Move MUSKET BOI left and right
def move_left():
    player.speed = -.75

def move_right():
    player.speed = .75
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

# declares bulletstate as global when it needs to change
def fire_ebullet():
    # declares bulletstate as global when it needs to change
    global ebulletstate    
    if ebulletstate == "ready":
        ebulletstate = "fire"
    # move the bullet just above the player
        x = enemy.xcor()
        y = enemy.ycor()
        ebullet.setposition(x, y +15)
        ebullet.showturtle()




# Key bindings    
wn.listen()
wn.onkeypress(move_left, "Left")

wn.onkeypress(move_right, "Right")

wn.onkeypress(fire_bullet, "space")

#wn.onkeypress(fire_ebullet, "space")

#level up stuff
levelUp = 2700
AHHH = 0
AHHHH = 1

# Main game loop
while True:
    wn.update()
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
            winsound.PlaySound("sounds/explode.wav", winsound.SND_ASYNC)

            # reset the bullet
            #enemy.hideturtle()
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            enemyLives -= 1
            fire_ebullet()
            print(enemyBonus)
            if enemyLives == 0:
                enemy.setposition(0,420690)
                

                # update the score
                score += 100
                enemies_killed += 1
                scorestring = "Score: {}".format(score)
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                number_of_enemies = number_of_enemies -1
                enemyLives += enemyBonus



        if enemy.ycor() <= -200: 
            player.hideturtle()
            
            enemy.hideturtle()
            print("GAME OVER")
            break

        if number_of_enemies == 0:
            number_of_enemies = 27
            enemy.showturtle()
            for i in range(number_of_enemies-enemies_killed):
             enemies.append(turtle.Turtle())

            enemy_start_x = -225
            enemy_start_y = 250
            enemy_number = 0


            for enemy in enemies:
                # HOMEINVADER color
                enemy.color("red")
                # HOMEINVADER shape 
                enemy.shape("rocket11.gif")
                enemy.penup()
                # HOMEINVADER speed (currently set at fastest)
                enemy.speed(0)
                x = enemy_start_x + (50 * enemy_number)
                y = enemy_start_y
                enemy.setposition(x, y)
                #update teh invader #
                enemy_number += 1
                if enemy_number == 9:
                    enemy_start_y -= 50
                    enemy_number = 0
    if score == levelUp:
        levelUp = levelUp+2700
        bulletspeed += .003
        AHHH += 1
        wn.bgpic("rocket16.gif")
        if AHHH == AHHHH:
            AHHHH += 2
            enemyBonus += 1

        
        
                            




    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if ebulletstate == "fire":
        ey = ebullet.ycor()
        ey -= ebulletspeed
        ebullet.sety(ey)

    
    # check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if ebullet.ycor() < -275:
        ebullet.hideturtle()
        ebulletstate= "ready"

    


   
