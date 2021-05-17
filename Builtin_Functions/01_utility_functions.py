def main():
    num_list = [0, 1, 2, 3, 4, 5, 6]
    print(num_list)

    # any value in the list is True
    print(any(num_list))

    # all values in the list are True
    print(all(num_list))

    print('Min: ', min(num_list))
    print('Max: ', max(num_list))
    print('Sum:', sum(num_list))


if __name__ == "__main__":
    main()
