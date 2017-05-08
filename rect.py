import math
import pyglet


class Rect():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

        self.color = (255, 255, 255, 255)

    def draw(self):

        pattern = pyglet.image.SolidColorImagePattern(color=self.color)
        image = pattern.create_image(math.ceil(self.w),
                                     math.ceil(self.h))
        image.blit(self.x, self.y)

    # Easy-access functions
    def left(self):
        return self.x

    def right(self):
        return self.x + self.w

    def bottom(self):
        return self.y

    def top(self):
        return self.y + self.h

    def bl(self):
        return (self.x, self.y)

    def tr(self):
        return (self.right(), self.y)

    def tl(self):
        return (self.x, self.top())

    def br(self):
        return (self.right(), self.y)

    def h_center(self):
        return (self.x + (self.w / 2))

    def v_venter(self):
        return (self.y + (self.h / 2))

    def center(self):
        return (self.h_center(), self.y_center())

    # Easy set functions
    def set_left(self, x):
        self.x = x

    def set_right(self, x):
        self.x = (x - self.w)

    def set_bottom(self, y):
        self.y = y

    def set_top(self, y):
        self.y = (y - self.h)

    def set_center(self, pt):
        self.x = (pt[0] - (self.w / 2))
        self.y = (pt[1] - (self.h / 2))

    def set_bl(self, pt):
        self.x = pt[0]
        self.y = pt[1]

    def set_br(self, pt):
        self.set_right(pt[0])
        self.y = pt[1]

    def set_tl(self, pt):
        self.x = pt[0]
        self.set_top(pt[1])

    def set_tr(self, pt):
        self.set_top(pt[0])
        self.set_right(pt[1])

    # Geometry functions
    def area(self):
        return (self.w * self.h)

    def perim(self):
        return (2 * (self.w + self.h))

    def diag(self):
        return math.sqrt((self.w * self.w) + (self.h * self.h))

    def radius(self):
        return (self.diag() / 2)

    # Name: Union
    # Description: Returns the rectangular overlaping
    #              segment of this rectangle and the passed-in
    #              rectangle.
    def union(self, b):

        # Set the properties of the rectangle if a collision is
        # occurring, otherwise return None
        if((self.x < b.right()) and
           (self.right() > b.x) and
           (self.top() > b.y) and
           (self.y < b.top())):

            c = Rect()

            # Origin of the overlap is always the greatest X
            # and greatest Y
            c.x = max(self.x, b.x)
            c.y = max(self.y, b.y)

            # This is the top-right corner of the rectangle
            # and will be translated into W, H
            x2 = min(self.right(), b.right())
            y2 = min(self.top(), b.top())

            c.w = x2 - c.x
            c.h = y2 - c.y

            return c

        else:
            return None
