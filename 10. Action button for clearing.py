from tkinter import *

window = Tk()

def clearMe():
    entry.delete(0, END)    #Deleting text from 0 to end..we cn also use (3, 5) or any number

button = Button(window, text = 'Clear Me', fg = 'Red', command=clearMe)
button.pack()
entry= Entry(window)
entry.pack()

window.mainloop()