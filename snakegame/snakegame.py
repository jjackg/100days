from hashlib import new
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ## Detect food being eaten ##
    if sn




        
 

screen.exitonclick()