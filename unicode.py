from tkinter import *

root = Tk()
root.title('Snex-Tech Systems!')
root.iconbitmap('snex.ico')
root.geometry("400x400")


my_label = Label(root, text='41' + u'\u00A2', font=("Helvetica", 32)).pack(pady=10)

my_button = Button(root, text=u'\u00BB', font=("Helvetica", 32)).pack(pady=10)





root.mainloop()