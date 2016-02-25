#! /usr/bin/env Python3


class Builder:

    """ It's a class to perform algorithm which check can wall build or not
    from portion of bricks
    """

    def __init__(self, wall):
        self.wall = wall

    def build(self):
        self.wall.print()
        print("Algorithm comming soon in the next version of application")
        return False
