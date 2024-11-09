from tkinter import *

window = Tk()

#for updating result in entry section rather than creating new label
'''
def evaluate(event=None):
    data=entry.get()
    try:
        result=eval(data)
        entry.delete(0,END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, 'Enter valid expression')
'''
def evaluate(event=None):
    data = entry.get()
    try:
        result = eval(data)
        label1.config(text='Answer: '+str(result))
    except:
        label1.config(text='Please enter valid expression')
label = Label(window, text = 'Enter your expression down below')
label.grid(row=0, columnspan=2)
button = Button(window, text='Calculate', command=evaluate)
button.grid(row=1, column=0)
label1 = Label(window)
label1.grid(row=2, columnspan=2)
entry = Entry(window)
entry.grid(row=1, column=1)
entry.bind('<Return>', evaluate)


window.mainloop()
