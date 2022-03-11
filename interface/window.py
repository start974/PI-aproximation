from tkinter import Button, Listbox, Label, StringVar

from shape import ShapeInOut
from .Canvas import MainCanvas

class Mainwindow():
    canvas_size = 750

    def __init__(self, master, height=1000, width=1000):
        self.master = master
        self.height = height
        self.width = width

        r = (width * 0.6) / 2
        self.shapes = ShapeInOut(r)

        self.__set_window_property()
        self.__set_canvas()
        self.__set_label_pi()
        self.__set_box_approx()
        self.__set_buttons()

    def __set_window_property(self):
        self.master.title("PI approximation")
        self.master.geometry(f"{self.width}x{self.height}")

        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)

        self.master.rowconfigure(0, weight=4)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=2)
        self.master.rowconfigure(3, weight=2)
        self.master.columnconfigure(1, weight=1)

    def __set_canvas(self):
        self.canvas = MainCanvas(self.shapes)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=5, sticky="news")
        self.canvas.draw()

    def __set_buttons(self):
        self.start_button = Button(self.master, text="Start iteration", default="disabled") \
            .grid(row=2, column=1, sticky="nsew")

        self.next_button = Button(self.master, text="Next iteration", command=self.next_pi) \
            .grid(row=2, column=2, sticky="nsew")

        self.close_button = Button(self.master, text="Close", command=self.master.quit) \
            .grid(row=3, column=1, columnspan=2, sticky="nsew")

    def __set_box_approx(self):
        self.box_approx = Listbox(self.master, activestyle="none", exportselection=0)
        self.box_approx.grid(row=2, column=0, rowspan=2, sticky="nsew")

        self.__add_approx()

    def __set_label_pi(self):
        self.label_pi_var = StringVar()
        Label(self.master, textvar=self.label_pi_var) \
            .grid(row=1, column=0, columnspan=3, sticky="ew")
        self.__update_pi()

    def __add_approx(self):
        self.box_approx.insert(0, str(self.shapes))

    def __update_pi(self):
        approx = self.shapes.pi_approx

        self.label_pi_var.set(f"({len(approx)}) π = {approx}")

    def next_pi(self):
        self.shapes.next()
        self.canvas.draw()
        self.__add_approx()
        self.__update_pi()
