from turtle import Turtle, Screen

ted = Turtle(shape='turtle')
lellow = Turtle(shape='turtle')
keen = Turtle(shape='turtle')
moo = Turtle(shape='turtle')
poringe = Turtle(shape='turtle')

turtles_list = (ted, lellow, keen, moo, poringe)

ted.color('red')
lellow.color('yellow')
keen.color('green')
moo.color('blue')
poringe.color('orange')

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")

y_pos = 120
for t in turtles_list:
    t.penup()
    t.goto(x=-230, y=y_pos)
    y_pos -= 60



screen.exitonclick()
