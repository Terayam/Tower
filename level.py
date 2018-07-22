import pyglet
import wall


class Level:

    def __init__(self, sprite_batch):

        self.background = None
        self.has_player = False
        self.sprite_batch = sprite_batch
        self.walls = []
        self.entities = []

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    def add_wall(self, wallX, wallY, wallW, wallH):

        # Create a new wall to add to the list
        new_wall = wall.Wall()

        # Set wall dimensions
        new_wall.set_pos_size_bbox(wallX, wallY, wallW, wallH)

        self.walls.append(new_wall)

    def reset_walls_sprite_group(self):

        for w in self.walls:
            w.batch = self.sprite_batch

    def draw(self):
        self.background.blit(0, 0)
