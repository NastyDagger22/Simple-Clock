# Adds tkinter (What makes the window show)
from tkinter import *
from tkinter.ttk import *

# strftime is what lets the time work
from time import strftime

# Creates the window and root.title is the window's name, in which this case is Clock
root = Tk()
root.title("Clock")

# - The format of time, in which this case is hours, minutes, seconds, and whether its AM or PM.
# - Config of text, it's text=string becasue string above label.config is the text that will be shown.
# - Rechecks the time each second (1000 milliseconds is a single second)

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time) 

# - Text and background settings, and also where the text will be.
label = Label(root, font=("Arial", 100), background = "grey", foreground = "white")
label.pack(anchor='center')

time()

mainloop()
