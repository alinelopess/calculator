from tkinter import *


def clear():
    txtDisplay.delete(0, END)
    return


# Parent Window.
root = Tk()
root.title('Calculator')
root.geometry('350x450')

# Main entry.
num1 = StringVar()
txtDisplay = Entry(root, textvariable=num1, relief=RIDGE, bd=10, width=33, insertwidth=1, font=40)
txtDisplay.place(x=15, y=10)
txtDisplay.focus()


def update_entry(v):
    current_value = num1.get()
    num1.set(current_value + v)


def equalOper():
    current_num = num1.get()
    support_oper = ['+', '-', 'x', '÷']
    result = ""
    for oper in support_oper:
        if oper in current_num:
            nums = current_num.split(oper)
            if oper == '+':
                result = str(float(nums[0]) + float(nums[1]))
            if oper == '-':
                result = str(float(nums[0]) - float(nums[1]))
            if oper == 'x':
                result = str(float(nums[0]) * float(nums[1]))
            if oper == '÷':
                result = str(float(nums[0]) / float(nums[1]))

    num1.set(result)


# Buttons:
zeroButton = Button(root, text='0', width=20, height=3, bg='LightGreen', fg='brown',
                    command=lambda: update_entry('0')).place(x=17, y=382)
oneButton = Button(root, text='1', width=8, height=3, bg='LightGreen', fg='brown',
                   command=lambda: update_entry('1')).place(x=17, y=302)
twoButton = Button(root, text='2', width=8, height=3, bg='LightGreen', fg='brown',
                   command=lambda: update_entry('2')).place(x=100, y=302)
threeButton = Button(root, text='3', width=8, height=3, bg='LightGreen', fg='brown',
                     command=lambda: update_entry('3')).place(x=182, y=302)
fourButton = Button(root, text='4', width=8, height=3, bg='LightGreen', fg='brown',
                    command=lambda: update_entry('4')).place(x=17, y=222)
fiveButton = Button(root, text='5', width=8, height=3, bg='LightGreen', fg='brown',
                    command=lambda: update_entry('5')).place(x=100, y=222)
sixButton = Button(root, text='6', width=8, height=3, bg='LightGreen', fg='brown',
                   command=lambda: update_entry('6')).place(x=182, y=222)
sevenButton = Button(root, text='7', width=8, height=3, bg='LightGreen', fg='brown',
                     command=lambda: update_entry('7')).place(x=17, y=142)
eightButton = Button(root, text='8', width=8, height=3, bg='LightGreen', fg='brown',
                     command=lambda: update_entry('8')).place(x=100, y=142)
ninthButton = Button(root, text='9', width=8, height=3, bg='LightGreen', fg='brown',
                     command=lambda: update_entry('9')).place(x=182, y=142)

decimalButton = Button(root, text='.', width=8, height=3, bg='LightBlue', command=lambda: update_entry('.')).place(
    x=182, y=382)
equalButton = Button(root, text='=', width=8, height=8, bg='Red', command=lambda: equalOper()).place(x=264, y=307)
plusButton = Button(root, text='+', width=8, height=3, bg='gray', command=lambda: update_entry('+')).place(x=264,
                                                                                                           y=222)
minusButton = Button(root, text='-', width=8, height=3, bg='gray', command=lambda: update_entry('-')).place(x=264,
                                                                                                            y=142)
multiplyButton = Button(root, text='x', width=8, height=3, bg='gray', command=lambda: update_entry('x')).place(x=264,
                                                                                                               y=66)
divideButton = Button(root, text='÷', width=8, height=3, bg='gray', command=lambda: update_entry('÷')).place(x=182,
                                                                                                             y=66)
clearButton = Button(root, text='Clear (CE)', width=20, height=3, command=clear, bg='Black', fg="Pink").place(x=17,
                                                                                                             y=66)

# Locks the parent windows size.
root.maxsize(350, 450)
root.minsize(350, 450)

# Parent window's background color:
root.configure(background='pink')
root.mainloop()
