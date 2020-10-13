from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Snex-Tech Systems')
#root.iconbitmap('c:/GUI/snex.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    #if response == "yes":
    #	Label(root, text="You Clicked Yes!").pack()
    #else:
    #	Label(root, text="You Clicked No!!").pack()


Button(root, text="Popup", command=popup).pack()


mainloop()