from turtle import Turtle, Screen
import random

ted = Turtle(shape='turtle')
lellow = Turtle(shape='turtle')
keen = Turtle(shape='turtle')
moo = Turtle(shape='turtle')
poringe = Turtle(shape='turtle')

ted.color('red')
lellow.color('yellow')
keen.color('green')
moo.color('blue')
poringe.color('orange')

turtles_list = (ted, lellow, keen, moo, poringe)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")

is_race_on = True
y_pos = 120
for t in turtles_list:
    t.penup()
    t.goto(x=-230, y=y_pos)
    y_pos -= 60

while is_race_on:
    for t in turtles_list:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"You've won! {t.pencolor()} finished first!")
            else:
                print(f"You've lost. {t.pencolor()} won.")

        rand_dis = random.randint(0, 10)
        t.forward(rand_dis)



screen.exitonclick()
