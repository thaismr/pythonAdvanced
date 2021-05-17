def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    numbers = (1, 4, 5, 7, 8, 0, 10, 11, 15, 30, 22)
    letters = "acwrQrvtjiogBserS"

    odds = list(filter(lambda x: x % 2 != 0, numbers))
    print(odds)

    low_caps = list(filter(lambda x: x.isupper(), letters))
    print(low_caps)

    squares = list(map(lambda x: x**2, numbers))
    print(squares)

    week = list(map(lambda d: 'weekend' if (d == "SUN" or d == "SAT") else 'work day', days))
    print(week)


if __name__ == "__main__":
    main()
