#! /usr/bin/env Python3


class Brick:
    """
    The Brick instance contents information of one real brick
    """

    blueprint = []

    def __init__(self, width, height, count):

        self.width = width
        self.height = height
        self.count = count

    # sort bricks to max -> min
    # specify comporator key

    @classmethod
    def print(cls, data):
        if isinstance(data, list):
            print()
            print("Bricks:")
            print()
            for brick in data:
                if isinstance(brick, Brick):
                    for w in range(0, brick.width):
                        for h in range(0, brick.height):
                            print("*", end="")
                        print()
                    print(brick.count)
                print()

    @classmethod
    def sort(cls, data):
        data = sorted(data, key=Brick.cmp_to_key(Brick.comparator))
        return data[::-1]

    @classmethod
    def cmp_to_key(cls, mycmp):

        """
        Convert a cmp= function into a key= function
        """

        class K:

            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
        return K

    # specify comporator, calculate which brick is larger then another one

    @classmethod
    def comparator(cls, x, y):

        x_digit = x.width
        if x.width <= x.height:
            x_digit = x.height
        y_digit = y.width
        if y.width <= y.height:
            y_digit = y.height
        return x_digit - y_digit
