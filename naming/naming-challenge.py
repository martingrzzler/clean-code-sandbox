class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"X: {self.x}, Y: {self.y}\n")


class Rectangle:
    def __init__(self, bottom_left, width, height):
        self.bottom_left = bottom_left
        self.top_right = Point(bottom_left.x + width, bottom_left.y + height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print_bottom_left(self):
        self.bottom_left.print()

    def print_top_right(self):
        self.top_right.print()


width = 90
height = 10
rect = Rectangle(Point(50, 100), width, height)

rect.print_bottom_left()
rect.print_top_right()

print(rect.area())
