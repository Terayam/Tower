import pyglet
import wall


class Level:

    def __init__(self, sprite_batch):

        self.background = None
        self.sprite_batch = sprite_batch
        self.entities = []

        # Create all level objects
        self.build_level()

    def build_level(self):
        self.add_walls()
        self.add_entities()

    def set_background(self, filename):
        self.background = pyglet.image.load(filename)

    # TODO: This seems like it shouldn't really be a member function of the
    # Level class.  This is something a LevelBuilder should do instead
    def add_wall(self, wallX, wallY, wallW, wallH):

        # Create a new wall to add to the list
        new_wall = wall.Wall()

        # Set wall dimensions
        new_wall.set_pos_size_bbox(wallX, wallY, wallW, wallH)

        self.entities.append(new_wall)

    def draw(self):
        self.background.blit(0, 0)
