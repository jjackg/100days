from turtle import Screen
from snake import Snake
from food import Food
from scoreboards import Scoreboards
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

scoreboards = Scoreboards()
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
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboards.add_score()
        snake.extend()

    ## Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboards.game_over() 

    ## Detect collsion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboards.game_over()


screen.exitonclick()