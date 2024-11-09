import tkinter as tk

def display(event):
    print(f"Key Pressed: {event.char}")
window = tk.Tk()

window.bind("<Key>", display)

window.mainloop()