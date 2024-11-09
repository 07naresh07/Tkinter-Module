from tkinter import *
import tkinter.messagebox
window = Tk()
result = tkinter.messagebox.showinfo("Warning", "File contains viruses. Are you sure you want to proceed?")
#In above code, 'Warning' is the title of error or message box and do not display on executation
window.mainloop()