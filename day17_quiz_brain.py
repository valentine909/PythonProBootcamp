class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        while self.question_number < len(self.question_list):
            question = self.question_list[self.question_number]
            answer = input(f'Q.{self.question_number + 1}: {question.question} (True/False)?: ')
            if answer == question.answer:
                self.score += 1
                print('You got it right!')
            else:
                print('That\'s wrong!')
            print(f'The correct answer was: {question.answer}.\n'
                  f'Your current score is {self.score}/{self.question_number + 1}.\n')
            self.question_number += 1
            self.next_question()
