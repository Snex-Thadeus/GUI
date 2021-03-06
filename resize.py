from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Snex-Tech")
root.geometry("800x500")
root.iconbitmap('snex.ico')

# Open Image
my_pic = Image.open("images/me.jpg")

# Resize Image
resized = my_pic.resize((250, 188), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

# Image size 500x375 / 250x188
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)

root.mainloop()
