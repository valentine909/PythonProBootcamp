from data import data
from question import Question
from quiz_brain import QuizBrain
from ui import Quizzler_UI


def make_question_bank():
    list_of_questions = []
    for dictionary in data:
        q = dictionary['text']
        a = dictionary['answer']
        question = Question(q, a)
        list_of_questions.append(question)
    return list_of_questions


if __name__ == '__main__':
    question_bank = make_question_bank()
    quiz = QuizBrain(question_bank)
    Quizzler_UI(quiz)
