from turtle import Turtle, Screen, textinput
from paddels import paddel
from ball import creating_ball
import random
import time
screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("chocolate")
screen.tracer(0)
player1 = 0
player2 = 0
chances = 0
input1 = textinput("Input", "Enter player1 name: ")
input2 = textinput("Input", "Enter player2 name: ")
r_x = random.randint(-100, 0)
def write(text, x, y):
    text.hideturtle()
    text.color("white")
    text.penup()
    text.goto(x, y)
text1 = Turtle()
text2 = Turtle()
text3 = Turtle()
write(text1, -250, 200)
write(text2, 200, 200)
write(text3, -50, -50)
left_paddel = paddel((-350, 0))
right_paddel = paddel((350, 0))
screen.listen()
screen.onkey(key="w", fun=left_paddel.up)
screen.onkey(key="s", fun=left_paddel.down)
screen.onkey(key="Up", fun=right_paddel.up)
screen.onkey(key="Down", fun=right_paddel.down)
ball = creating_ball()
text1.write(f"{input1} = {player1}", font=("Arial", 18, "bold"))
text2.write(f"{input2} = {player2}", font=("Arial", 18, "bold"))
condition = True
while condition:
    time.sleep(0.1)
    screen.update()
    ball.moving()
    if right_paddel.distance(ball) < 50 and ball.xcor() >= 330:
        ball.paddel_detect()
        player2 += 1
        text2.clear()
        text2.write(f"{input2} = {player2}", font=("Arial", 18, "bold"))
    elif left_paddel.distance(ball) < 50 and ball.xcor() <= -330:
        ball.paddel_detect()
        player1 += 1
        text1.clear()
        text1.write(f"{input1} = {player1}", font=("Arial", 18, "bold"))
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        chances += 1
        ball.goto(r_x, 0)
    
    if chances >= 3:
        if player1 > player2:
            text3.write(f"Game Over! {input1} wons", font=("Arial", 18, "bold"))
        elif player2 > player1:
            text3.write(f"Game Over! {input2} wons", font=("Arial", 18, "bold"))
        else:
            text3.write(f"Draw Match", font=("Arial", 18, "bold"))
        condition = False
screen.exitonclick()