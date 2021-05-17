
class Person:
    def __init__(self):
        self.name = "Jane"
        self.lastname = "Doe"
        self.age = 30

    def __repr__(self):
        data = [self.name, self.lastname, self.age]
        return '<class Person - name: {0}, lastname: {1}, age: {2}>'.format(*data)

    def __str__(self):
        data = [self.name, self.lastname, self.age]
        return '{0} {1} is {2} old'.format(*data)

    def __bytes__(self):
        data = [self.name, self.lastname, self.age]
        to_bytes = 'Person:{0}:{1}:{2}'.format(*data)
        return to_bytes.encode('utf-8')


def main():
    person = Person()

    print(person)
    print(str(person))
    print(repr(person))
    print(bytes(person))
    print('Formatted: {0}'.format(person))


if __name__ == "__main__":
    main()
