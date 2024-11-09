from tkinter import *
import tkinter.messagebox
window = Tk()
result = tkinter.messagebox.askyesno("Warning", "File contains viruses. Are you sure you want to proceed?")
if result:
    print("User chose to proceed")
else:
    print("User chose not to proceed")