from tkinter import *

window = Tk()
window.geometry('220x180')
equa = ""
window.title('CALCULATOR')
equation = StringVar()
calculation = Label(window, textvariable=equation)
calculation.grid(columnspan=4)
equation.set('Enter Your Expression')

def exit_app():
    window.quit()
def clear_display():
    global equa
    equa = ""
    equation.set('')
def pressBtn(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
def calculate():
    global equa
    try:
        total = str(eval(equa))
        equation.set(total)
        equa=total
    except ZeroDivisionError:
        equation.set("Error")
        equa=" "
    except Exception as e:
        equation.set("Error")
        equa = ""

button0 = Button(window, text='0', command=lambda:pressBtn(0))
button0.grid(row=5, column=0)
button1 = Button(window, text='1', command=lambda:pressBtn(1))
button1.grid(row=4, column=0)
button2 = Button(window, text='2', command=lambda:pressBtn(2))
button2.grid(row=4, column=1)
button3 = Button(window, text='3', command=lambda:pressBtn(3))
button3.grid(row=4, column=2)
button4 = Button(window, text='4', command=lambda:pressBtn(4))
button4.grid(row=3, column=0)
button5 = Button(window, text='5', command=lambda:pressBtn(5))
button5.grid(row=3, column=1)
button6 = Button(window, text='6', command=lambda:pressBtn(6))
button6.grid(row=3, column=2)
button7 = Button(window, text='7', command=lambda:pressBtn(7))
button7.grid(row=2, column=0)
button8 = Button(window, text='8', command=lambda:pressBtn(8))
button8.grid(row=2, column=1)
button9 = Button(window, text='9', command=lambda:pressBtn(9))
button9.grid(row=2, column=2)
point = Button(window, text='.', command=lambda:pressBtn("."))
point.grid(row=5, column=1)
plush = Button(window, text='+', command=lambda:pressBtn('+'))
plush.grid(row=4, column=3)
minus = Button(window, text='-', command=lambda:pressBtn('-'))
minus.grid(row=3, column=3)
multi = Button(window, text='x', command=lambda:pressBtn('*'))
multi.grid(row=2, column=3)
divide = Button(window, text='/', command=lambda:pressBtn('/'))
divide.grid(row=5, column=3)
equal = Button(window, text='=', command=calculate)
equal.grid(row=5, column=2)
clear = Button(window, text='AC', command=clear_display)
clear.grid(row=1, column=0)
prct = Button(window, text='%', command=lambda:pressBtn('%'))
prct.grid(row=1, column=1)
exit = Button(window, text='EXIT', command=exit_app)
exit.grid(row=1, column=2)


window.mainloop()