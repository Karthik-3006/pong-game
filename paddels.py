from turtle import Turtle, Screen
class paddel(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)
    def up(self):
        if self.ycor() <= 240:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)
    def down(self):
        if self.ycor() >= -220:
            y_cor2 = self.ycor() - 20
            self.goto(self.xcor(), y_cor2)
    