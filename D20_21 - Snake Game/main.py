from turtle import Screen
# performs various time-related functions
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# turn turtle animation on/off an set delay for update drawings
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# move snake
game_is_on = True
while game_is_on:
    # perform a TurtleScreen update when tracer is turned off
    screen.update()
    # suspend execution of the calling thread for the given number of seconds
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail:
        # trigger game over sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    # this can be done with slicing instead
        # piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
        # print(piano_keys[2:5]) --> [start:stop:increment]
        # output --> ['c', 'd', 'e']


screen.exitonclick()
