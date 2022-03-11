from .Shape import Shape
from .ShapeIn import ShapeIn
from .ShapeOut import ShapeOut


class ShapeInOut(Shape):
    def __init__(self, r: float):
        self.__shape_in = ShapeIn(r)
        self.__shape_out = ShapeOut(r)
        self.__r = r
        self.last = 0

    @property
    def r(self):
        return self.__r

    @property
    def shape_in(self):
        return self.__shape_in

    @property
    def shape_out(self):
        return self.__shape_out

    @property
    def size_shapes(self):
        """
        size of shape in shape out
        :return:
        """
        return self.shape_in.size, self.shape_out.size

    @property
    def pi_bound(self):
        """
        bound in/ out of pi
        :return:
        """
        return tuple(map(lambda x: x / (2 * self.r), self.size_shapes))

    def __len__(self):
        """
        number point of shape
        """
        return len(self.shape_in)

    @property
    def pi_approx(self):
        """
        py aporximation string
        :return:
        """
        pi_in, pi_out = tuple(map(str, self.pi_bound))
        while pi_in[self.last] == pi_out[self.last]:
            self.last += 1
        return pi_in[:self.last]

    @property
    def points(self):
        """
        points shape in / shape out
        """
        return self.shape_in.points, self.shape_out.points

    def next(self):
        self.shape_in.next()
        self.shape_out.next()

    def __str__(self):
        b_in, b_out = self.pi_bound
        return f"{len(self)}:  {b_in} < π < {b_out}"
