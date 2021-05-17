import collections, string


def main():
    a = "acwrQrvtjiogBserS"
    b = "BFTyvdyiSSiomwpOM"

    letters_deque = collections.deque(string.ascii_lowercase)
    print(len(letters_deque))

    for letter in letters_deque:
        print(letter.upper(), end=',')

    letters_deque.pop()  # take out 'z'
    letters_deque.popleft()  # take out 'a'
    letters_deque.append(1)
    letters_deque.appendleft(2)
    print('\n', letters_deque)

    letters_deque.rotate(10)  # moves items 10 places to the right, while end items come to first 10 places
    print(letters_deque)


if __name__ == "__main__":
    main()
