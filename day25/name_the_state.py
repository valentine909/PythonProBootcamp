import pandas as pds
from turtle import Turtle, Screen
FILENAME = '50_states.csv'
FONT = ("Arial", 8, "bold")


def screen_init():
    screen = Screen()
    screen.bgpic('blank_states_img.gif')
    screen.setup(725, 491)
    screen.title('Name the States')
    return screen


if __name__ == '__main__':
    writer = Turtle(visible=False)
    writer.pu()
    scr = screen_init()
    correct_guesses = 0
    data = pds.read_csv(FILENAME)
    guessed_states = []
    while correct_guesses < 50:
        answer = scr.textinput(f"{correct_guesses}/50 States Correct", "What's another state's name?").capitalize()
        if answer == 'Exit':
            print(*[i for i in data.state if i not in guessed_states], sep='\n')
            break
        state = data[data.state == answer]
        if not state.empty and answer not in guessed_states:
            writer.goto(state.x.item(), state.y.item())
            writer.write(answer, font=FONT)
            correct_guesses += 1
            guessed_states.append(answer)
    writer.write('YOU WIN! Congrats!!!', font=FONT)
    scr.mainloop()
