from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=300)
canvas.pack()
def createRect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill='red')

createRect(10, 10, 100, 290)
createRect(100, 150, 250, 200)

window.mainloop()
