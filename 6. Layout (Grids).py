from tkinter import *
window = Tk()
label1 = Label(window, text='Label 1')
label1.grid(row=0, column=0)
label2 = Label(window, text='Label 2')
label2.grid(row=1, column=0)
label3 = Label(window, text='Label 3')
label3.grid(row=0, column=1)
label4 = Label(window, text='Label 4')
label4.grid(row=2, column=2)

window.mainloop()