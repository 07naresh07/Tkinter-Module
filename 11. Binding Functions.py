from tkinter import *

window = Tk()
def printName(event):
    print('Hello there Naresh')

button1 = Button(window, text = 'Click Me')
button1.bind("<Button-1>", printName)   #"<Button-2>" for right click and "<Button-3>" for scroll mouse button
button1.pack()

window.mainloop()