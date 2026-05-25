import turtle as t


STRETCH_WID = 5
STRETCH_LEN = 1

MOVE = 20

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
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.screen.update()


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.screen.update()

