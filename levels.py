import level

from entities import debt


class Debug1(level.Level):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Debug1, self).__init__(*args, **kwargs)

        self.set_background("media/img/bg.png")

    def add_walls(self):

        self.add_wall(250, 200, 50, 200)
        self.add_wall(350, 200, 50, 200)
        self.add_wall(175, 150, 300, 10)

    def add_entities(self):

        test_enemy = debt.Debt('media/img/enemy.png', batch=self.sprite_batch)
        test_enemy.target = self.player
        self.entities.append(test_enemy)


class Debug2(level.Level):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Debug2, self).__init__(*args, **kwargs)

        self.set_background("media/img/bg2.png")
