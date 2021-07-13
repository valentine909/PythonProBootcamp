import tkinter


def calculate_mile():
    mile = float(input_.get())
    label_number['text'] = f"{mile * 1.609:.2f}"


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=120)
window.config(padx=10, pady=10)
window.option_add("*Font", "Arial 14 bold")


label_miles = tkinter.Label(text='Miles')
label_miles.grid(column=3, row=1)

label_km = tkinter.Label(text='Km')
label_km.grid(column=3, row=2)

label_equal = tkinter.Label(text='is equal to')
label_equal.grid(column=1, row=2)

label_number = tkinter.Label(text='0')
label_number.grid(column=2, row=2)

button = tkinter.Button(text='Calculate', command=calculate_mile)
button.grid(column=2, row=3)

input_ = tkinter.Entry(width=10, justify='center')
input_.insert(0, '1')
input_.grid(column=2, row=1)

window.mainloop()
