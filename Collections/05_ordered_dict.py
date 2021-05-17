from collections import OrderedDict


def main():
    scores = [
        ("Name", (18, 12)),
        ("Name 2", (10, 8)),
        ("Name 3", (15, 9))
    ]
    sorted_scores = sorted(scores, key=lambda t: t[1][0], reverse=True)
    print(sorted_scores)

    scores = OrderedDict(sorted_scores)
    print(scores)

    name, stats = scores.popitem(False)
    print('Highest score:', name, stats)
    print(scores)


if __name__ == "__main__":
    main()
