from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
DATABASE = 'db_passwords.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    field_password.delete(0, END)
    password = generate_password()
    field_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    record = [field_website.get(), field_email.get(), field_password.get()]
    if all(record):
        with open(DATABASE, 'a') as file:
            file.write(';'.join(record) + '\n')
        field_password.delete(0, END)
        field_website.delete(0, END)
        messagebox.showinfo('', 'Password was saved')
    else:
        messagebox.showerror('Data missing', 'Provide all required data')
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    website = field_website.get()
    try:
        with open(DATABASE) as db:
            for record in db.readlines():
                web, em, pas = record.split(';')
                if web == website:
                    messagebox.showinfo(website, f'Email: {em}\nPassword: {pas}')
                    return
            messagebox.showinfo(website, f'No saved password found for {website}')
    except FileNotFoundError:
        messagebox.showinfo(website, f'No saved password found for {website}')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=2)

label_website = Label(text='Website:')
label_website.grid(row=2, column=1)

label_email = Label(text='Email/Username:', padx=20)
label_email.grid(row=3, column=1)

label_password = Label(text='Password:')
label_password.grid(row=4, column=1)

field_website = Entry(width=30)
field_website.grid(row=2, column=2, sticky=W)
field_website.focus()

field_email = Entry(width=56)
field_email.grid(row=3, column=2, columnspan=2, sticky=W)
field_email.insert(0, 'my_mail@gmail.com')

field_password = Entry(width=30)
field_password.grid(row=4, column=2, sticky=W)

button_search = Button(text='Search', command=search_password, width=16)
button_search.grid(row=2, column=3, sticky=E)

button_generate = Button(text='Generate Password', command=random_password, width=16)
button_generate.grid(row=4, column=3, sticky=E)

button_generate = Button(text='Add', command=save_password, width=47)
button_generate.grid(row=5, column=2, columnspan=2, sticky=W)

window.mainloop()
