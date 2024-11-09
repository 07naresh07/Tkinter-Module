from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width=300, height=300)
canvas.pack()
colors = ['green', 'blue', 'cyan', 'red', 'pink', 'brown', 'gray', 'yellow']

def randomRect(num):
    for i in range(0, num):
        x1 = random.randrange(140)
        y1 = random.randrange(140)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        color = random.choice(colors)  # Corrected to choose a random color
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

randomRect(150)
window.mainloop()
