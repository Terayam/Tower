import pyglet
import wall


class Level:

    def __init__(self):

        self.background = None
        self.wall_sprite_batch = pyglet.graphics.Batch()
        self.walls = []

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
            w.batch = self.wall_sprite_batch

    def draw(self):
        self.background.blit(0, 0)

        # Draw wall Batch
        self.wall_sprite_batch.draw()
