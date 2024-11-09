from tkinter import *
window = Tk()
window.geometry('400x500')
label1 = Label(window, text='Name: ')
label1.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

check = Checkbutton(window, text='Remember Name')
check.grid(columnspan=2)    #Not necessary to define row as we already defined row=0 for label1 and next row will be default

window.mainloop()