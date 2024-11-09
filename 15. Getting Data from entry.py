from tkinter import *

def evaluate(event):
    data = entry.get()
    #result = abs(float(data))
    #label1.config(text='Answer: '+str(result), fg='Red)
    try:
        final = eval(data)
        label1.config(text='Answer: '+str(final), fg='Red', bg='gray')
    except:
        label1.config('Invalid entry. Please confirm the data!!')
window = Tk()
label = Label(window, text='Enter your Expression: ')
label.pack()
entry = Entry(window)
entry.pack()
entry.bind("<Return>", evaluate)
label1 = Label(window)
label1.pack()
window.mainloop()