import turtle as t
import random 

screen = t.Screen()
screen.setup(width=700, height=600)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

local = -80
for color in colors:
    new_trutle = t.Turtle(shape="turtle")
    new_trutle.penup()
    new_trutle.color(color)
    new_trutle.goto(-330, local)
    turtles.append(new_trutle)
    local += 40

if user_bet:
    is_game_on = True
    
while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 330:
            is_game_on = False
            
            if turtle.pencolor() == user_bet.lower():
                print(f"You've got it. The {turtle.pencolor()} was the winner") 
            else:
                print(f"You were wrong. The {turtle.pencolor()} was the winner")
        
        turtle.forward(random.randint(0, 10))

screen.exitonclick()