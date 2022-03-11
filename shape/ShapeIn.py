import numpy as np

from .Shape import Shape
from .tools import middle, project_circle


class ShapeIn(Shape):
    def __init__(self, r: float):
        """
        init shape in circle
        :param r: radus of square
        """
        self.r = r
        self._points = np.array([(r, 0), (0, -r), (-r, 0), (0, r)])

    @property
    def points(self):
        return self._points

    def next(self):
        new_points = np.empty((len(self._points) * 2, 2), dtype=np.dtype('d'))
        p1 = self._points[-1]
        i = 0
        for p2 in self._points:
            new_points[i] = project_circle(middle(p1, p2), self.r)
            new_points[i + 1] = p2
            p1 = p2
            i += 2

        self._points = new_points
        return self._points
