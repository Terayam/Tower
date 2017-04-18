import rm


class Level:

    def __init__(self):

        self.id = 0
        self.background = None

    def set_background(self, filename):
        self.background = rm.load_image(filename)
