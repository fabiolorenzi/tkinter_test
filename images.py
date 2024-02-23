from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello world")
root.iconbitmap("../asdf.ico")

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()

myImg = ImageTk.PhotoImage(Image.open("../asdf.jpg"))
imageLabel = Label(image=myImg)
imageLabel.pack()

root.mainloop()