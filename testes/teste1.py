import tkinter

window = tkinter.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text='I\'m a Label', font=('Arial', 24, 'bold'))
my_label.pack(side='left')


window.mainloop()