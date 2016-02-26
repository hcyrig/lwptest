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
    def __is_created_wall(cls, wall):

        for part in wall.blueprint:
            for objectp in part:
                if objectp == 1:
                    return False
        return True

    @classmethod
    def __is_bricks_empty(cls, bricks):

        for brick in bricks:
            if brick.count >= 1:
                return False
        return True

    @classmethod
    def __put_by_ver(cls, wall, brick, ij):

        for i in range(ij[0], len(wall.blueprint)):
            if i >= ij[0] + brick.height:
                break
            for j in range(ij[1], len(wall.blueprint[i])):
                if j < ij[1] + brick.width:
                    wall.blueprint[i][j] = 0
                else:
                    break

    @classmethod
    def __put_by_hor(cls, wall, brick, position):

        for i in range(position[0], len(wall.blueprint)):
            if i >= position[0] + brick.width:
                break
            for j in range(position[1], len(wall.blueprint[i])):
                if j < position[1] + brick.height:
                    wall.blueprint[i][j] = 0
                else:
                    break

    @classmethod
    def __is_exist_brick_by(cls, wall, ij, brick):

        if len(wall.blueprint) - (ij[0] + brick.height) >= 0 and \
                    len(wall.blueprint[ij[0]]) - (ij[1] + brick.width) >= 0:
            for i in range(ij[0], ij[0] + brick.height):
                    for j in range(ij[1], ij[1] + brick.width):
                        if wall.blueprint[i][j] == 0:
                            return False
            return True
        else:
            return False

    @classmethod
    def __search_exist_brick_hor(cls, wall, brick, y, x):

        for i in range(y, len(wall.blueprint)):
            width = 0
            for j in range(x, len(wall.blueprint[i])):
                if wall.blueprint[i][j] == 1:
                    width += 1
                    if width == brick.width:
                        x = (j+1) - width
                        if Builder.__is_exist_brick_by(wall, (i, x), brick):
                            return [i, x]
                        x = 0
                        width = 0
                else:
                    width = 0
        return None

    @classmethod
    def __is_search_probably_hor(cls, search, wall, brick):

        find = True
        wall = copy.deepcopy(wall)
        while find:
            ij = Builder.__search_exist_brick_hor(wall, brick, 0, 0)
            if ij is not None:
                Builder.__put_by_ver(wall, brick, ij)
                search.append(ij)
            else:
                find = False

        print(search)
        return [search, []]

    @classmethod
    def __probably_brick_positions(cls, wall, brick):

        # horizontal search of probably positions for bricks

        search = []
        find = Builder.__is_search_probably_hor(search, wall, brick)
        if len(find[0]) == 0:
            w = brick.width
            brick.width = brick.height
            brick.height = w
            find = Builder.__is_search_probably_hor(search, wall, brick)
        return find

    def __check(self, wall, bricks):

        if Builder.__is_created_wall(wall):
            wall.print()
            return True
        if Builder.__is_bricks_empty(bricks):
            wall.print()
            return False

        temp_postions = 0
        brick = bricks[0]
        if brick.count:
            wall.print()
            positions = Builder.__probably_brick_positions(wall, brick)
            if len(positions):
                if len(positions[0]) < len(positions[1]):
                    Builder.__put_by_hor(wall, brick, positions[1][0])
                    temp_postions = len(positions[1])
                elif len(positions[0]) >= len(positions[1]):
                    if len(positions[0]) != 0:
                        Builder.__put_by_ver(wall, brick, positions[0][0])
                        temp_postions = len(positions[0])

            brick.count -= 1
            bricks[0] = brick
            wall.bricks = bricks

        if brick.count > 0 and temp_postions > 0:
            return self.__check(wall, bricks)
        else:
            return self.__check(wall, bricks[1:])
