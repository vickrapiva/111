import tkinter as tk
from math import hypot

class MainWindow(tk.Tk
):
    """Главное окно приложения, наследуемое от Tk"""
    
    def __init__(self):
        super().__init__()
        self.title("точка")
        self.geometry('1000x1000')

        self.ovals = {}

        self.canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.draw_oval(ox=250, oy=250, r=50)
        self.canvas.bind("<Button-1>", self.on_mouse_down)      # Нажатие ЛКМ
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)     # Движение с зажатой ЛКМ
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up) # Отпускание ЛКМ
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.select_oval_id = None
        self.draw_line_id = None

    def draw_oval(self, ox, oy, r, fill='black', outline='black'):
        oval_id = self.canvas.create_oval(ox-r, oy-r, ox+r, oy+r, fill=fill, outline=outline)
        self.ovals[oval_id] = {
            'ox': ox,
            'oy': oy,
            'r': r,
        }

    def on_mouse_down(self, event):
        items = self.canvas.find_closest(event.x, event.y)
        if not items:
            return
        oval_id = items[0]
        oval = self.ovals[oval_id]
        l = hypot(oval['ox'] - event.x, oval['oy'] - event.y)
        if l <= oval['r']:
            self.select_oval_id = oval_id
            self.canvas.itemconfig(oval_id, fill='red')
            self.draw_line_id = self.canvas.create_line(oval['ox'], oval['oy'], event.x, event.y)

    def on_mouse_up(self, event):
        if self.select_oval_id:
            self.canvas.itemconfig(self.select_oval_id, fill='black')
            self.select_oval_id = None
            self.draw_line_id = None

    def on_mouse_move(self, event):
        if self.select_oval_id and self.draw_line_id:
            oval = self.ovals[self.select_oval_id]
            self.canvas.coords(self.draw_line_id, oval['ox'], oval['oy'], event.x, event.y)

MainWindow().mainloop()
