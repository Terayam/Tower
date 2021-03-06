import pyglet
import collections
import math
import rm

from primitives import entity
from util import util_functions
from util import constants


class Player(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Player, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Player, self).bbox_to_image()
        self.bbox.color = util_functions.random_color()

        self.collidable = True
        self.collide_latch = False

        # Initialize key states
        self.movementButtons = collections.defaultdict(bool)

        # Initialize state variables
        self.hMove = 0.0
        self.vMove = 0.0

        # Physics constants
        self.coef_friction = constants.NORMALDECCEL
        self.idle_speed = constants.MINSPEED

        # Drawing variables

    ###################
    # Sound Functions #
    ###################
    def load_sfx(self):

        # Create a new dictionary of sounds
        sound_dict = {}

        sound_dict['collide'] = rm.load_sfx('assets/sound/joo.wav')

        return sound_dict

    ###########################
    # State Machine Functions #
    ###########################
    def setup_stateMachine(self):

        state_behaviors = {'idle': self.behave_idle,
                           'move': self.behave_move}

        return state_behaviors

    def setup_state_animations(self):

        animation_sequences = {'idle': [0],
                               'move': [10, 11, 12, 13]}

        return animation_sequences

    def update_stateMachine(self, elapsed_s):

        # Switch between moving and idle states
        self.current_state = 'idle'

        velMag = math.sqrt(self.xVel * self.xVel + self.yVel * self.yVel)

        if(velMag > self.idle_speed):
            self.current_state = 'move'

    ####################
    # Inputs Functions #
    ####################

    def handle_key_press(self, symbol):

        # Set key to held
        self.movementButtons[symbol] = True

    def handle_key_release(self, symbol):

        # Set key to unheld
        self.movementButtons[symbol] = False

    def read_joystate(self, joystick_handler):

        temp_hMove = 0.0
        temp_vMove = 0.0

        if(self.movementButtons[pyglet.window.key.A] or
           joystick_handler.moveLeft):
            temp_hMove = -1.0
        elif(self.movementButtons[pyglet.window.key.D] or
             joystick_handler.moveRight):
            temp_hMove = 1.0
        else:
            temp_hMove = 0.0

        if(self.movementButtons[pyglet.window.key.W] or
           joystick_handler.moveUp):
            temp_vMove = 1.0
        elif(self.movementButtons[pyglet.window.key.S] or
             joystick_handler.moveDown):
            temp_vMove = -1.0
        else:
            temp_vMove = 0.0

        self.hMove = util_functions.biggest([temp_hMove, joystick_handler.x])
        self.vMove = util_functions.biggest([temp_vMove, joystick_handler.y])

    def update(self, elapsed_s):

        # accelerate in the direction of movement
        self.xAcc = constants.MOVEACCEL * self.hMove
        self.yAcc = constants.MOVEACCEL * self.vMove

        super(Player, self).update(elapsed_s)

        # Cap maximum speed of player
        self.cap_normal_move_speed(constants.MAXPLAYERSPEED)

    #####################
    # Behavior functions
    #####################
    def behave_idle(self, elapsed_s):

        # Reset animation
        self.animation_fps = 0

    def behave_move(self, elapsed_s):

        velMag = math.sqrt(self.xVel * self.xVel + self.yVel * self.yVel)
        self.animation_fps = (24 * (velMag / constants.MAXPLAYERSPEED))

    ################################
    # Collision Response functions #
    ################################
    def collide(self, other):

        # Don't collide if either sprite is not collidable
        if(self.collidable and other.collidable):

            # Get the rectangle overlap
            overlap = self.bbox.union(other.bbox)

            if(overlap and self.debug_overlap):
                overlap.color = (255, 0, 0, 255)
                overlap.draw()

            if(overlap):

                # Call the collide with player function
                # of the other sprite with this sprite
                other.collide_with_player(overlap)

    def collide_with_wall(self, player, overlap):
        self.exit_collision(overlap)

        if(not self.collide_latch):
            self.sound_dict['collide'].play()
            self.collide_latch = True
