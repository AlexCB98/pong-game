import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

ball = Ball()
scoreboard = Scoreboard()

paddle_1 = Paddle((470,0))
screen.onkey(paddle_1.up, 'Up')
screen.onkey(paddle_1.down, 'Down')

paddle_2 = Paddle((-470,0))
screen.onkey(paddle_2.up, 'w')
screen.onkey(paddle_2.down, 's')

while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Collision with wall

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Collision with paddles

    if (
        ball.distance(paddle_1) < 50 and ball.xcor() > 440
        or ball.distance(paddle_2) < 50 and ball.xcor() < -440
    ):
        ball.bounce_x()

    # Ball go beyond the right paddle

    if ball.xcor() > 500:
        ball.reset_position()
        scoreboard.l_point()

    # Ball go beyond the left paddle

    if ball.xcor() < -500:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()