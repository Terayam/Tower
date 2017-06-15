import pyglet


class BgmPlayer:

    def __init__(self):

        # create a new pyglet player
        # note: this class assumes that the pyglet media subsystem has already
        # been initialized
        self.pyglet_player = pyglet.media.Player()

        # set the default behavior to loop
        self.pyglet_player.eos_action = pyglet.media.Player.EOS_LOOP

    def change_source(self, source):
        self.pyglet_player.next_source()
        self.pyglet_player.queue(source)

    def play(self):
        self.pyglet_player.play()

    def pause(self):
        self.pyglet_player.pause()
