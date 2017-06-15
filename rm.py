import os
import constants
import level
import wall
import pyglet


###############################################################################
# Media Loading
###############################################################################


def initialize_media():
    pyglet.options['audio'] = ('pulse', 'openal', 'directsound', 'silent')


def load_sfx(filename):

    new_sound = pyglet.media.load(filename, streaming=False)
    
    if(not new_sound):
        print("Error loading sound: {0}".format(filename))

    return new_sound

###############################################################################
# Level Loading
###############################################################################


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

        elif(attribute == 'wall'):

            new_level.walls.append(parse_wall(value))

    # Refresh walls sprite batch
    new_level.reset_walls_sprite_group()

    return new_level


def parse_wall(wall_string):

    # Split string on commas
    split_string = wall_string.split(',')

    if(len(split_string) is not 4):
        print('Error parsing wall in: "', wall_string, '"')
        return None

    pattern = pyglet.image.SolidColorImagePattern(color=(0, 0, 0, 0))
    wall_image = pattern.create_image(1, 1)

    new_wall = wall.Wall(wall_image)

    # Split string on commas
    split_string = wall_string.split(',')

    new_wall.bbox.x = int(split_string[0])
    new_wall.x = int(split_string[0])
    new_wall.bbox.y = int(split_string[1])
    new_wall.y = int(split_string[1])
    new_wall.bbox.w = int(split_string[2])
    new_wall.bbox.h = int(split_string[3])

    return new_wall
