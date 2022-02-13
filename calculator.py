from tkinter import *

# creates root widget comes first in any tkinter app
root = Tk()
# use .title to give window a title
root.title("Calculator App")

# entry creates an input field
inputBox = Entry(root, width=35, borderwidth=5)
# uses .grid to display on the gui using row and column to tell where to display the labels it will ignore empty columns and rows
# columnspan tells it to set number of columns
# padx and pady determine the size of the widget
inputBox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    # .get grabs what has been iputed in the box
    current_number = inputBox.get()
    # uses delete to remove what has been entered otherwise it will duplicate numbers as you add more
    inputBox.delete(0, END)
    # inputs the number parameter from the button you have clicked and puts it next to the previously pressed number
    # have to make them a string as concat will add the numbers aswell
    inputBox.insert(0, str(current_number) + str(number))

# define what clear button does
def button_clear():
    inputBox.delete(0, END)
    
# define what the plus button does
def button_add():
    first_number = inputBox.get()
    # makes global variable to be used outside this function
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    inputBox.delete(0, END)
    
def button_subtract():
    first_number = inputBox.get()
    # makes global variable to be used outside this function
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    inputBox.delete(0, END)

def button_division():
    first_number = inputBox.get()
    # makes global variable to be used outside this function
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    inputBox.delete(0, END)

def button_multiply():
    first_number = inputBox.get()
    # makes global variable to be used outside this function
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    inputBox.delete(0, END)
    
# define what equals button does
def button_equal():
    second_number = inputBox.get()
    inputBox.delete(0, END)
    # checks which button is pressed the does the set math
    if math == "addition":
        inputBox.insert(0, f_num + int(second_number))

    if math == "subtraction":
        inputBox.insert(0, f_num - int(second_number))
        
    if math == "division":
        inputBox.insert(0, f_num / int(second_number))
        
    if math == "multiplication":
        inputBox.insert(0, f_num * int(second_number))  
    
    



# creates a buttons 0-9 command tells it to use the defined function
# using lambda allows to enter a paramerter to the buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_plus = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_division)
button_times = Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_equals = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_c = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# uses grid to display buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_times.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_plus.grid(row=4, column=3)

button_c.grid(row=5, column=0, columnspan=2)
button_equals.grid(row=5, column=2, columnspan=2)








# uses root widget with mainloop which displays the gui and keeps it looping till closed
root.mainloop()