#! /usr/bin/env Python3

from components.brick import Brick
from components.builder import Builder


class Wall:
    """
     It is an area for building something witch user has been wanted
    """
    # constructor for wall mush have area parameter

    blueprint = []

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

        print("Wall:")
        print("Width: ", self.width)
        print("Height: ", self.height)
        print("Blueprint:", self.blueprint)
        Brick.print(self.bricks)

    # separate a raw wall's data to object fields

    def __create_blueprint(self, data):

        wall_skeleton = data[0]
        self.width = int(wall_skeleton[0])
        self.height = int(wall_skeleton[1])
        Wall.blueprint = data[:self.height+1]
        return data[1:self.height+1]

    # separate a raw bricks' data to object fields

    @classmethod
    def __create_bricks(cls, data):

        Brick.blueprint = data
        bricks_skeleton = data[0]
        Brick.types = int(bricks_skeleton[0])
        bricks_blueprints = data[1:]
        type_list = []
        for blueprint in bricks_blueprints:
            for one_bl in range(0, int(blueprint[2])):
                type_list.append(Brick(blueprint[0],
                                       blueprint[1],
                                       blueprint[2]))
        return type_list
