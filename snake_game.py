import turtle
import time
import random

delay = 0.1
score = 0
hight_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# the width & height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# food in game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'yellow'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
        font=("candara", 24, "bold"))