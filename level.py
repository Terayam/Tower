import pyglet


class Level:

    def __init__(self):

        self.id = 0
        self.background = None
        self.next_level = 0
        self.walls = []

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    def draw(self):
        self.background.blit(0, 0)
