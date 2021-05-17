import collections


def main():
    coords = collections.namedtuple("Coordinates", "x y")

    p1 = coords(10, 20)
    p2 = coords(40, 50)
    print(p1, p2)
    print('P1:', p1.x, p1.y)
    print('P2:', p2.x, p2.y)

    p1 = p1._replace(x=100, y=200)
    print(p1)


if __name__ == "__main__":
    main()
