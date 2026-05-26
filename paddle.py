import turtle as t


STRETCH_WID = 5
STRETCH_LEN = 1

MOVE = 20
MAX_Y = 330
MIN_Y = -330

class Paddle(t.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.speed('fastest')
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < MAX_Y:
            new_y = self.ycor() + MOVE
            self.goto(self.xcor(), new_y)


    def down(self):
        if self.ycor() > MIN_Y:
            new_y = self.ycor() - MOVE
            self.goto(self.xcor(), new_y)
