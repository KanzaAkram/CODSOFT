from tkinter import *
from tkinter import messagebox

cal = Tk()                      # Creating basic window
cal.geometry("312x394")         # Size of the window width:- 312, height:- 394
cal.resizable(0, 0)             # This prevents from resizing the window
cal.title("Simple Calculator")

#>>>>>>>>>>>>>>>>>>>>>>>>>>functions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def about():
    messagebox.showinfo('About'," \n Created by KANZA MUHAMMAD AKRAM \n \n")

def click_button(item):                                           # 'click_button' function continuously updates the input field whenever you enters a number
    global expression                                             # 'expression' variable globally declared to store the expression string
    inputText.set(inputText.get()+(str(item)))                    # concatenation of string with the input text variable and store the value in 'expression' variable

def clear_button():                                               # 'clear_button' function clears the last input item
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clear_all():                                                  # 'clear_all' function clears the input field
    inputText.set("")

def equal_button():
    result = ""
    try:
        result = eval(inputText.get())                             # 'eval' function evalutes the string expression directly
        inputText.set(result)
    except:
        result = "_ERROR_"
        inputText.set(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>menubar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
menubar = Menu(cal,bg="yellow",fg="pink")

filemenu = Menu(menubar, tearoff=0,bg="pink",fg="black")
filemenu.add_command(label="Cut", accelerator="Ctrl+X" )
filemenu.add_command(label="Copy",accelerator="Ctrl+C" )
filemenu.add_command(label="Paste",accelerator="Ctrl+V")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=cal.quit)

menubar.add_cascade(label="Edit", menu=filemenu)    #.add_cascade is used to create a parent menu item and add other menu items to it in a hierarchical way.
helpmenu = Menu(menubar, tearoff=0,bg="pink",fg="black")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

cal.config(bg="pink",menu=menubar)  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Frame>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
expression = ""
inputText = StringVar()                     # 'StringVar()' is used to get the instance of input field

#Input Frame
inputFrame = Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="crimson", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 17 ), textvariable=inputText, width=50,fg="black", bg="yellow", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)

#Button Frame
button_frame = Frame(cal, width=312, height=272.5, bg="yellow")
button_frame.pack()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Buttons>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#First_row
clearall = Button(button_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_bracket= Button(button_frame, text = "(", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_bracket = Button(button_frame, text = ")", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "<", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)

#Second_row
power = Button(button_frame, text = "^", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "π", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(3.1415)).grid(row = 2, column = 1, padx = 1, pady = 1)
exp  = Button(button_frame, text = "e", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(2.7182)).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_= Button(button_frame, text = "/", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

#Third_row
seven = Button(button_frame, text = "7", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fourth_row
four = Button(button_frame, text = "4", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#Fifth_row
one = Button(button_frame, text = "1", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

#Sixth_row
point = Button(button_frame, text = ".", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg="black", width = 10, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "black", width = 21, height = 3, bd = 0, bg="pink", cursor = "hand2", command = lambda: equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
cal.mainloop()                       #mainloop() is an infinite loop used to run the application
