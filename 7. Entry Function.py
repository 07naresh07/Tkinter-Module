from tkinter import *
window = Tk()
window.geometry('400x500')
label1 = Label(window, text='Name: ')
label1.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

entry2 = Entry(window)
label2 = Label(window, text='Email: ')
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

window.mainloop()