# create a to-do list that: can accept an item and add it to a list, adds the item to localStorage(or similar), and upon page refresh(or similar) the item will persist
# allows the user to click a button to remove the item and then when they remove the item, it removes it from the screen and also removes its persistence

# imports all the things from tkinter - tkinter is in the standard library
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

# using ws (ws is arbitrary) to initialize Tk() - From now on, ws will be called as the parent window.  All other widgets will be placed on it
ws = Tk()

# gives us the window geometry, the format is: width x height + x-position + y-position
# width is horizontal space
# height is vertical space
# x-position refers to the position of the window on the display over the x-axis
# y-position refers to the position of the window on the display over the y-axis
ws.geometry('500x450+500+200')

# Title adds title to the window
# config used to provide background color to window
# resizable accepts bools - false means window can't be re-sized
# ws.mainloop() holds the screen so we can see the window, it is an infinite loop.  Otherwise the window would just pop up once and then disappear
# using the loop, it keeps a constant refresh going so that we are constantly seeing the new version of the window every time

ws.title('to-do list')
ws.config(bg = '#223441')
ws.resizable(width = False, height = False)


ws.mainloop()

# Frame widgets are used to hold other widgets - they help in keeping & maintaining user interface and user experience clean/organized
# we will place Listbox, scrollbars, and buttons inside the frame
# in this way, frame will act as an additional window over the parent window
# pady=10 means we have extra padding around the frame from the outside

frame = Frame(ws)
frame.pack(pady = 10)

# bd = 0 refers to the border equal zero, fg is foreground
# highlightthickness=0 every time the focus is moved to any item then it should not show any movement that is value 0, by default it has a value
# selectbackground decides the color of items that are focused within the listbox
# activestyle="none" removes the underline that appears when an item is selected or focused
# geometry manager used is pack()
# side=LEFT keeps the listbox to the left side of the frame, makes it so we can assign the right position to scrollbars
# fill=BOTH fills the blank space in both the x and y directions

lb = Listbox(
    frame,
    width = 25,
    height = 8,
    font = ('Times', 18),
    bd = 0,
    fg = '#464646',
    highlightthickness = 0,
    selectbackground = '#a6a6a6',
    activestyle = "none",

)

lb.pack(side = LEFT, fill = BOTH)

# task_list variable stores the data
# for loop used to insert data into the Listbox
# every time the loop runs, it adds an item to the Listbox and continues until all items are inserted
# lb.insert(END, item) command stacks the items in the Listbox.  insert is a built-in method for Listbox
# END signifies that the new item will be added in the end, if END is replaced with 0 then new data will be added at the top

task_list = [
    'Eat apple',
    'drink water',
    'go to gym',
    'write software',
    'learn something'
]

for item in task_list:
    lb.insert(END, item)

# For scrollbars, geometry method used is a pack() so that everything remains dynamic and in a sequence
# side = RIGHT allows us to place the scrollbars on the right side
# lb.config(yscrollcommand=sb.set) assigns a purpose to the scrollbar, we have to bind Listbox with scrollbar
# sb.config(command=lb.yview) makes the scrollbar move in the y direction (yview)


sb = Scrollbar(frame)
sb.pack(side = RIGHT, fill=BOTH)

lb.config(yscrollcommand = sb.set)
sb.config(command = lb.yview)

# entry box is used to take input from the user, ws entry box is placed on the parent window, geometry manager used is pack with padding of 20 outside the widget

my_entry = Entry(
    ws,
    font = ('times', 24)
)

my_entry.pack(pady=20)

# add another frame for buttons

button_frame = Frame(ws)
button_frame.pack(pady = 20)

# adding buttons: need to add two buttons, addTask and deleteTask
# command: when a button is clicked the function mentioned in the command is called

# get() method is used to pull the value provided by the user in the entry box.
# if-else condition is applied to avoid blank space entry in the Listbox
# if the task does not have blank space, only then will it allow it to store the information in the Listbox, otherwise warning message

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter a task.")

# here ANCHOR refers to the selected item in the Listbox, delete is a built-in function to delete Listbox item

def deleteTask():
    lb.delete(ANCHOR)

addTask_btn = Button(
    button_frame,
    text = 'Add Task',
    font = 'Tahoma',
    bg = '#c5f776',
    padx = 20,
    pady = 10,
    command = newTask 
)

addTask_btn.pack(fill = BOTH, expand = True, side = LEFT)

delTask_btn = Button(
    button_frame, 
    text = 'Delete Task',
    font = 'Tahoma',
    bg = '#ff8b61',
    padx = 20,
    pady = 10,
    command = deleteTask
)

delTask_btn.pack(fill = BOTH, expand = True, side = LEFT)








