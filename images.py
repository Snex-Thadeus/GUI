from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Snex-Tech Systems")
#root.iconbitmap('C:\Users\HOMELUX\PycharmProjects\GUI\codemy.ico')

my_img = ImageTk.PhotoImage(Image.open("images/me.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()