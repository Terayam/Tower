import pyglet


class Level:

    def __init__(self):

        self.id = 0
        self.background = None
        self.next_level = 0
        self.wall_sprite_batch = pyglet.graphics.Batch()
        self.walls = []

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    def reset_walls_sprite_group(self):

        for w in self.walls:
            w.batch = self.wall_sprite_batch

    def draw(self):
        self.background.blit(0, 0)

        # Draw wall Batch
        self.wall_sprite_batch.draw()
