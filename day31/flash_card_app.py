from tkinter import *
import os
import pandas as pds
BG_COLOR = "#B1DDC6"
CARD_BACK = '#91C2AF'
WIDTH = 1024
HEIGHT = 768
DATABASE = './data/vocabulary_5001-6000.csv'


class Cards_Game:
    def __init__(self, root):
        self.root = root
        self.df = None
        self.init_df()
        self.row = None
        self.words_to_learn = False
        self.flip_timer = None

        self.card_back = PhotoImage(file='images/card_back.png')
        self.card_front = PhotoImage(file='images/card_front.png')
        self.right_button = PhotoImage(file='images/right.png')
        self.wrong_button = PhotoImage(file='images/wrong.png')

        self.canvas = Canvas(width=WIDTH, height=HEIGHT)
        self.canvas.config(bg=BG_COLOR)
        self.card = self.canvas.create_image(WIDTH // 2, HEIGHT // 2, image=self.card_front)
        self.canvas.place(x=0, y=0)

        self.button_right = Button(image=self.right_button, highlightthickness=0, command=self.right)
        self.button_right.place(x=650, y=650)

        self.button_wrong = Button(image=self.wrong_button, highlightthickness=0, command=self.wrong)
        self.button_wrong.place(x=250, y=650)

        self.label_lang = Label(text='English', font=('Arial', 40, 'italic'), bg='white')
        self.label_lang.place(x=410, y=220)

        self.label_word = Label(text='some word', font=('Arial', 50, 'bold'), bg='white')
        self.label_word.place(x=500, y=380, anchor="center")

        self.card_init()

    def init_df(self):
        try:
            self.df = pds.read_csv('./data/words_to_learn.csv')
            self.words_to_learn = True
        except FileNotFoundError:
            self.df = pds.read_csv(DATABASE)

    def get_word(self):
        if len(self.df) == 0:
            self.words_to_learn = False
            try:
                os.remove('./data/words_to_learn.csv')
            except FileNotFoundError:
                pass
            self.init_df()
        return self.df.sample(n=1)

    def card_init(self):
        self.row = self.get_word()
        self.canvas.itemconfig(self.card, image=self.card_front)
        self.label_word.config(text=self.row.English.item(), fg='black', bg='white')
        self.label_lang.config(text='English', fg='black', bg='white')
        self.flip_timer = self.root.after(3000, self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.card, image=self.card_back)
        self.label_word.config(text=self.row.Russian.item(), fg='white', bg=CARD_BACK)
        self.label_lang.config(text='Russian', fg='white', bg=CARD_BACK)

    def right(self):
        self.root.after_cancel(self.flip_timer)
        self.df = self.df.drop(self.row.index)
        self.card_init()

    def wrong(self):
        self.root.after_cancel(self.flip_timer)
        if self.words_to_learn:
            self.row.to_csv('./data/words_to_learn.csv', mode='a', index=False, encoding='utf-8', header=False)
        else:
            self.row.to_csv('./data/words_to_learn.csv', mode='a', index=False, encoding='utf-8')
            self.words_to_learn = True
        self.card_init()
# ---------------------------- Root SETUP ------------------------------- #


window = Tk()
window.title('Flash card game')
window.geometry(f'{WIDTH}x{HEIGHT}')
window.resizable(False, False)


# ---------------------------- MAIN PROCEDURE ------------------------------- #

Cards_Game(window)
window.mainloop()
