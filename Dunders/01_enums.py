from enum import Enum, auto


class Fruit(Enum):
    GRAPE = 1
    BANANA = 2
    ORANGE = 3
    PEAR = auto()


def main():
    print(Fruit)
    print(Fruit.GRAPE)
    print(type(Fruit.GRAPE))
    print(repr(Fruit.GRAPE))

    print(Fruit.GRAPE.name, Fruit.GRAPE.value)

    print('Pear:', Fruit.PEAR.value)

    fruits = dict()
    fruits[Fruit.BANANA] = "Yellow"
    print(fruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
