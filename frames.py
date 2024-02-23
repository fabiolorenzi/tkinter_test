from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello world")
root.iconbitmap("../asdf.ico")

frame = LabelFrame(root, padx=5, pady=1)
frame.pack(padx=10, pady=10)

frameButton = Button(frame, text = "test button")
frameButton.grid(row=0, column=0)

frameExit = Button(frame, text="Exit", command=root.quit)
frameExit.grid(row=0, column=1)

myImg = ImageTk.PhotoImage(Image.open("../asdf.jpg"))
imageLabel = Label(root, image=myImg)
imageLabel.pack()

root.mainloop()