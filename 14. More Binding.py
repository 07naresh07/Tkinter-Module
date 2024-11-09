from tkinter import *

window = Tk()
def leftClick(event):
    print('Left')
def rightClick(event):
    print('Right')
def scroll(event):
    print("Scroll")
def leftKey(event):
    print('Left key pressed')
def rightKey(event):
    print('Right key pressed')
def upKey(event):
    print("Upward key pressed")
def downKey(event):
    print("Downward key pressed")
def charKey(event):
    print(f"Character {event.char} is pressed")

window.geometry('500x500')
window.bind("<Button-1>", leftClick)
window.bind("<Button-2>", rightClick)
window.bind("<Button-3>", scroll)
window.bind("<Left>", leftKey)
window.bind("<Right>", rightKey)
window.bind('<Up>', upKey)
window.bind('<Down>', downKey)
window.bind("<Key>", charKey)

window.mainloop()