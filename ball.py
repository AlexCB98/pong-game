import turtle as t

STRETCH_WID = 1
STRETCH_LEN = 1
MOVE = 10

class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.penup()
        self.x_move = MOVE
        self.y_move = MOVE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()