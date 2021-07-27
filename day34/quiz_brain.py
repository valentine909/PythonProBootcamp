class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.question = None
        self.answer = None

    def next_question(self):
        self.question_number += 1
        record = self.question_list.pop()
        self.question = record.question
        self.answer = record.answer
        return f"Q{self.question_number}. {self.question}"

    def questions_remain(self):
        return len(self.question_list)

    def check_answer(self, answer):
        if answer == self.answer.lower():
            self.score += 1
            return True
        else:
            return False



