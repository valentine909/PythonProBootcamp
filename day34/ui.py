from tkinter import Tk, Canvas, Button, Label, E, PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Quizzler_UI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.root = Tk()
        self.root.title('Quizzler')
        self.root.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=300, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 150, text='Some text', font=('Arial', 14), width=270)

        self.label_score = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR, font=('Arial', 12, 'bold'))
        self.label_score.grid(row=0, column=1, pady=20, sticky=E)

        self.image_true = PhotoImage(file='images/true.png')
        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.check_true)
        self.button_true.grid(row=2, column=0, pady=20)

        self.image_false = PhotoImage(file='images/false.png')
        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.check_false)
        self.button_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.questions_remain():
            self.label_score.config(text=f'Score: {self.quiz.score}')
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text='No more questions remain')
            self.button_false.config(state='disabled')
            self.button_true.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.root.after(300, self.get_next_question)

    def check_true(self):
        return self.give_feedback(self.quiz.check_answer('true'))

    def check_false(self):
        return self.give_feedback(self.quiz.check_answer('false'))
