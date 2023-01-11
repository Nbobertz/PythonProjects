from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("SnakeGame")
##: Create the snake screen, 600 by 600 square window.
# my snake game is title

##: below is creating 3 objects and placing them in the center of the screen linked together.
screen.tracer(0)

##: Below is a while loop and function that will move the snakeforward. It will allow us to move the snake left or
# right with either 'a' or 'd'
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


#import latest highscore

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        print("Tasty!")
        snake.add()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # if head collides with any other part of body then the turn is over
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
print('game is over')

screen.exitonclick()
