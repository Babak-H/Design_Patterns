# Open Closed Principle
# when you add functionality to a class, you add it via extension, NOT modification
# Open for extension, Closed for modification, instead of modifying a class, extend it (inherit from it in new class)
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    # this style breaks open-close principle (needs modification for any kind of change)
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p


# Specification

# base class (similar to Java interface)
class Specification:
    def is_satisfied(self, item):
        pass

    # &
    def __and__(self, other):
        # self here is a
        return AndSpecification(self, other)


# base class (similar to Java interface)
class Filter:
    # spec : Object of specification class
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # make sure each item satisfies every single specification
        return all(map(
            # this is the method from parent class
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item  # yield holds the item for you to do what you like with it


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.MEDIUM)

    products = [apple, tree, house]

    myFilter = BetterFilter()

    print('Green Products:')
    green = ColorSpecification(Color.GREEN)
    for p in myFilter.filter(products, green):
        print(p.name)

    large = SizeSpecification(Size.LARGE)

    print("Large Green items:")
    # large_green = AndSpecification(green, large)
    large_green = large & green  # & is same as __and__
    for p in myFilter.filter(products, large_green):
        print(p.name)
