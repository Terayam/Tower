import level


class Debug1(level.Level):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Debug1, self).__init__(*args, **kwargs)

        self.has_player = True
        self.set_background("img/bg.png")
        self.add_wall(250, 200, 50, 200)
        self.add_wall(350, 200, 50, 200)
        self.add_wall(175, 150, 300, 10)


class Debug2(level.Level):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Debug2, self).__init__(*args, **kwargs)

        self.set_background("img/bg2.png")
