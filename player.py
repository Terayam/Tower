import entity
import constants
import pygame
import math


class Player(entity.Entity):

    def __init__(self):

        # Call the base class initializer
        entity.Entity.__init__(self)

        # Initialize state variables
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def handle_event(self, event):

        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_a):
                self.moveLeft = True
            elif(event.key == pygame.K_d):
                self.moveRight = True
            elif(event.key == pygame.K_w):
                self.moveUp = True
            elif(event.key == pygame.K_s):
                self.moveDown = True
            else:
                pass

        if(event.type == pygame.KEYUP):

            if(event.key == pygame.K_a):
                self.moveLeft = False
            elif(event.key == pygame.K_d):
                self.moveRight = False
            elif(event.key == pygame.K_w):
                self.moveUp = False
            elif(event.key == pygame.K_s):
                self.moveDown = False
            else:
                pass

    def update(self, elapsed_ms):

        # accelerate in the direction of movement
        if(self.moveRight):
            self.xAcc = constants.MOVEACCEL
        elif(self.moveLeft):
            self.xAcc = -constants.MOVEACCEL
        else:
            self.xAcc = 0

        if(self.moveDown):
            self.yAcc = constants.MOVEACCEL
        elif(self.moveUp):
            self.yAcc = -constants.MOVEACCEL
        else:
            self.yAcc = 0

        entity.Entity.update(self, elapsed_ms)

        # Cap maximum speed of player
        self.cap_normal_moves_speed()

    def cap_normal_moves_speed(self):

        # Get magnitude of ve,ocity vector
        mag = math.sqrt((self.xVel * self.xVel) + (self.yVel * self.yVel))

        # If magnitude  if greater than max, scale components proportionally
        if(mag > constants.MAXSPEED):
            self.xVel = (constants.MAXSPEED / mag) * self.xVel
            self.yVel = (constants.MAXSPEED / mag) * self.yVel
