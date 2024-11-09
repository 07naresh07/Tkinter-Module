from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_rectangle((10, 10), (100, 290))
canvas.create_line((10,10), (100, 290))
canvas.create_line((100, 10), (10, 290))
canvas.create_polygon(10, 10, 100, 290, 100, 10, 10, 290)   #At least three points to generate polygon

window.mainloop()
