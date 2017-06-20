import pyglet
import entity
import constants
import util
import rm


class Player(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Player, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Player, self).bbox_to_image()
        self.bbox.color = util.random_color()

        self.collidable = True
        self.collide_latch = False

        # Movement keys
        self.moveLeftDigital = False
        self.moveRightDigital = False
        self.moveUpDigital = False
        self.moveDownDigital = False

        # Initialize state variables
        self.hMove = 0.0
        self.vMove = 0.0

        # Physics constants
        self.coef_friction = constants.NORMALDECCEL

    ###################
    # Sound Functions #
    ###################
    def load_sfx(self):

        # Create a new dictionary of sounds
        sound_dict = {}

        sound_dict['collide'] = rm.load_sfx('./sound/joo.wav')

        return sound_dict

    ####################
    # Inputs Functions #
    ####################

    def handle_key_press(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeftDigital = True
        elif(symbol == pyglet.window.key.D):
            self.moveRightDigital = True
        elif(symbol == pyglet.window.key.W):
            self.moveUpDigital = True
        elif(symbol == pyglet.window.key.S):
            self.moveDownDigital = True

    def handle_key_release(self, symbol):

        if(symbol == pyglet.window.key.A):
            self.moveLeftDigital = False
        elif(symbol == pyglet.window.key.D):
            self.moveRightDigital = False
        elif(symbol == pyglet.window.key.W):
            self.moveUpDigital = False
        elif(symbol == pyglet.window.key.S):
            self.moveDownDigital = False

    def read_joystate(self, joystick_handler):

        temp_hMove = 0.0
        temp_vMove = 0.0

        if(self.moveLeftDigital or joystick_handler.moveLeft):
            temp_hMove = -1.0
        elif(self.moveRightDigital or joystick_handler.moveRight):
            temp_hMove = 1.0
        else:
            temp_hMove = 0.0

        if(self.moveUpDigital or joystick_handler.moveUp):
            temp_vMove = 1.0
        elif(self.moveDownDigital or joystick_handler.moveDown):
            temp_vMove = -1.0
        else:
            temp_vMove = 0.0

        self.hMove = util.biggest([temp_hMove, joystick_handler.x])
        self.vMove = util.biggest([temp_vMove, joystick_handler.y])

    def update(self, elapsed_s):

        # accelerate in the direction of movement
        self.xAcc = constants.MOVEACCEL * self.hMove
        self.yAcc = constants.MOVEACCEL * self.vMove

        super(Player, self).update(elapsed_s)

        # Cap maximum speed of player
        self.cap_normal_move_speed(constants.MAXPLAYERSPEED)

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
