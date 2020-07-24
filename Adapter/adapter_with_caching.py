# whenever out given API and the one we need do not match, we create an in-between component to connect them
# (called Adapter)


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print('.', end='')


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# this class is a list object, but with extra functionality (override of list class)
class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter():
    # we save each drawn line in the cache, so we don't have to reprocess it again
    # cache is a class-level variable
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        # find 4 corners of the line add all the points to a list
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points = []
        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    # we make this class iterable (each object of this class can be looped through)
    def __iter__(self):
        return iter(self.cache[self.h])  # loops through the points


def draw(rcs):
    print("\n\n -- Drawing Rectangles --\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rs = [Rectangle(1, 1, 10, 10),
          Rectangle(3, 3, 6, 6)]
    draw(rs)
    draw(rs)
