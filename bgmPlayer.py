import pyglet
import defaults


class BgmPlayer:

    def __init__(self):

        # Create a new source group to hold the music queue using the
        # default Audio format and no video format
        self.srcGroup = pyglet.media.SourceGroup(defaults.defaultAudioFormat,
                                                 None)

        # create a new pyglet player
        # note: this class assumes that the pyglet media subsystem has already
        # been initialized
        self.pyglet_player = pyglet.media.Player()

        # set the default behavior to loop
        self.pyglet_player.eos_action = pyglet.media.SourceGroup.loop

    def change_source(self, source):

        # Clear the current source and start the next one
        self.srcGroup.next_source()
        self.srcGroup.queue(source)

        self.pyglet_player.next_source()
        self.pyglet_player.queue(self.srcGroup)

    def loop(self, looping):
        self.srcGroup.loop = looping

    def play(self):
        self.pyglet_player.play()

    def pause(self):
        self.pyglet_player.pause()
