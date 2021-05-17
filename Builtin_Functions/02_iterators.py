def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    days_long = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    iterator = iter(days)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    with open('data.txt', 'r') as data_f:
        # read until end of file (''):
        for line in iter(data_f.readline, ''):
            print(line, end='')

    print()

    for num in range(len(days)):
        print(num, days[num], end=', ')

    for i, day in enumerate(days):
        print(i, day)

    print('Returns a tuple for each pair of values:')
    for day in zip(days, days_long):
        print(day)

    for i, day in enumerate(zip(days, days_long)):
        print(i, day[0], '=', day[1])


if __name__ == "__main__":
    main()
