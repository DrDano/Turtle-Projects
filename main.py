
from turtle import Turtle, Screen

big_john_turtle = Turtle()
big_john_turtle.shape("turtle")
big_john_turtle.color("AntiqueWhite")
big_john_turtle.pencolor("black")

for _ in range(0, 25):
    big_john_turtle.pendown()
    big_john_turtle.forward(5)
    big_john_turtle.penup()
    big_john_turtle.forward(5)



screen = Screen()
screen.exitonclick()
