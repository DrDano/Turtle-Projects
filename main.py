
from turtle import Turtle, Screen
import random

screen = Screen()

big_john_turtle = Turtle()
big_john_turtle.shape("turtle")
big_john_turtle.color("AntiqueWhite")
big_john_turtle.pensize(1)
big_john_turtle.speed(20)
Screen().colormode(cmode=255)

heading = 2


for _ in range(0, 90):
    r = random.randint(100, 255)
    g = random.randint(100, 200)
    b = random.randint(100, 200)
    big_john_turtle.pencolor(r, g, b)
    big_john_turtle.setheading(heading)
    heading += 4
    big_john_turtle.circle(100)

screen.exitonclick()
