from tkinter import *
from tkinter.font import Font

window = Tk()
window.geometry('400x500')
font_family = Font(family='Times New Roman', size=10, weight='bold', slant='italic')

label = Label(window, text='Please enter followinf information', fg='Red')
label.grid(row=0, columnspan=2)

label1 =  Label(window, text='Username', fg='gray', font=font_family)
label1.grid(row=1, column=0)
label2 = Label(window, text='Password', fg='cyan', font=font_family)
label2.grid(row=2, column=0)
entry1 = Entry(window)
entry1.grid(row=1, column=1)
entry2 = Entry(window)
entry2.grid(row=2, column=1)
checkButton = Checkbutton(window, text = 'Remember Password')
checkButton.grid(row=3, columnspan=2)

window.mainloop()