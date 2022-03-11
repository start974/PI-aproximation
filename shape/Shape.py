from abc import ABC, abstractmethod
from functools import reduce

from .tools import reduce_op


class Shape(ABC):
    @property
    @abstractmethod
    def points(self):
        """
        points in shape
        :return: matrix swith n line and 2 column (view as list of vector2)
        """

    @property
    def size(self):
        """
        size of shape (circonference)
        """
        points = self.points
        return reduce(reduce_op, points, (points[-1], 0))[1]

    def __len__(self):
        """
        number points contain in shape
        """
        return len(self.points)

    @abstractmethod
    def next(self):
        """
        transform shape to next shape
        """
