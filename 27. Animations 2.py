from tkinter import *
import time

window = Tk()

canvas = Canvas(window, width=300, height=300)
canvas.pack()

def createLine():
    lines = [
        canvas.create_line(20, 20, 40, 20),
        canvas.create_line(40, 20, 40, 10),
        canvas.create_line(40, 10, 50, 25),
        canvas.create_line(50, 25, 40, 35),
        canvas.create_line(40, 35, 40, 25),
        canvas.create_line(40, 25, 20, 25),
        canvas.create_line(20, 25, 20, 20)
    ]
    for line in lines:
        canvas.addtag_withtag('shape', line)
createLine()

def moveLine(event):
    for i in range(10):
        canvas.move('shape', 5, 0)
        window.update()
        time.sleep(0.05)
canvas.bind('<Button-1>', moveLine)
window.mainloop()
