import turtle as t


STRETCH_WID = 5
STRETCH_LEN = 1
X_POS = 470
Y_POS = 0

class Paddle(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.speed('fastest')
        self.penup()
        self.goto(X_POS, Y_POS)