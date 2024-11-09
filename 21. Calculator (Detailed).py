from tkinter import*
import tkinter.messagebox

window = Tk()
window.title('Calculator')
number=''
variable = StringVar()
display = Label(window, textvariable = variable)
display.grid(columnspan=4)
variable.set('Enter Your Expression: ')

def getNum(num):
    global number
    number = number+str(num)
    variable.set(number)
def clearDisplay():
    global number
    number=''
    variable.set('')

def rootCalc():
    try:
        global number
        import math
        sqrt = str(math.sqrt(float(number)))
        variable.set(sqrt)
        number = sqrt   #Sets number to sqrt value in calculator display i.e. if we have got 5 as root of 25, then the remaining on the screen will set to 5, not 0 or delete number
    except ValueError:
        variable.set('ERROR')
        number = ''
    except Exception as e:
        variable.set('ERROR')
        number=''

def exitDisp():
    window.quit()

def evaluate():
    try:
        global number
        total = str(eval(number))
        variable.set(total)
        number = total  #Sets number to sqrt value in calculator display i.e. if we got 5 as root of 25, then the remaining on the screen will set to 5, not 0 or delete number
    except ZeroDivisionError:
        variable.set('ERROR')
        number=''
    except Exception as e:
        variable.set('ERROR')
        number=''



AC = Button(window, text='AC', command=clearDisplay)
AC.grid(row=1, column=0)
sqrt = Button(window, text='√', command=rootCalc)
sqrt.grid(row=1, column=1)
percent = Button(window, text = '%', command=lambda:getNum('%'))
percent.grid(row=1, column=2)
div = Button(window, text = '÷', command=lambda:getNum('/'))
div.grid(row=1, column=3)

button7 = Button(window, text='7', command=lambda:getNum(7))
button7.grid(row=2, column=0)
button8 = Button(window, text = '8', command=lambda:getNum(8))
button8.grid(row=2, column=1)
button9 = Button(window, text='9', command=lambda:getNum(9))
button9.grid(row=2, column=2)
mult = Button(window, text='x', command=lambda:getNum('*'))
mult.grid(row=2, column=3)

button4 = Button(window, text='4', command=lambda:getNum(4))
button4.grid(row=3, column=0)
button5 = Button(window, text = '5', command=lambda:getNum(5))
button5.grid(row=3, column=1)
button6 = Button(window, text='6', command=lambda:getNum(6))
button6.grid(row=3, column=2)
min = Button(window, text='-', command=lambda:getNum('-'))
min.grid(row=3, column=3)

button1 = Button(window, text='1', command=lambda:getNum(1))
button1.grid(row=4, column=0)
button2 = Button(window, text = '2', command=lambda:getNum(2))
button2.grid(row=4, column=1)
button3 = Button(window, text='3', command=lambda:getNum(3))
button3.grid(row=4, column=2)
plus = Button(window, text='+', command=lambda:getNum('+'))
plus.grid(row=4, column=3)

button0 = Button(window, text='0', command=lambda:getNum(0))
button0.grid(row=5, column=0)
exit = Button(window, text = 'EXIT', command=exitDisp)
exit.grid(row=5, column=1)
point = Button(window, text='.', command=lambda:getNum('.'))
point.grid(row=5, column=2)
equal = Button(window, text='=', command=evaluate)
equal.grid(row=5, column=3)

window.mainloop()