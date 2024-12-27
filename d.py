from tkinter import * 
root = Tk()
root.title("Root window")
root.geometry("400x300")

def topwin():

    top = Toplevel()
    top. geometry ("180x100" )
    top. title("toplevel")

    l2 = Label(top, text = "This is toplevel window")
    l2. pack()
    top.mainloop()

l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command =topwin)

l.pack()
btn.pack()