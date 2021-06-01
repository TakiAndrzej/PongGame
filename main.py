from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard_l = Scoreboard((-100, 220))
scoreboard_r = Scoreboard((100, 220))

screen.listen()
screen.onkeypress(key='Up', fun=paddle1.go_up)
screen.onkeypress(key='Down', fun=paddle1.go_down)
screen.onkeypress(key='w', fun=paddle2.go_up)
screen.onkeypress(key='s', fun=paddle2.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_from_wall()

    # Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 330 or ball.distance(paddle2) < 50 and ball.xcor() < -330:
        ball.bounce_from_paddle()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_l.update_score()
        ball.move_speed = 0.1

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard_r.update_score()
        ball.move_speed = 0.1

screen.exitonclick()



