import pyglet

from util import defaults


class BgmPlayer:

    def __init__(self):

        # Create a new source group to hold the music queue using the
        # default Audio format and no video format
        self.srcGroup = pyglet.media.SourceGroup()

        # create a new pyglet player
        # note: this class assumes that the pyglet media subsystem has already
        # been initialized
        self.pyglet_player = pyglet.media.Player()

        # set the default behavior to loop
        #self.pyglet_player.eos_action = pyglet.media.SourceGroup.loop

        # Set the default BGM volume
        self.original_volume = 1.0
        self.muted = False

    def change_source(self, source):

        # Clear the current source and start the new one
        self.srcGroup = pyglet.media.SourceGroup()
        self.srcGroup.add(source)

        self.pyglet_player.next_source()
        self.pyglet_player.queue(self.srcGroup)

    def loop(self, looping):
        self.pyglet_player.loop = looping

    def play(self):
        self.pyglet_player.play()

    def pause(self):
        self.pyglet_player.pause()

    def playing(self):
        return self.pyglet_player.playing

    def set_volume(self, vol):
        self.pyglet_player.volume = vol

    def mute(self):

        self.original_volume = self.pyglet_player.volume
        self.muted = True
        self.set_volume(0.0)

    def unmute(self):
        self.muted = False
        self.set_volume(self.original_volume)
