import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    if player.finish_line():
        scoreboard.update_score()
        cars.increase_speed()
        
    cars.create_car()
    cars.move()
   
    for car in cars.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
                     
screen.exitonclick()