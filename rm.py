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

    return new_level
