import pygame
import os
import constants
import level


def load_image(filename):

    fullpath = os.path.join(constants.IMGDIR, filename)

    try:
        image = pygame.image.load(fullpath)
    except pygame.error:
        print('Cannot load image:', filename)
        raise SystemExit

    image.set_colorkey(constants.COLORKEY, pygame.RLEACCEL)

    return image


def load_all_levels():

    level_list = {}

    # Load each file in level directory
    for filename in os.listdir(constants.LEVELDIR):

        level = load_level(filename)

        # Add loaded level to list
        if(level is None):
            print("Error parsing level from: {0}".format(filename))
        else:
            level_list[level.id] = level

    return level_list


def load_level(filename):

    fullpath = os.path.join(constants.LEVELDIR, filename)

    #  Try to open the level
    level_file = open(fullpath, 'r')

    # Create storage for level
    new_level = None

    # Check if the file opened
    if(not level_file):
        print('Could not open file "{0}"'.format(fullpath))
    else:
        new_level = parse_level(level_file)

    # Close file
    level_file.close()

    # Check for level parsing errors
    if(new_level is None):
        print('Error parsing level in "{0}"'.format(fullpath))

    # Done
    return new_level


def parse_level(level_file):

    # storage for a new level
    new_level = level.Level()

    # Visit each line in the file
    for line in level_file:

        attribute = line[0:line.find(':')]
        value = line[line.find(':') + 1:-1].strip()

        # Process data
        if(attribute == 'id'):
            new_level.id = int(value)

        elif(attribute == 'background'):
            new_level.set_background(value)

        elif(attribute == 'next_level'):
            new_level.next_level = int(value)

    return new_level
