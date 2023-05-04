from turtle import Turtle

ALIGN = "center"
FONT = ("Lexend", 14, "bold")
PATH = "Projects\Intermediate\snake-game\data.txt"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.check_high_score()
        self.hideturtle()
        self.goto(0.0, 268)
        self.speed("fastest")
        self.color("white")
        self.write_score()
        
        
    def increase(self):
        self.score += 1
        self.write_score()
        
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", False, ALIGN, FONT)
        
        
    def check_high_score(self):
        with open(PATH, mode='r') as file:
            value = file.read()
            return int(value)
        
        
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open(PATH, mode="w") as file:
                file.write(str(self.high_score))    
        self.score = 0
        self.write_score()
        
    """ def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, ALIGN, FONT) """