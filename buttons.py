from tkinter import *

a = 0

root = Tk()

myLabel = Label(root, text = "hello")

def manageClick():
    global a
    global myLabel

    a += 1

    myLabel.pack_forget()
    myLabel = Label(root, text = "You clicked the button " + str(a) + " times")
    myLabel.pack()

myButton = Button(root, text = "Click me", padx = 50, pady = 10, command = manageClick)
myButton.pack()

root.mainloop()