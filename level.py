import pyglet
import wall


class Level:

    def __init__(self, sprite_batch):

        self.background = None
        self.has_player = False
        self.sprite_batch = sprite_batch
        self.entities = []

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    def add_wall(self, wallX, wallY, wallW, wallH):

        # Create a new wall to add to the list
        new_wall = wall.Wall()

        # Set wall dimensions
        new_wall.set_pos_size_bbox(wallX, wallY, wallW, wallH)

        self.entities.append(new_wall)

    def draw(self):
        self.background.blit(0, 0)
