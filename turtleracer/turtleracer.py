from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400) 

user_bet = screen.textinput(title = "Make your bet",
                            prompt = "Which turtle will win the race? Enter you colour: ")
colours = ["red", "green", "blue", "yellow", "purple", "orange"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle in range(len(colours)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colours[turtle])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[turtle])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_colour = turtle.pencolor()
            if wining_colour == user_bet:
                print(f"You win! The {wining_colour} turtle won")
            else:
                print(f"You lose! The {wining_colour} turtle won")
        rand_distance =random.randint(0,15)
        turtle.forward(rand_distance)


    
screen.exitonclick()
 