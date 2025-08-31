from turtle import Turtle, Screen
import time
class creating_ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.new_x = 10
        self.new_y = 10
    def moving(self):
        self.goto(self.xcor()+self.new_x, self.ycor()+self.new_y)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.new_y *= -1
    def paddel_detect(self):
        self.new_x *= -1