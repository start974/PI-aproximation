import numpy as np

from .tools import get_normal, solve, project_circle
from .Shape import Shape


class ShapeOut(Shape):

    def __init__(self, r: float):
        """
        init shape in circle
        :param r: radius of square
        """
        self.r = r
        self._points = np.array([(r, r), (r, -r), (-r, -r), (-r, r)])

    @property
    def points(self):
        return self._points

    def next(self):
        new_points = np.empty((len(self._points) * 2, 2), dtype=np.dtype('d'))
        p1 = self._points[-2]
        p2 = self._points[-1]
        i = 0
        for p3 in self._points:
            p = project_circle(p2, self.r)
            p_n = get_normal(p)
            new_points[i] = solve(p_n, p, p1 - p2, p2)
            new_points[i + 1] = solve(p_n, p, p3 - p2, p2)
            p1, p2 = p2, p3
            i += 2

        self._points = new_points
        return self._points
