
class Colors:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == 'rgb':
            return self.red, self.green, self.blue
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == 'rgb':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):
        return "red", "green", "blue", "rgb"


def main():
    colors = Colors()

    print(colors)
    print(colors.rgb)

    colors.rgb = (125, 200, 86)
    print(colors.rgb)
    print(colors.red)

    print(dir(colors))


if __name__ == "__main__":
    main()
