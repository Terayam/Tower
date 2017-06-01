import math
import pyglet
import constants
import rect
import util


class Entity(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):

        # Call the sprite initializer, but don't set an image
        super(Entity, self).__init__(*args, **kwargs)

        ######################
        # Physics Parameters #
        ######################
        self.subpixel = True
        self.collidable = False

        # Set initial physics position
        self.bbox = rect.Rect()

        # Set initial velocity
        self.xVel = 0.0
        self.yVel = 0.0

        # Set initial acceleration
        self.xAcc = 0.0
        self.yAcc = 0.0

        ###############################
        # Default Behavior Parameters #
        ###############################
        self.tracking_gain = 1.0

        ######################
        # Drawing parameters #
        ######################
        self.bbox.color = util.random_color()

        ########################
        # Debugging Parameters #
        ########################
        self.debug_overlap = True

    #####################
    # Drawing functions #
    #####################
    def set_image(self, image):
        self.image = image

    def bbox_to_image(self):
        self.bbox.w = self.width
        self.bbox.h = self.height

    def undraw(self, screen, background):
        screen.blit(background, self.rect, self.rect)

    #####################
    # Physics functions #
    #####################
    def update(self, elapsed_s):

        # Perform automated behaviors
        self.behave(elapsed_s)

        # Update velocity
        self.xVel = self.xVel + (self.xAcc * elapsed_s)
        self.yVel = self.yVel + (self.yAcc * elapsed_s)

        # Update position
        self.x = self.x + (self.xVel * elapsed_s)
        self.y = self.y + (self.yVel * elapsed_s)

        # Update bbox position since we moved normal X position
        self.update_bbox()

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

        #print('deccel: {0}'.format(deccel_speed))

    def update_bbox(self):

        # Update bbox position
        self.bbox.x = self.x
        self.bbox.y = self.y

    def cap_normal_move_speed(self, max_speed):

        if(self.xVel > max_speed):
            self.xVel = max_speed
        elif(self.xVel < -max_speed):
            self.xVel = -max_speed

        if(self.yVel > max_speed):
            self.yVel = max_speed
        elif(self.yVel < -max_speed):
            self.yVel = -max_speed

    #######################
    # Collision functions #
    #######################
    def collide(self, other):

        # Don't collide if either sprite is not collidable
        if(self.collidable and other.collidable):

            # Get the rectangle overlap
            overlap = self.bbox.union(other.bbox)

            if(overlap and self.debug_overlap):
                overlap.color = (255, 0, 0, 255)
                overlap.draw()

        # Base class doesn't do anything with the collision

    def collide_with_player(self, overlap):
        pass

    def collide_with_wall(self, overlap):
        pass

    def collide_with_enemy(self, overlap):
        pass

    def exit_collision(self, overlap):

        # Self moves coresponding to the overlap

        # Primarily a Horizontal overlap
        if(overlap.h > overlap.w):

            # Overlap is left, move right
            if(overlap.x > self.x):
                self.x = self.x - overlap.w

            # Overlap is right, move left
            else:
                self.x = overlap.right()

            # Stop X movement
            self.xVel = 0.0
            self.xAcc = 0.0

        # Primarily a Vertical overlap
        else:

            # Overlap is below, move up
            if(overlap.y > self.y):
                self.y = self.y - overlap.h

            # Overlap is above, move down
            else:
                self.y = overlap.top()

            # Stop Y movement
            self.yVel = 0.0
            self.yAcc = 0.0

        # Update bbox position since we moved normal X position
        self.update_bbox()

    ######################
    # Behavior Functions #
    ######################
    def behave(self, elapsed_s):
        pass

    def track_target(self, elapsed_s):

        # Don't do anything if I don't have a target
        # (Target is expected to be an entity)
        if(self.target):

            # Find the vector towards the target
            dx = self.target.x - self.x
            dy = self.target.y - self.y

            # Normalize magnitude so only using direction
            mag = math.sqrt((dx * dx) + (dy * dy))

            # Don't update accelerations if magnitude is zero
            if(abs(mag) > 0):
                dx = dx / mag
                dy = dy / mag

                # Apply a gain to accelerate
                self.xAcc = dx * self.tracking_gain
                self.yAcc = dy * self.tracking_gain
