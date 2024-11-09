from tkinter import *
import tkinter.messagebox
window = Tk()
result = tkinter.messagebox.showinfo("Warning", "File contains viruses. Are you sure you want to proceed?")
answer = tkinter.messagebox.askquestion("Question", "Are you over 18 years of age?")
if answer=="yes":
    tkinter.messagebox.showinfo("Congrats", 'You are loggedin successfully')
if answer=='no':
    tkinter.messagebox.showinfo("Suspicious",'Please verify the age')

window.mainloop()