import pygame
import constants
import math


class Entity(pygame.sprite.Sprite):

    def __init__(self):

        # Call the sprite initializer, but don't set an image
        pygame.sprite.Sprite.__init__(self)
        self.image = None

        # Set initial draw
        self.rect = pygame.Rect(0, 0, 0, 0)

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
        decel_speed = (constants.NORMALDECCEL / elapsed_ms)

        if(abs(self.xVel) > decel_speed):
            if(self.xVel > 0):
                self.xVel -= decel_speed
            else:
                self.xVel += decel_speed
        else:
            self.xVel = 0.0

        if(abs(self.yVel) > decel_speed):
            if(self.yVel > 0):
                self.yVel -= decel_speed
            else:
                self.yVel += decel_speed
        else:
            self.yVel = 0.0

    def undraw(self, screen, background):
        screen.blit(background, self.rect, self.rect)

    def draw(self, screen):

        # Update drawing position to current physics location
        self.set_draw_pos(self.xPos, self.yPos)

        screen.blit(self.image, self.rect)
