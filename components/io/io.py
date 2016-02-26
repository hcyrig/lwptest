#! /usr/bin/env Python3

import sys

from components.io import constants


class IO:
    """
    get data from standart input source or from file source
    """

    # private implementation

    @classmethod
    def __file_name_from_params(cls):
        is_file_in_parametres = False
        for element in sys.argv:
            if is_file_in_parametres:
                return element
            if element == constants.FILE_COMMAND_LINE_KEY:
                is_file_in_parametres = True
                continue
            print("In command line params file name hasn't founded")
        return None

    @classmethod
    def __file_name(cls):
        file_name = IO.__file_name_from_params()
        if file_name is None:
            file_name = constants.FILE_DEFAULT_TITLE
        return file_name

    # public implementation

    @classmethod
    def data_from_file(cls):

        try:
            with open(IO.__file_name(),
                      constants.FILE_READ_PARAMETER,
                      encoding=constants.FILE_DEFAULT_ENCODING) as infile:
                return infile.readlines()
        except Exception as e:
            print("In current folder a file hasn't founded \
            or file hasn't corrected. Exp: ", e)
        return None

    @classmethod
    def data_from_standart_input(cls):

        try:
            data = list()
            data.append(input(constants.STANDART_INPUT_PART_OF_WALL_DEFINE))
            for index in range(0, int(data[0][0])):
                data.append(input(
                    constants.STANDART_INPUT_PART_OF_WALL_BLUEPRINT))
            data.append(input(constants.STANDART_INPUT_PART_OF_BRICKS_TYPES))
            for index in range(0, int(data[-1])):
                data.append(input(
                    constants.STANDART_INPUT_PART_OF_BRICKS_BLUEPRINTS))
            print(data)
            return data
        except Exception as e:
            print("Exp: ", e)
            return None
