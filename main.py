from tkinter import *

window = Tk()

window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=1)

mile_input = Entry(width=20)
mile_input.grid(column=1, row=1)

is_equal_text = Label(text="Is equal to")
is_equal_text.grid(column=0,row=2)

km_value_text = Label(text="0")
km_value_text.grid(column=1,row=2)

km_text = Label(text="Km")
km_text.grid(column=2,row=2)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=3)

window.mainloop()