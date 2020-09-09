from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning")
root.iconbitmap("D://Code/Python/Tkinter/test.ico")

myimg = ImageTk.PhotoImage(Image.open("D://Code/Python/Tkinter/Azul.jpg"))
mylabel = Label(image=myimg)
mylabel.pack()


mylabel1 = Label(root, text="Hello, type something here!", fg="red").pack()
e = Entry(root, borderwidth=5)
e.pack()
e.insert(0, "Name: ")
# e.delete(0, END)
# mylabel1.grid(row=0,column=0, columnspan=2)
# mylabel2.grid(row=1,column=0)
def click_action(name):
    mylb = Label(root, text=name).pack()

mybtn = Button(root, text="OK", command=lambda: click_action(e.get().split("Name: ")[1]), padx=20, pady=5).pack()#grid(row=3,column=0)

quit = Button(root, text="quit", command=root.quit).pack()
root.mainloop()