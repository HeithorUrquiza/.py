from turtle import Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((365, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.vel)
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 283 or ball.ycor() < -283:
        ball.bounce_y()
        
    #Detect collsion with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
    #Detect if R paddle misses
    if ball.xcor() > 400:
        scoreboard.increase_l_score()
        ball.reset_position()
        
    #Detect if L paddle misses
    if ball.xcor() < -400:
        scoreboard.increase_r_score()
        ball.reset_position()

    if scoreboard.r_score + scoreboard.l_score == 20:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()