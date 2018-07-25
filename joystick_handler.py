import math

from util import constants


class Joystick_handler():

    def __init__(self):

        # Input states
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.x = 0.0
        self.y = 0.0

        self.joystick = None

    def set_joystick(self, joystick):

        self.joystick = joystick

    def update_joystate(self):

        if(self.joystick):

            # Check hat X position
            if(self.joystick.hat_x > 0):
                self.moveLeft = False
                self.moveRight = True
            elif(self.joystick.hat_x < 0):
                self.moveLeft = True
                self.moveRight = False
            else:
                self.moveLeft = False
                self.moveRight = False

            # check hat Y position
            if(self.joystick.hat_y > 0):
                self.moveUp = True
                self.moveDown = False
            elif(self.joystick.hat_y < 0):
                self.moveUp = False
                self.moveDown = True
            else:
                self.moveUp = False
                self.moveDown = False

            # Update analog state
            self.x = self.joystick.x
            self.y = -self.joystick.y  # Joystick direction is inverted

            # Joystick deadzone, circle shaped
            total_deflection = math.sqrt((self.x * self.x) +
                                         (self.y * self.y))

            if(total_deflection < constants.JS_DEADZONE):
                self.x = 0
                self.y = 0

            self.x = self.x * constants.ANALOG_GAIN
            self.y = self.y * constants.ANALOG_GAIN

            if(self.x > 1.0):
                self.x = 1.0
            elif(self.x < -1.0):
                self.x = -1.0

            if(self.y > 1.0):
                self.y = 1.0
            elif(self.y < -1.0):
                self.y = -1.0
