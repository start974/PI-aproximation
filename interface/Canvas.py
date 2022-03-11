from tkinter import Canvas, ALL

from shape import ShapeInOut, Shape


class MainCanvas(Canvas):
    CUTOFF = 2048
    def __init__(self, shape_in_out: ShapeInOut):
        self.bg_color = "gray"
        self.r = shape_in_out.r
        self.size = self.r * 2 * 1.2
        self.height = self.size
        self.width = self.size
        super(MainCanvas, self).__init__(bg=self.bg_color, height=self.height, width=self.width)
        self.shapes = shape_in_out

    @property
    def center(self):
        return self.width / 2, self.height / 2

    def to_coord_canvas(self, x, y):
        x_center, y_center = self.center
        return x_center + x, y_center - y

    def __draw_circle(self):
        r = self.r
        x1, y1 = self.to_coord_canvas(-r, -r)
        x2, y2 = self.to_coord_canvas(r, r)
        self.create_oval(x1, y1, x2, y2, width=2, outline="red")

    def draw_repere(self):
        """
        (unused)
        draw trièdre in center
        """
        x0, y0 = self.to_coord_canvas(0, 0)
        x1, y1 = self.to_coord_canvas(50, 50)
        self.create_line(x0, y0, x1, y0, arrow="last")
        self.objects.append(l1)
        self.create_line(x0, y0, x0, y1, arrow="last")

    def __draw_shape(self, shape: Shape, **kwargs) -> None:
        if len(shape.points) > self.CUTOFF:
            return
        points = [self.to_coord_canvas(v[0], v[1]) for v in shape.points]
        self.create_polygon(points, width=2, **kwargs)

    def draw(self, ):
        self.delete(ALL)
        self.__draw_shape(self.shapes.shape_out, fill="yellow", outline="green")
        self.__draw_shape(self.shapes.shape_in, fill=self.bg_color, outline="cyan")
        self.__draw_circle()
