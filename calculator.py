

from tkinter import *

base_window = Tk()
base_window.title("Calculator")

#base_window.geometry("500x500")
base_window.minsize(250,450)    #(w,h)
base_window.maxsize(250,450)


#mytext = Label(base_window, text= "hello world!!", bg = "#fc8003", fg="white", font = ("arial", 40, "bold"))
#mytext.grid(row=0, column = 0)

def click(number):
    current_value = entry.get()
    #entry.delete(0, END)
    entry.insert(END, str(number))
    #entry.insert(0, str(current_value) + str(number))

def addition():
    global first_number
    global sign
    sign = "add"
    first_number  = entry.get()
    entry.delete(0, END)

def subtraction():
    global first_number
    global sign
    sign = "sub"
    first_number = entry.get()
    entry.delete(0, END)

def multiplication():
    global first_number
    global sign
    sign = "mul"
    first_number = entry.get()
    entry.delete(0, END)

def division():
    global first_number
    global sign
    sign = "div"
    first_number = entry.get()
    entry.delete(0, END)

def answer():
    second_number = entry.get()
    entry.delete(0, END)
    if sign == "add":
        entry.insert(0, float(first_number) + float(second_number))
    if sign == "sub":
        entry.insert(0, float(first_number) - float(second_number))
    if sign == "mul":
        entry.insert(0, float(first_number) * float(second_number))
    if sign == "div":
        entry.insert(0, float(first_number) / float(second_number))

def clear():
    entry.delete(0, END)


entry = Entry(base_window, width = 10, borderwidth = 2, font = ("arial", 40, "bold"))
entry.grid(row=0, column=0,columnspan=3)

mybutton_clear = Button(base_window, text = "Clear", padx = 30, pady = 30,command = clear).grid(row=0, column=2)


mybutton_7 = Button(base_window, text = "7", padx = 30, pady = 30,command = lambda : click(7)).grid(row=1, column=0)
mybutton_8 = Button(base_window, text = "8", padx = 30, pady = 30,command = lambda : click(8)).grid(row=1, column=1)
mybutton_9 = Button(base_window, text = "9", padx = 30, pady = 30,command = lambda : click(9)).grid(row=1, column=2)

mybutton_4 = Button(base_window, text = "4", padx = 30, pady = 30,command = lambda : click(4)).grid(row=2, column=0)
mybutton_5 = Button(base_window, text = "5", padx = 30, pady = 30,command = lambda : click(5)).grid(row=2, column=1)
mybutton_6 = Button(base_window, text = "6", padx = 30, pady = 30,command = lambda : click(6)).grid(row=2, column=2)

mybutton_1 = Button(base_window, text = "1", padx = 30, pady = 30,command = lambda : click(1)).grid(row=3, column=0)
mybutton_2 = Button(base_window, text = "2", padx = 30, pady = 30,command = lambda : click(2)).grid(row=3, column=1)
mybutton_3 = Button(base_window, text = "3", padx = 30, pady = 30,command = lambda : click(3)).grid(row=3, column=2)

mybutton_0 = Button(base_window, text = "0", padx = 30, pady = 30,command = lambda : click(0)).grid(row=4, column=0)
mybutton_add = Button(base_window, text = "+", padx = 30, pady = 30,command = addition).grid(row=4, column=1)
mybutton_equ = Button(base_window, text = "=", padx = 30, pady = 30,command = answer).grid(row=4, column=2)

mybutton_sub = Button(base_window, text = "-", padx = 30, pady = 30,command = subtraction).grid(row=5, column=0)
mybutton_mul = Button(base_window, text = "*", padx = 30, pady = 30,command = multiplication).grid(row=5, column=1)
mybutton_div = Button(base_window, text = "/", padx = 30, pady = 30,command = division).grid(row=5, column=2)


base_window.mainloop()