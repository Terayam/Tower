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

            moveLeftHat = False
            moveRightHat = False
            moveUpHat = False
            moveDownHat = False

            moveLeftAna = False
            moveRightAna = False
            moveUpAna = False
            moveDownAna = False

            # Check hat X position
            if(self.joystick.hat_x > 0):
                moveLeftHat = False
                moveRightHat = True
            elif(self.joystick.hat_x < 0):
                moveLeftHat = True
                moveRightHat = False

            # check hat Y position
            if(self.joystick.hat_y > 0):
                moveUpHat = True
                moveDownHat = False
            elif(self.joystick.hat_y < 0):
                moveUpHat = False
                moveDownHat = True

            # Check X axis position
            if(self.joystick.x < -0.5):
                moveLeftAna = True
                moveRightAna = False
            elif(self.joystick.x > 0.5):
                moveLeftAna = False
                moveRightAna = True

            # Check y axis position
            if(self.joystick.y < -0.5):
                moveUpAna = True
                moveDownAna = False
            elif(self.joystick.y > 0.5):
                moveUpAna = False
                moveDownAna = True

            self.moveLeft = moveLeftHat or moveLeftAna
            self.moveRight = moveRightHat or moveRightAna
            self.moveUp = moveUpHat or moveUpAna
            self.moveDown = moveDownHat or moveDownAna
