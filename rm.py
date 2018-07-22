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
