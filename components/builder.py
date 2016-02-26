#! /usr/bin/env Python3

import copy


class Builder:
    """ It's a class to perform algorithm which check can wall build or not
    from portion of bricks
    """

    def __init__(self, wall):
        self.wall = wall

    def build(self):

        while len(self.wall.bricks) != 0:

            wall = copy.deepcopy(self.wall)
            bricks = copy.deepcopy(self.wall.bricks)
            result = self.__check(wall, bricks)
            if not result:
                if len(self.wall.bricks) != 0:
                    brick = self.wall.bricks[0]
                    if brick.count == 0:
                        self.wall.bricks = self.wall.bricks[1:]
                    else:
                        brick.count -= 1
                        if brick.count == 0:
                            self.wall.bricks = self.wall.bricks[1:]
                        else:
                            self.wall.bricks[0] = brick
                    continue
            else:
                return result
        return False

    @classmethod
    def __is_bricks_empty(cls, bricks):

        for brick in bricks:
            if brick.count >= 1:
                return False
        return True

    def __check(self, wall, bricks):

        if wall.is_created_wall():
            wall.print()
            return True
        if Builder.__is_bricks_empty(bricks):
            wall.print()
            return False

        temp_positions = 0
        brick = bricks[0]
        if brick.count:
            wall.print()
            positions = wall.probably_brick_positions(brick)
            if len(positions):
                if len(positions[0]) < len(positions[1]):
                    wall.put_by_hor(brick, positions[1][0])
                    temp_positions = len(positions[1])
                elif len(positions[0]) >= len(positions[1]):
                    if len(positions[0]) != 0:
                        wall.put_by_ver(brick, positions[0][0])
                        temp_positions = len(positions[0])

            brick.count -= 1
            bricks[0] = brick
            wall.bricks = bricks

        if brick.count > 0 and temp_positions > 0:
            return self.__check(wall, bricks)
        else:
            return self.__check(wall, bricks[1:])
