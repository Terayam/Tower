import math


class Rect():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    # Easy-access functions
    def left(self):
        return self.x

    def right(self):
        return self.x + self.w

    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.h

    def tl(self):
        return (self.x, self.y)

    def tr(self):
        return (self.right(), self.y)

    def bl(self):
        return (self.x, self.bottom())

    def br(self):
        return (self.right(), self.bottom())

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

    def set_top(self, y):
        self.y = y

    def set_bottom(self, y):
        self.y = (y - self.h)

    def set_center(self, pt):
        self.x = (pt[0] - (self.w / 2))
        self.y = (pt[1] - (self.h / 2))

    def set_tl(self, pt):
        self.x = pt[0]
        self.y = pt[1]

    def set_tr(self, pt):
        self.set_right(pt[0])
        self.y = pt[1]

    def set_bl(self, pt):
        self.x = pt[0]
        self.set_bottom(pt[1])

    def set_br(self, pt):
        self.set_right(pt[0])
        self.set_bottom(pt[1])

    # Geometry functions
    def area(self):
        return (self.w * self.h)

    def perim(self):
        return (2 * (self.w + self.h))

    def diag(self):
        return math.sqrt((self.w * self.w) + (self.h * self.h))

    def radius(self):
        return (self.diag() / 2)
