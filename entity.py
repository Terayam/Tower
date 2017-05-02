import pyglet
import constants


class Entity(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):

        # Call the sprite initializer, but don't set an image
        super(Entity, self).__init__(*args, **kwargs)

        ########################
        # Debugging Parameters #
        ########################
        self.debug_rect = False

        ######################
        # Drawing parameters #
        ######################

        ######################
        # Physics Parameters #
        ######################
        self.subpixel = True

        # Set initial physics position
        self.x = 0.0
        self.y = 0.0

        # Set initial velocity
        self.xVel = 0.0
        self.yVel = 0.0

        # Set initial acceleration
        self.xAcc = 0.0
        self.yAcc = 0.0

    def set_image(self, image):
        self.image = image

    def update(self, elapsed_s):

        # Update velocity
        self.xVel = self.xVel + (self.xAcc * elapsed_s)
        self.yVel = self.yVel + (self.yAcc * elapsed_s)

        # Update position
        self.x = self.x + (self.xVel * elapsed_s)
        self.y = self.y + (self.yVel * elapsed_s)

        # Oppose movement and freeze tiny movements
        deccel_speed = (constants.NORMALDECCEL * elapsed_s)

        if(self.xVel > 0):
            self.xVel -= deccel_speed

            # Stop moving if direction changed
            if(self.xVel < 0):
                self.xVel = 0

        else:
            self.xVel += deccel_speed

            # Stop moving if direction changed
            if(self.xVel > 0):
                self.xVel = 0

        if(self.yVel > 0):
            self.yVel -= deccel_speed

            # Stop moving if direction changed
            if(self.yVel < 0):
                self.yVel = 0

        else:
            self.yVel += deccel_speed

            # Stop moving if direction changed
            if(self.yVel > 0):
                self.yVel = 0


    def undraw(self, screen, background):
        screen.blit(background, self.rect, self.rect)
