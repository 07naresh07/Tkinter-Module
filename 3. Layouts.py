from tkinter import *

window = Tk()
topFrame =Frame(window)
topFrame.pack() #Its okay if we don't define side=TOP as we defined side=BOTTOM and top is default one
botFrame = Frame(window)
botFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text = 'Click Me', fg='green')
button1.pack(side=LEFT)
button2 = Button(topFrame, text = 'Hello!!', fg='purple')
button2.pack(side=LEFT) #It places widget from left to right and when button1 is placed, next position is right of button1 as 1st position is already filled=Left to Right Concept
button3 = Button(botFrame, text = 'Naresh', fg='blue')
button3.pack(side=LEFT)
button4 = Button(botFrame, text = 'Uma', fg='yellow')
button4.pack(side=LEFT) 

window.mainloop()