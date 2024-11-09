from tkinter import *

window = Tk()
def printName():
    print("Hello there Naresh Singh Dhami")
button = Button(window, text = 'Click Me', command=printName)
button.pack()

window.mainloop()