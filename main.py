import turtle as t
from paddle import Paddle


screen = t.Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

paddle_1 = Paddle((470,0))
screen.onkey(paddle_1.up, 'Up')
screen.onkey(paddle_1.down, 'Down')

paddle_2 = Paddle((-470,0))
screen.onkey(paddle_2.up, 'w')
screen.onkey(paddle_2.down, 's')



screen.update()
screen.exitonclick()