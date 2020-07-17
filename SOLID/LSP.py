# Liskov Substitution Principle
# if a class or method works with a base class, it should also work with any of its children classes


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rect):
    # here we cached the width
    w = rect.width
    # for square here it will be changed
    rect.height = 10
    # here we still use the old value, therefore we are breaking the LSP
    expected = int(w * 10)
    print(expected)


rc = Rectangle(2, 3)
use_it(rc)
print(rc.height)
print(rc.area)

sq = Square(5)
use_it(sq)
print(sq.area)