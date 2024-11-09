from tkinter import *

window = Tk()
window.geometry('400x400')
label = Label(window, text='Hover over me!!')
label.pack()
def onMe(event):
    label.config(text='Mouse is over me!')
def offMe(event):
    label.config(text='Mouse left me!')
label.bind("<Enter>", onMe)
label.bind('<Leave>', offMe)

window.mainloop()