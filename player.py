import pyglet
import entity
import constants
import math
import util


class Player(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Player, self).__init__(*args, **kwargs)

        # Movement keys
        self.moveLeftDigital = False
        self.moveRightDigital = False
        self.moveUpDigital = False
        self.moveDownDigital = False

        # Initialize state variables
        self.hMove = 0.0
        self.vMove = 0.0

    def handle_key_press(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeftDigital = True
        elif(symbol == pyglet.window.key.D):
            self.moveRightDigital = True
        elif(symbol == pyglet.window.key.W):
            self.moveUpDigital = True
        elif(symbol == pyglet.window.key.S):
            self.moveDownDigital = True

    def handle_key_release(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeftDigital = False
        elif(symbol == pyglet.window.key.D):
            self.moveRightDigital = False
        elif(symbol == pyglet.window.key.W):
            self.moveUpDigital = False
        elif(symbol == pyglet.window.key.S):
            self.moveDownDigital = False

    def read_joystate(self, joystick_handler):

        self.moveLeftDigital |= joystick_handler.moveLeft
        self.moveRightDigital |= joystick_handler.moveRight
        self.moveUpDigital |= joystick_handler.moveUp
        self.moveDownDigital |= joystick_handler.moveDown

        temp_hMove = 0.0
        temp_vMove = 0.0

        if(self.moveLeftDigital):
            temp_hMove = -1.0
        elif(self.moveRightDigital):
            temp_hMove = 1.0

        if(self.moveUpDigital):
            temp_vMove = 1.0
        elif(self.moveDownDigital):
            temp_vMove = -1.0

        self.hMove = util.biggest([temp_hMove, joystick_handler.x])
        self.vMove = util.biggest([temp_vMove, joystick_handler.y])

    def update(self, elapsed_s):

        # accelerate in the direction of movement
        if(self.hMove > 0.0):
            self.xAcc = constants.MOVEACCEL
        elif(self.hMove < 0.0):
            self.xAcc = -constants.MOVEACCEL
        else:
            self.xAcc = 0

        if(self.vMove > 0.0):
            self.yAcc = constants.MOVEACCEL
        elif(self.vMove < 0.0):
            self.yAcc = -constants.MOVEACCEL
        else:
            self.yAcc = 0

        super(Player, self).update(elapsed_s)

        # Cap maximum speed of player
        self.cap_normal_moves_speed()

    def cap_normal_moves_speed(self):

        self.xVel = util.smallest([constants.MAXSPEED * self.hMove, self.xVel])
        self.yVel = util.smallest([constants.MAXSPEED * self.vMove, self.yVel])
