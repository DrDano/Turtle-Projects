from turtle import Turtle, Screen

ted = Turtle()
screen = Screen()


def move_f():
    ted.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_f)

screen.exitonclick()
