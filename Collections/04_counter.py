from collections import Counter


def main():
    a = "acwrQrvtjiogBserS"
    b = "BFTyvdyiSSiomwpOM"

    count_a = Counter(a)
    count_b = Counter(b)

    print(count_a)
    print(count_a)

    # how many letters 'r'?
    print(
        count_a['r'],
        count_b['r']
    )

    # how many letters total?
    print(
        sum(
            count_a.values()
        )
    )

    # join both
    count_a.update(count_b)
    print(sum(count_a.values()))

    # 5 most common letters now
    print(count_a.most_common(5))

    # subtract b
    count_a.subtract(count_b)
    print(sum(count_a.values()))

    # all by most common
    print(count_a.most_common())

    # count intersection
    print(count_a & count_b)


if __name__ == "__main__":
    main()
