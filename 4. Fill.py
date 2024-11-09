import tkinter as tk

window = tk.Tk()
window.geometry('500x400')
button1 = tk.Button(None, text = 'Click Me', fg='green', bg='cyan')
button1.pack(fill=tk.X)
button2 = tk.Button(None, text = 'Hello!!', fg='purple')
button2.pack(side=tk.RIGHT, fill=tk.Y) 
button3 = tk.Button(None, text = 'Naresh', fg='blue')
button3.pack(side=tk.LEFT)
button4 = tk.Button(None, text = 'Uma', fg='yellow')
button4.pack(side=tk.LEFT) 

window.mainloop()