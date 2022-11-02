from turtle import Screen, Turtle
import random
import turtle as t
import numpy as np

timmy = Turtle()
timmy.shape("classic")
timmy.speed(0)
timmy.pensize(1)
t.colormode(255)


### Color generator ###
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple

### Draw Spirograph ###
def draw_spirograph(number_of_lines):
    delta = np.linspace(0 ,360, num = number_of_lines)
    for i in delta:
        timmy.setheading(i)
        timmy.color(random_color())
        timmy.circle(100)

draw_spirograph(500)

screen = Screen()
screen.exitonclick()


