try:
    from day17_data_onlinedb import question_data
except Exception as e:
    from day17_data import question_data
from day17_question_model import Question
from day17_quiz_brain import QuizBrain

if __name__ == '__main__':
    question_bank = []
    for dictionary in question_data:
        q = dictionary['text']
        a = dictionary['answer']
        question = Question(q, a)
        question_bank.append(question)

    quiz = QuizBrain(question_bank)
    quiz.next_question()
    print(f'You\'ve completed the quiz.\nYour final score was: {quiz.score}/{len(question_bank)}.')
