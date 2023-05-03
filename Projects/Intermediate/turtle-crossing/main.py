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
cars = [CarManager()]

screen.listen()
screen.onkey(player.move, "Up")

count = 0
game_is_on = True
while game_is_on:
    count += 1
    screen.update()
    time.sleep(0.1)
    
    if count % 6 == 0:
        cars.append(CarManager())
    
    for car in cars:
        car.move()
        
        if player.distance(car) < 35:
            time.sleep(4)
        
        
    
    
    
    
    
