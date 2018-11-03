#SPACE INVADERS
#SETUP THE SCREEN

import turtle
import math
import random
#Setting up the screen
import os

ms = turtle.Screen()
ms.bgcolor("black")
ms.title("Space Invaders")
ms.bgpic("space_invaders_background.gif")

#register the shapes
turtle.register_shape("trump.gif")
turtle.register_shape("jungun.gif")
turtle.register_shape("nuke.gif")

#Draw Border
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

#set the score to zero
score = 0

#draw the scpre
score_pen= turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

#create the turtle player
player = turtle.Turtle()
player.color("blue")
player.shape("jungun.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed =15
'''
#create the speed turtle enemy
speed_enemy = turtle.Turtle()
speed_enemy.color("Orange")
speed_enemy.penup()
speed_enemy.speed(0)
x = random.randint(-200,200)
y = random.randint(100,250)
speed_enemy.setposition(x,y)
'''
#choose the number of enemies
num_of_enemies = 5
#create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(num_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("trump.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Create the players weapen
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("nuke.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire- bullet fired
bulletstate = "ready"

#moving the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs to change
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay laser.wav&")
        bulletstate = "fire"
        #move the bullet right above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True

#creating keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



#main game loop
while True:

    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #moving the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        # check if the collision has happened
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score+= 10
            scorestring = "Score %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print "GAME OVER"
            break

     #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

turtle.mainloop()

delay = raw_input("PRESS ENTER TO FINISH...")