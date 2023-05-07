from turtle import Screen, Turtle
from writer import Writer
import pandas

IMAGE = 'Projects/Intermediate/us-states/blank_states_img.gif'

screen = Screen()
screen.title('U.S. States Game')
screen.addshape(IMAGE)
screen.setup(736, 498)
turtle = Turtle(IMAGE)
writer = Writer()

data = pandas.read_csv('Projects/Intermediate/us-states/50_states.csv')
states = data['state'].to_list()
correct_answers = []

while len(correct_answers) < 50:
    user_answer = screen.textinput(f'{len(correct_answers)}/50 States Correct', 'What\'s anothe state name?').title()

    if user_answer == 'Exit':
        to_learn = [state for state in states if state not in correct_answers]
        df = pandas.DataFrame(to_learn)
        df.to_csv('Projects/Intermediate/us-states/states_to_learn.csv')
        break
    
    if user_answer in states:
        coordinate = data[data.state == user_answer]
        x = coordinate.iloc[0, 1]
        y = coordinate.iloc[0, 2]
        writer.write_name(x, y, user_answer)
        correct_answers.append(user_answer)