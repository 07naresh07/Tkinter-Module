from tkinter import *
import time

window = Tk()
canvas = Canvas(window, height=300, width=300)
canvas.pack()

polygon_id1 = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='Blue')
polygon_id2 = canvas.create_polygon(100, 100, 150, 200, 250, 280, fill='red')
def move_data(event): 
    for i in range(0, 60):
        canvas.move(polygon_id1, 10, 0)
        window.update()
        time.sleep(0.1)
canvas.bind('<Button-2>', move_data)

window.mainloop()