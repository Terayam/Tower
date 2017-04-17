import pygame
import os
import constants


def load_image(filename):

    fullpath = os.path.join('img', filename)

    try:
        image = pygame.image.load(fullpath)
    except pygame.error:
        print('Cannot load image:', filename)
        raise SystemExit

    image.set_colorkey(constants.COLORKEY, pygame.RLEACCEL)

    return image
