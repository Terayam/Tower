import pyglet
import constants
import math


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

    def set_draw_pos(self, xPos, yPos):
        # Move drawing rectangle to current physics point
        self.x = math.floor(self.xPos)
        self.y = math.floor(self.yPos)

    def set_image(self, image):
        self.image = image

    def handle_event(self, event):
        pass

    def update(self, elapsed_ms):

        # Update velocity
        self.xVel = self.xVel + (self.xAcc / elapsed_ms)
        self.yVel = self.yVel + (self.yAcc / elapsed_ms)

        # Update position
        self.x = self.xPos + (self.xVel / elapsed_ms)
        self.y = self.yPos + (self.yVel / elapsed_ms)

        # Oppose movement and freeze tiny movements
        deccel_speed = (constants.NORMALDECCEL / elapsed_ms)

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

    # def draw(self, screen):
    #
    #     # Update drawing position to current physics location
    #     self.set_draw_pos(self.xPos, self.yPos)
    #
    #     self.image.blit()

        # Draw the rectangle if enabled
        # if(self.debug_rect):
        #     self.draw_rect(screen)

    # def draw_rect(self, screen):
        # pygame.draw.rect(screen, constants.DEBUGRECTCOLOR, self.rect, 1)
