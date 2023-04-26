import math


class Circle:
    def __init__(self, radius: float) -> None:
        if type(radius) == float:
            self.radius = radius
        else:
            raise ValueError(f'Entered number has wrong format')

    def length(self):
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        return round(math.pi * self.radius ** 2, 2)


# circle = Circle(10)
circle = Circle(10.0)
print(circle.length(), circle.square())


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        if side_a <= 0:
            raise ValueError(f'First value must be greater than 0')
        else:
            self.side_a = side_a
            if side_b is None:
                self.side_b = side_a
            elif side_b <= 0:
                raise ValueError(f'Second value must be greater than 0')
            else:
                self.side_b = side_b

    def square_rectangle(self):
        return self.side_a * self.side_b

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


# rect = Rectangle(3, 12)
# rect = Rectangle(6, -17)
rect = Rectangle(-4, 8)
print(rect.len_rectangle(), rect.square_rectangle())