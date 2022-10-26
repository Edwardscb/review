# create a to-do list that: can accept an item and add it to a list, adds the item to localStorage(or similar), and upon page refresh(or similar) the item will persist
# allows the user to click a button to remove the item and then when they remove the item, it removes it from the screen and also removes its persistence

# imports all the things from tkinter - tkinter is in the standard library
from tkinter import *
from tkinter import messagebox

# using ws (ws is arbitrary) to initialize Tk() - From now on, ws will be called as the parent window.  All other widgets will be placed on it
ws = Tk()

# gives us the window geometry, the format is: width x height + x-position + y-position
# width is horizontal space
# height is vertical space
# x-position refers to the position of the window on the display over the x-axis
# y-position refers to the position of the window on the display over the y-axis
ws.geometry('500x450+500+200')




