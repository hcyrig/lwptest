#! /usr/bin/env Python3

# Constances for work with files when user might to attach it

FILE_READ_PARAMETER = 'r'

FILE_COMMAND_LINE_KEY = '-f'

FILE_DEFAULT_TITLE = 'walls_blueprint.txt'

FILE_DEFAULT_ENCODING = 'utf-8'

STANDART_INPUT_PART_OF_WALL_DEFINE = '''
            Please input data in this format:
            x y, where x - columns, y - rows of walls blueprint (matrix of
            possible positions)
            instance:
            3 4
'''

STANDART_INPUT_PART_OF_WALL_BLUEPRINT = '''
            0110 - it is a instance matrix, it is an example for you
            1101   where 0 - empty position, 1 - exist position of part\
            of brick
            1111
'''

STANDART_INPUT_PART_OF_BRICKS_TYPES = '''
            x , where x - count of bricks' types
            instance:
            3
'''

STANDART_INPUT_PART_OF_BRICKS_BLUEPRINTS = '''
            x, y, z - where x - horizontal count of brick's part,
                            y - vertical count of brick's path,
                            z - count of bricks in current type
            instance:
            1 1 10
            1 4 4
            2 2 1
'''