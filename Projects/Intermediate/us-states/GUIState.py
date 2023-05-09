from turtle import Screen, Turtle

IMAGE = 'Projects/Intermediate/us-states/blank_states_img.gif'

class GUIState:
    
    def __init__(self):
        self.screen = Screen()
        self.screen.title('U.S. States Game')
        self.screen.addshape(IMAGE)
        self.screen.setup(736, 498)
        self.turtle = Turtle(IMAGE)
        
    
    def user_input(self, *args):
        return self.screen.textinput(f'{len(args[0])}/50 States Correct', 'What\'s anothe state name?').title()