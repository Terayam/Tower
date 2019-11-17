from primitives import entity
from util import util_functions


class Wall(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Wall, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Wall, self).bbox_to_image()
        self.bbox.color = util_functions.random_color()

        self.collidable = True

        self.interaction_name = 'Wall'
