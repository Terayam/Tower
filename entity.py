import pyglet
import constants
import rect


class Entity(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):

        # Call the sprite initializer, but don't set an image
        super(Entity, self).__init__(*args, **kwargs)

        ########################
        # Debugging Parameters #
        ########################

        ######################
        # Drawing parameters #
        ######################

        ######################
        # Physics Parameters #
        ######################
        self.subpixel = True

        # Set initial physics position
        self.bbox = rect.Rect()

        # Set initial velocity
        self.xVel = 0.0
        self.yVel = 0.0

        # Set initial acceleration
        self.xAcc = 0.0
        self.yAcc = 0.0

    def set_image(self, image):
        self.image = image

    def bbox_to_image(self):
        self.bbox.w = self.width
        self.bbox.h = self.height

    def update(self, elapsed_s):

        # Update velocity
        self.xVel = self.xVel + (self.xAcc * elapsed_s)
        self.yVel = self.yVel + (self.yAcc * elapsed_s)

        # Update position
        self.x = self.x + (self.xVel * elapsed_s)
        self.y = self.y + (self.yVel * elapsed_s)

        # Update bbox position
        self.bbox.x = self.x
        self.bbox.y = self.y

        # Oppose movement and freeze tiny movements
        deccel_speed = (constants.NORMALDECCEL * elapsed_s)

        if(abs(self.xVel) > deccel_speed):
            if(self.xVel > 0):
                self.xVel -= deccel_speed
            else:
                self.xVel += deccel_speed
        else:
            self.xVel = 0.0

        if(abs(self.yVel) > deccel_speed):
            if(self.yVel > 0):
                self.yVel -= deccel_speed
            else:
                self.yVel += deccel_speed
        else:
            self.yVel = 0.0

    def undraw(self, screen, background):
        screen.blit(background, self.rect, self.rect)

    def cap_normal_move_speed(self, max_speed):

        if(self.xVel > max_speed):
            self.xVel = max_speed
        elif(self.xVel < -max_speed):
            self.xVel = -max_speed

        if(self.yVel > max_speed):
            self.yVel = max_speed
        elif(self.yVel < -max_speed):
            self.yVel = -max_speed
