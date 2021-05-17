from collections import defaultdict


def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN", "MON"]

    count_days = defaultdict(int)
    count_from_50 = defaultdict(lambda: 50)

    for day in days:
        count_days[day] += 1
        count_from_50[day] += 1

    print(dict(count_days))
    print(dict(count_from_50))


if __name__ == "__main__":
    main()
