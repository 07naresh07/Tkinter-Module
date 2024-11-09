from tkinter import *

def clickMe():
    entry1.delete(0, END)   #deletes any existing data
    entry1.insert(0, "naresh@1995") #Inserts the new text in entry1, 0 for the position of text
def help():
    entry2.delete(0, END)
    entry2.insert(0, "Krishn@1176")
window = Tk()
label = Label(window, text = 'Python GUI with Tkinter Module')
label.grid(row=0, columnspan=2)
button1 = Button(window, text = 'Username', fg='red', command=clickMe)
button1.grid(row=1, column=0)
entry1 = Entry(window)
entry1.grid(row=1, column=1)
button2 = Button(window, text='Password', fg='red', command=help)
button2.grid(row=2, column=0)
entry2 = Entry(window)
entry2.grid(row=2, column=1)



window.mainloop()