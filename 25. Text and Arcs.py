from tkinter import *
from tkinter.font import Font

window = Tk()
fonts = Font(family='TImes', size=20, weight='normal', slant='italic')
canvas = Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_arc(10, 10, 100, 290, extent=359, style=ARC)  #Takes 360 as '0'
canvas.create_rectangle(10, 10, 100, 290)
canvas.create_arc(150, 150, 250, 280, extent=270, style=ARC)
#canvas.create_text(150, 150, text='HELLO NARESH!!', font=fonts, fill='Red')
canvas.create_text(150, 150, text='Hello Naresh', font=('Times', 30, 'italic', 'bold'), fill='Blue')
window.mainloop()