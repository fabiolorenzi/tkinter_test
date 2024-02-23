from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello world")
myLabel2 = Label(root, text = "My name is Fabio")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

myLabel3 = Label(root, text = "Boh, it's a test")
myLabel4 = Label(root, text = "nothing else to say")

myLabel3.grid(row=2, column=0)
myLabel4.grid(row=2, column=2)

root.mainloop()