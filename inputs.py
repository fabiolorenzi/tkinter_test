from tkinter import *

root = Tk()

def manageClick():
    name = myInput.get()
    myLabel = Label(root, text='Hello {0}'.format(name))
    myLabel.pack()

myInput = Entry(root, width=50)
myInput.pack()
myInput.insert(0, "Enter your name")

myButton = Button(root, text="Click me", command=manageClick)
myButton.pack()

root.mainloop()