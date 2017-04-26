import pyglet
import entity
import constants
import math


class Player(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Player, self).__init__(*args, **kwargs)

        # Initialize state variables
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def handle_key_press(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeft = True
        elif(symbol == pyglet.window.key.D):
            self.moveRight = True
        elif(symbol == pyglet.window.key.W):
            self.moveUp = True
        elif(symbol == pyglet.window.key.S):
            self.moveDown = True
        else:
            pass

    def handle_key_release(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeft = False
        elif(symbol == pyglet.window.key.D):
            self.moveRight = False
        elif(symbol == pyglet.window.key.W):
            self.moveUp = False
        elif(symbol == pyglet.window.key.S):
            self.moveDown = False
        else:
            pass

    def read_joystate(self, joystick_handler):

        self.moveLeft = joystick_handler.moveLeft
        self.moveRight = joystick_handler.moveRight
        self.moveUp = joystick_handler.moveUp
        self.moveDown = joystick_handler.moveDown

    def update(self, elapsed_s):

        # accelerate in the direction of movement
        if(self.moveRight):
            self.xAcc = constants.MOVEACCEL
        elif(self.moveLeft):
            self.xAcc = -constants.MOVEACCEL
        else:
            self.xAcc = 0

        if(self.moveUp):
            self.yAcc = constants.MOVEACCEL
        elif(self.moveDown):
            self.yAcc = -constants.MOVEACCEL
        else:
            self.yAcc = 0

        super(Player, self).update(elapsed_s)

        # Cap maximum speed of player
        self.cap_normal_moves_speed()

    def cap_normal_moves_speed(self):

        # Get magnitude of ve,ocity vector
        mag = math.sqrt((self.xVel * self.xVel) + (self.yVel * self.yVel))

        # If magnitude  if greater than max, scale components proportionally
        if(mag > constants.MAXSPEED):
            self.xVel = (constants.MAXSPEED / mag) * self.xVel
            self.yVel = (constants.MAXSPEED / mag) * self.yVel
