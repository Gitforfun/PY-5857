class Point(object):
    x, y = 0, 0
    _index = 0

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return self
        # return [self.x, self.y]

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return self.x
        elif self._index == 1:
            self._index += 1
            return self.y
        else:
            self._index = 0
            raise StopIteration


a = Point(4, 8)
b = Point(15, 16)

c = a + b  # a.__add__(b)

for point in a:
    print(point)

# numbers = map(str, [1, 2, 3, 4, 5])
# print(numbers)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))  --> numbers.__next__()
#
# for x in numbers:
#     print(x)
