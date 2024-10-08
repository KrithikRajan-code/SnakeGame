from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

#moving snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.write_text()

# collision of food
    if snake.head.distance(food)<20:
        food.refresh()
        score.score += 1

        snake.extend()

#detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        score.again_reset()
        snake.snake_reset()
        food.refresh()


# detect collition with tail
    for segment in snake.segements[1:]:
        if snake.head.distance(segment) < 10:
            score.again_reset()
            snake.snake_reset()
            food.refresh()


screen.exitonclick()