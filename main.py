import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from field import Field
import time

screen = t.Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

ball = Ball()
scoreboard = Scoreboard()
field = Field()

paddle_1_up = False
paddle_1_down = False
paddle_2_up = False
paddle_2_down = False

paddle_1 = Paddle((470,0))

paddle_2 = Paddle((-470,0))

def paddle_1_go_up():
    global paddle_1_up
    paddle_1_up = True

def paddle_1_stop_up():
    global paddle_1_up
    paddle_1_up = False

def paddle_1_go_down():
    global paddle_1_down
    paddle_1_down = True

def paddle_1_stop_down():
    global paddle_1_down
    paddle_1_down = False

def paddle_2_go_up():
    global paddle_2_up
    paddle_2_up = True

def paddle_2_stop_up():
    global paddle_2_up
    paddle_2_up = False

def paddle_2_go_down():
    global paddle_2_down
    paddle_2_down = True

def paddle_2_stop_down():
    global paddle_2_down
    paddle_2_down = False

screen.onkeypress(paddle_1_go_up, 'Up')
screen.onkeyrelease(paddle_1_stop_up, 'Up')
screen.onkeypress(paddle_1_go_down, 'Down')
screen.onkeyrelease(paddle_1_stop_down, 'Down')

screen.onkeypress(paddle_2_go_up, 'w')
screen.onkeyrelease(paddle_2_stop_up, 'w')
screen.onkeypress(paddle_2_go_down, 's')
screen.onkeyrelease(paddle_2_stop_down, 's')

while True:
    time.sleep(ball.increase_speed)
    ball.move()

    if paddle_1_up:
        paddle_1.up()

    if paddle_1_down:
        paddle_1.down()

    if paddle_2_up:
        paddle_2.up()

    if paddle_2_down:
        paddle_2.down()

    screen.update()

    # Collision with wall

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Collision with paddles

    if ball.xcor() > 440 and ball.x_move > 0 and ball.ycor() < paddle_1.ycor() + 60 and ball.ycor() > paddle_1.ycor() - 60:
        ball.setx(440)
        ball.bounce_x()

    if ball.xcor() < -440 and ball.x_move < 0 and ball.ycor() < paddle_2.ycor() + 60 and ball.ycor() > paddle_2.ycor() - 60:
        ball.setx(-440)
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
