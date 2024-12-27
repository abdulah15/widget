from tkinter import*
from PIL import Image, ImageTk

root = Tk()
upload = Image.open("image.png")
image = ImageTk.PhotoImage(upload)


label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="this is how you add image in tkiner window")
label2.place(x=50, y=370)


from tkinter import messagebox

def msg():
    messagebox.showwarning("Alert","Stop virus found")

button = Button(root, text="Scan For Virus",command=msg)
button.place(x=40, y=80)

root.mainloop()