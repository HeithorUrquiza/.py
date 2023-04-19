class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list):
            
    
    def next_question(self):
        current_quenstion = self.question_list[self.question_number].text
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_quenstion} (True/False)?: ")
    