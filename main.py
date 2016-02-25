#! /usr/bin/env Python3

import components

from components.director import Director


def create_director():
    return Director()


def life_circle():

    director = create_director()
    if director.prepare():
        wall = director.is_running()
        if wall is not None:
            print(wall.force_self())
            del wall
    del director

# scripts's an enter point

print("The test programme as a wall's building algorithm.")
print("programme's version is: ", components.__version__)

life_circle()

print("programme closes without errors")
print("Have a nice day!")
