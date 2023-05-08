from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("Miles to Kilometers Converter")
#window.minsize(width=350, height=100)
window.config(padx=50, pady=50)


input = Entry(width=10)
input.insert(END, "0")
input.grid(column=1, row=0)

#labels
miles_label = Label(text="Miles",font=FONT)
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)
result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

#Button
def calculate():
    value_input = float(input.get())
    result_label.config(text=str(round(value_input * 1.609344, 1)))


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()