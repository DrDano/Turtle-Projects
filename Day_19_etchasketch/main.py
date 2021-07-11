from turtle import Turtle, Screen

ted = Turtle()
screen = Screen()


def mf():
    ted.forward(20)


def mb():
    ted.back(20)


def tr():
    ted.right(10)


def tl():
    ted.left(10)


def clear_screen():
    ted.clear()
    ted.penup()
    ted.home()
    ted.pendown()


screen.listen()
screen.onkey(key='w', fun=mf)
screen.onkeyrelease(fun=mf, key='w')
screen.onkey(key='s', fun=mb)
screen.onkey(key='d', fun=tr)
screen.onkey(key='a', fun=tl)
screen.onkey(key='c', fun=clear_screen)


screen.exitonclick()
