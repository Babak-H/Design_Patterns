# a Factory is a component responsible solely for the wholesale (not piecewise) creation of objects

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} , {self.y}'

    # def __init__(self, a, b, sys=CoordinateSystem.CARTESIAN):
    # if sys == CoordinateSystem.CARTESIAN:
    #     self.x = a
    #     self.b = b
    # elif sys == CoordinateSystem.POLAR:
    #     self.x = a * cos(b)
    #     self.y = a * sin(b)

    @staticmethod
    def new_cartesian_point(x, y):  # Factory Method
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):  # Factory Method
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)
