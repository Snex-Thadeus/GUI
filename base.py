from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Snex-Tech Systems')
#root.iconbitmap('c:/GUI/snex.ico')


def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    #top.iconbitmap('c:/GUI/snex.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/me.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()
