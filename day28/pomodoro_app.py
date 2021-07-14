from tkinter import *
import time
from collections import namedtuple
from pushbullet_message import pushbullet_message
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

global timer
current_cycle = 0
mark = ''

# ------------------------ POMODORO PROGRAM CONFIG --------------------------- #
Cycle = namedtuple('Cycle', ['name', 'duration', 'color'])
c1 = Cycle('Work', WORK_MIN, GREEN)
c2 = Cycle('Rest', SHORT_BREAK_MIN, PINK)
c3 = Cycle('Big Rest', LONG_BREAK_MIN, RED)
program = [c1, c2] * 3 + [c1, c3]
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global current_cycle, mark
    try:
        window.after_cancel(timer)
    except NameError:
        pass
    canvas.itemconfig(timer_text, text=f'{WORK_MIN:02d}:00')
    label_timer.config(text='Timer', fg=GREEN)
    mark = ''
    label_progress.config(text=mark)
    current_cycle = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    cycle = program[current_cycle]
    pushbullet_message(f'{cycle.name} for {cycle.duration} min', f"Current time: {time.strftime('%H:%M:%S')}")
    label_timer.config(text=cycle.name, fg=cycle.color)
    count_down(cycle.duration * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(secs):
    canvas.itemconfig(timer_text, text=f'{secs // 60:02d}:{secs % 60:02d}')
    global timer, mark, current_cycle
    if secs:
        timer = window.after(1000, count_down, secs - 1)
    else:
        if program[current_cycle].name == 'Work':
            mark += '\u2713'
            label_progress.config(text=mark)
        raise_above_all()
        if current_cycle < len(program):
            current_cycle += 1
            start_timer()
        else:
            pushbullet_message(f'Full cycle finished', "Congrats!!")


def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=222, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f'{WORK_MIN:02d}:00', fill='black', font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=2, column=2)

label_config = {'fg': GREEN,
                'bg': YELLOW,
                'font': (FONT_NAME, 32, 'bold'),
                }

label_timer = Label(text='Timer', cnf=label_config)
label_timer.grid(row=1, column=2)

label_progress = Label(text=mark, cnf=label_config)
label_progress.grid(row=4, column=2)

button_start = Button(text='Start', highlightthickness=0, command=start_timer)
button_start.grid(row=3, column=1)

button_reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
button_reset.grid(row=3, column=3)

window.mainloop()
