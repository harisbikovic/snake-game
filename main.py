from turtle import Screen
import time
from snake import Snake
from food import  Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # 0 means now we keep care of
# when to update the screen (manually)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    scoreboard.update(scoreboard.score)
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # Collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Collision with the tail
    for turtle in snake.turtles_list[1:]:
        if snake.head.distance(turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()