"""
you are given a class called Square and a function called calculate_area() which calculates the area of a given
rectangle.
in order to use Square in calculate_area, instead of augmenting it with width/height members, implement the
SquareToRectangleAdapter class. This adapter takes a square and adapts it in such a way that it can be used as an
argument to calculate_area()
"""
from unittest import TestCase


class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


# we give this class width, height. so we can feed it an square and in return its object can be used as argument of
# calculate_area
class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

    
class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))


