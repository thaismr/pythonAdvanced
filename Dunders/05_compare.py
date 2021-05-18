
class Person:
    def __init__(self, name, level, exp):
        self.name = name
        self.level = level
        self.exp = exp

    def __ge__(self, other):
        if self.level == other.level:
            return self.exp >= other.exp
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.exp > other.exp
        return self.level > other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.exp <= other.exp
        return self.level <= other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.exp < other.exp
        return self.level < other.level

    def __repr__(self):
        return '<Person {0}: {1}, {2}>'.format(self.name, self.level, self.exp)


def main():
    person_1 = Person('John', 2, 10)
    person_2 = Person('Jane', 2, 15)
    person_3 = Person('Mary', 3, 15)
    print(person_1, person_2, person_3)

    dpt = [person_1, person_2, person_3, Person('Someone', 1, 5)]
    print(dpt[0] < dpt[1])
    print(dpt[2] > dpt[1])
    print(person_1 >= person_3)

    people = sorted(dpt)
    print(people)

    for person in people:
        print(person.name, end=' ')


if __name__ == "__main__":
    main()
