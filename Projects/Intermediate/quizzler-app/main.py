from entities.question_model import Question
from data.data import QuisData
from entities.quiz_brain import QuizBrain
from entities.ui import QuizInterface

data = QuisData()
question_bank = []
for question in data.get_data():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)