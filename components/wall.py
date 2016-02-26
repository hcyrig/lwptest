#! /usr/bin/env Python3

import copy

from components.brick import Brick
from components.builder import Builder


class Wall:
    """
     It is an area for building something witch user has been wanted
    """
    # constructor for wall mush have area parameter

    def __init__(self, data):   # 'area' is a <list type>

        self.width = 0
        self.height = 0
        if data is not None:
            self.is_builded = False
            self.is_correct_construction = False
            self.blueprint = self.__create_blueprint(data)
            if self.blueprint is not None:
                self.bricks = Wall.__create_bricks(data[self.height+1:])
        else:
            self.is_correct_construction = False

    # public interface for wall

    def force_self(self):

        # sort bricks to max -> min len

        self.bricks = Brick.sort(self.bricks)
        return Builder(self).build()

    # print existing wall

    def print(self):

        print()
        print("Wall:")
        print("W: ", self.width, end=" ")
        print("H: ", self.height)
        for row in self.blueprint:
            for part in row:
                if part == 1:
                    print("[]", end="")
                else:
                    print("  ", end="")
            print()
        Brick.print(self.bricks)

    def print_raw_data(self):

        print("Raw wall:")
        print(self.width, self.height, self.blueprint)
        print("Raw bricks:")
        print(Brick.blueprint)

    # separate a raw wall's data to object fields

    def __create_blueprint(self, data):

        wall_skeleton = data[0]
        self.width = int(wall_skeleton[0])
        self.height = int(wall_skeleton[1])
        return data[1:self.height+1]

    # separate a raw bricks' data to object fields

    # put the brick into 'ij' postion

    def put_by_ver(self, brick, ij):

        for i in range(ij[0], len(self.blueprint)):
            if i >= ij[0] + brick.height:
                break
            for j in range(ij[1], len(self.blueprint[i])):
                if j < ij[1] + brick.width:
                    self.blueprint[i][j] = 0
                else:
                    break

    def put_by_hor(self, brick, position):

        for i in range(position[0], len(self.blueprint)):
            if i >= position[0] + brick.width:
                break
            for j in range(position[1], len(self.blueprint[i])):
                if j < position[1] + brick.height:
                    self.blueprint[i][j] = 0
                else:
                    break

    # check the wall creation

    def is_created_wall(self):

        for part in self.blueprint:
            for p in part:
                if p == 1:
                    return False
        return True

    # check a brick on the wall

    def is_exist_brick_by(self, ij, brick):

        if len(self.blueprint) - (ij[0] + brick.height) >= 0 and \
                    len(self.blueprint[ij[0]]) - (ij[1] + brick.width) >= 0:
            for i in range(ij[0], ij[0] + brick.height):
                    for j in range(ij[1], ij[1] + brick.width):
                        if self.blueprint[i][j] == 0:
                            return False
            return True
        else:
            return False

    # search a brick on the wall / return a brick postion

    def search_exist_brick_hor(self, brick, y, x):

        for i in range(y, len(self.blueprint)):
            width = 0
            for j in range(x, len(self.blueprint[i])):
                if self.blueprint[i][j] == 1:
                    width += 1
                    if width == brick.width:
                        x = (j+1) - width
                        if self.is_exist_brick_by((i, x), brick):
                            return [i, x]
                        x = 0
                        width = 0
                else:
                    width = 0
        return None

    # search The Bricks' probably postions / return bricks'
    # positions as [[],[]]

    def is_search_probably_hor(self, search, brick):

        find = True
        wall = copy.deepcopy(self)
        while find:
            ij = wall.search_exist_brick_hor(brick, 0, 0)
            if ij is not None:
                wall.put_by_ver(brick, ij)
                search.append(ij)
            else:
                find = False

        print()
        print("The Bricks' probably positions")
        print(search)
        print()
        return [search, []]

    def probably_brick_positions(self, brick):

        # horizontal search of probably positions for bricks

        search = []
        find = self.is_search_probably_hor(search, brick)
        if len(find[0]) == 0:
            brick.rotate()
            find = self.is_search_probably_hor(search, brick)
        return find

    @classmethod
    def __create_bricks(cls, data):

        Brick.blueprint = data
        bricks_skeleton = data[0]
        Brick.types = int(bricks_skeleton[0])
        bricks_blueprints = data[1:]
        type_list = []
        for blueprint in bricks_blueprints:
            type_list.append(Brick(blueprint[0],
                                   blueprint[1],
                                   blueprint[2]))
        return type_list
