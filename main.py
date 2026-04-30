import tkinter as tk

def resize_oval(event):

    w, h = event.width, event.height

    oval_w = 15
    oval_h = 15
    otstup = 50

    x0 = otstup
    x1 = otstup + oval_w

    y0 = (h - oval_h) // 2
    y1 = (h + oval_h) // 2

    canvas.coords(oval, x0, y0, x1, y1)


root = tk.Tk()
root.title("точка")
root.state('zoomed')

canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

oval = canvas.create_oval(1, 1, 1, 1, fill='black', outline='black', tags = 'krug')

def linia():


def click():
    canvas.itemconfig(oval, fill='red')
    Line = canvas.create_line(1, 1, 200, 50, tags= "jopa")


def unclick():
    canvas.itemconfig(oval, fill = 'black')
    canvas.delete("jopa")


# vfi
canvas.bind("<Configure>", resize_oval)

canvas.tag_bind(oval, "<ButtonPress-1>", click)

canvas.tag_bind(oval, "<ButtonRelease-1>", unclick)

root.mainloop()
