import itertools


def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    numbers = (15, 30, 22)
    letters = "acwrQrvtjiogBserS"

    # method cycle() iterates over a list
    cycle = itertools.cycle(numbers)
    print(next(cycle), end=', ')
    print(next(cycle), end=', ')
    print(next(cycle), end=', ')
    print(next(cycle))

    counter = itertools.count(100, 10)
    print(next(counter), next(counter), next(counter), next(counter))

    add_ups = itertools.accumulate(numbers)
    print(list(add_ups))

    maxes = itertools.accumulate(numbers, max)
    print(list(maxes))

    chained = itertools.chain(numbers, days)
    print(list(chained))

    # days after 'WED'
    print(list(itertools.dropwhile(lambda d: d != "WED", days)))

    # days before 'WED'
    print(list(itertools.takewhile(lambda d: d != "WED", days)))


if __name__ == "__main__":
    main()
