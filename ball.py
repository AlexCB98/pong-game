import turtle as t

STRETCH_WID = 1
STRETCH_LEN = 1

class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
