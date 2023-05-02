from turtle import Screen 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((365, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    ball.move()
    
    if ball.ycor() > 290:
        ball.change_direction_top()


screen.exitonclick()
