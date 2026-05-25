import turtle as t
from paddle import Paddle


screen = t.Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


paddle_1 = Paddle()


screen.update()
screen.exitonclick()