import entity
import util


class Wall(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Wall, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Wall, self).bbox_to_image()
        self.bbox.color = util.random_color()

        self.collidable = True

    def collide(self, other):

        # Don't collide if either sprite is not collidable
        if(self.collidable and other.collidable):

            # Get the rectangle overlap
            overlap = self.bbox.union(other.bbox)

            if(overlap and self.debug_overlap):
                overlap.color = (255, 0, 0, 255)
                overlap.draw()

            if(overlap):

                # Call the collide with wall function
                # of the other sprite with this sprite
                other.collide_with_wall(self, overlap)
