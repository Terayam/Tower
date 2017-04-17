import pygame
import constants
import math


class Entity(pygame.sprite.Sprite):

    def __init__(self):

        # Call the sprite initializer, but don't set an image
        pygame.sprite.Sprite.__init__(self)
        self.image = None

        ########################
        # Debugging Parameters #
        ########################
        self.debug_rect = True

        ######################
        # Drawing parameters #
        ######################

        # Set initial draw position
        self.rect = pygame.Rect(0, 0, 0, 0)

        ######################
        # Physics Parameters #
        ######################

        # Set initial physics position
        self.xPos = 0.0
        self.yPos = 0.0

        # Set initial velocity
        self.xVel = 0.0
        self.yVel = 0.0

        # Set initial acceleration
        self.xAcc = 0.0
        self.yAcc = 0.0

    def set_draw_pos(self, xPos, yPos):
        # Move drawing rectangle to current physics point
        self.rect.x = math.floor(self.xPos)
        self.rect.y = math.floor(self.yPos)

    def set_image(self, image):
        self.image = image
        self.rect = image.get_rect()

    def handle_event(self, event):
        pass

    def update(self, elapsed_ms):

        # Update velocity
        self.xVel = self.xVel + (self.xAcc / elapsed_ms)
        self.yVel = self.yVel + (self.yAcc / elapsed_ms)

        # Update position
        self.xPos = self.xPos + (self.xVel / elapsed_ms)
        self.yPos = self.yPos + (self.yVel / elapsed_ms)

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

    def draw(self, screen):

        # Update drawing position to current physics location
        self.set_draw_pos(self.xPos, self.yPos)

        screen.blit(self.image, self.rect)

        # Draw the rectangle if enabled
        if(self.draw_rect):
            self.draw_rect(screen)

    def draw_rect(self, screen):
        pygame.draw.rect(screen, constants.DEBUGRECTCOLOR, self.rect, 1)
