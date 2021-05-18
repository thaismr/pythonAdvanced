
class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Coords x:{0}, y:{1}>'.format(self.x, self.y)

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    c1 = Coords(10, 20)
    c2 = Coords(50, 70)
    print(c1, c2)

    c3 = c1 + c2
    print(c3)

    c4 = c2 - c1
    print(c4)

    c1 += c2
    print(c1)


if __name__ == "__main__":
    main()
