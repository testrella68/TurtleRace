from turtle import *
from random import *
import turtle
import time

#SCREEN SETUP
setup(800, 500)
title("Turtle Race")
bgcolor("aqua")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("black")
write("Turtle Race", font=("Poppins", 20, "bold"))

#DIRT
goto(-350, 200)
pendown()
color("dimgrey")
begin_fill()
for i in range(2):
  forward(700)
  right(90)
  forward(400)
  right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

#BLACK SQUARES ROW 1
color("black")
for i in range(10):
  goto(250, (170 - (i * gap_size * 2)))
  stamp()

#BLACK SQUARES ROW 2
for i in range(10):
  goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
  stamp()

#YELLOW SQUARES ROW 1
color("gold")
for i in range(10):
  goto(250, (190 - (i * gap_size * 2)))
  stamp()

#YELLOW SQUARES ROW 2
for i in range(10):
  goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
  stamp()

#TURTLE 1 - RED
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(2)
red_turtle.penup()
red_turtle.goto(-300, 150)
red_turtle.pendown()

#TURTLE 2 - GREEN 
green_turtle = Turtle()
green_turtle.color("chartreuse")
green_turtle.shape("turtle")
green_turtle.shapesize(2)
green_turtle.penup()
green_turtle.goto(-300, 50)
green_turtle.pendown()

#TURTLE 3 = PURPLE 
purple_turtle = Turtle()
purple_turtle.color("darkviolet")
purple_turtle.shape("turtle")
purple_turtle.shapesize(2)
purple_turtle.penup()
purple_turtle.goto(-300, -50)
purple_turtle.pendown()

#TURTLE 4 - PINK
pink_turtle = Turtle()
pink_turtle.color("hotpink")
pink_turtle.shape("turtle")
pink_turtle.shapesize(2)
pink_turtle.penup()
pink_turtle.goto(-300, -150)
pink_turtle.pendown()

#PAUSE FOR 1 SECOND BEFORE RACING 
time.sleep(1)

#MOVE THE TURTLES
while red_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and purple_turtle.xcor() <= 230:
  red_turtle.forward(randint(1, 10))
  green_turtle.forward(randint(1, 10))
  pink_turtle.forward(randint(1, 10))
  purple_turtle.forward(randint(1, 10))

# CELEBRATE THE WINNER
# RED TURTLE WINS 
if red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > purple_turtle.xcor():
  print("Red Turtle Wins!")
  for i in range(72):
    red_turtle.right(5)
    red_turtle.shapesize(3.5)

# GREEN TURTLE WINS
elif green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > purple_turtle.xcor():
  print("Green Turtle Wins!")
  for i in range(72):
    green_turtle.right(5)
    green_turtle.shapesize(3.5)

# PURPLE TURTLE WINS
elif purple_turtle.xcor() > red_turtle.xcor() and purple_turtle.xcor() > green_turtle.xcor() and purple_turtle.xcor() > pink_turtle.xcor():
  print("Purple Turtle Wins!")
  for i in range(72):
    purple_turtle.right(5)
    purple_turtle.shapesize(3.5)

# PINK TURTLE WINS
else:
  print("Pink Turtle Wins!")
  for i in range(72):
    pink_turtle.right(5)
    pink_turtle.shapesize(3.5)