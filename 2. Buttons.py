from tkinter import *

window = Tk()
label = Label(window, text="Hello World", fg='Blue')    #fg for color of th text
label.pack()
button = Button(window, text='Click Me', fg='red')
button.pack()
window.mainloop()