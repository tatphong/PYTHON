from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning")
root.iconbitmap("D://Code/Python/Tkinter/test.ico")

myimg = ImageTk.PhotoImage(Image.open("D://Code/Python/Tkinter/Azul.jpg"))
myimg2 = ImageTk.PhotoImage(Image.open("D://Code/Python/Tkinter/image2.jpg"))
img_list = [myimg, myimg2]
img_box = Label(image=img_list[0])
img_box.pack()


mylabel1 = Label(root, text="Hello, type something here!", fg="red").pack()
e = Entry(root, borderwidth=5)
e.pack()
e.insert(0, "Name: ")
# e.delete(0, END)
# mylabel1.grid(row=0,column=0, columnspan=2)
# mylabel2.grid(row=1,column=0)
def click_action(name):
    mylb = Label(root, text=name).pack()

def shift():
    e.delete(0, END)
    e.insert(0, "Changed!!!")
change = Button(root, text="Change", command=shift, state=DISABLED).pack()

mybtn = Button(root, text="OK", command=lambda: click_action(e.get().split("Name: ")[1]), padx=20, pady=5).pack()#grid(row=3,column=0)

def next():
    global img_box
    img_box.forget()
    img_box = Label(image=img_list[1]).pack()

next = Button(root, text=">>", command=next).pack()

quit = Button(root, text="quit", command=root.quit).pack()

# status bar
status = Label(root, text="Write some status here", bd=3, relief=SUNKEN, anchor=E).pack(fill=BOTH)
root.mainloop()