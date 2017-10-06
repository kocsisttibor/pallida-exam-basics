# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys

database = "favourites.txt"

def get_arguments():
    return sys.argv


def read_from_file():
    with open(database) as f:
        return f.read().splitlines()


def not_in_database(favourite):
    return favourite not in read_from_file()


def add_favourites(favourites):
    extended_favourites = read_from_file()
    for favourite in set(favourites):
        if not_in_database(favourite):
            extended_favourites.append(favourite)
    return extended_favourites


def write_to_file(favourites):
    pass


def controller():
    pass

# controller()
