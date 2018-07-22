import pyglet
import wall


class Level:

    def __init__(self):

        self.id = 0
        self.background = None
        self.next_level = 0
        self.wall_sprite_batch = pyglet.graphics.Batch()
        self.walls = []

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    def add_wall(self, wallX, wallY, wallW, wallH):

        # Create a new wall to add to the list
        new_wall = wall.Wall()

        # TODO: A level should not need to know how to build a wall.  Move
        # this to the wall class
        new_wall.bbox.x = wallX
        new_wall.x = wallX
        new_wall.bbox.y = wallY
        new_wall.y = wallY
        new_wall.bbox.w = wallW
        new_wall.bbox.h = wallH

        self.walls.append(new_wall)

    def reset_walls_sprite_group(self):

        for w in self.walls:
            w.batch = self.wall_sprite_batch

    def draw(self):
        self.background.blit(0, 0)

        # Draw wall Batch
        self.wall_sprite_batch.draw()
