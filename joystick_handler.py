class Joystick_handler():

    def __init__(self):

        # Input states
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

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

            # Check X axis position

            # Check y axis position
