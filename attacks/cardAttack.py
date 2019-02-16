from util import constants
from util import util_functions
from primitives import entity
import math


class CardAttack(entity.Entity):

    def __init__(self, batch, x, y):

        # Call the base class initializer
        super(CardAttack, self).__init__('assets/img/card_attack.png',
                                         gridX=10,
                                         gridY=10,
                                         batch=batch)

        self.bbox_to_image()
        self.collidable = True

        entity.Entity()

        self.animation_style = constants.ANIMATE_ONCE

        self.x = x
        self.y = y

        self.stick_offset_x = 20.0
        self.stick_offset_y = 25.0
        self.stick_offset_animation = [(0.00, 00.0, 50.0),
                                       (0.15, 50.0, 25.0),
                                       (0.20, 45.0, 00.0),
                                       (0.30, 45.0, 00.0),
                                       (0.55, 35.0, 00.0),
                                       (2.00, 35.0, 00.0)]

        self.aliveTimer = 0
        self.lifetime = 2.0

    ###########################
    # State Machine Functions #
    ###########################
    def setup_stateMachine(self):

        state_behaviors = {'default': self.stick_target}

        return state_behaviors

    def setup_state_animations(self):

        animation_sequences = {'default': [0, 1, 2, 3]}

        return animation_sequences

    def update(self, elapsed_s):

        self.aliveTimer += elapsed_s

        if(self.aliveTimer >= self.lifetime):
            self.current_state = 'delete'

        new_stick_offset = util_functions.linear_interp_tuple_list(self.stick_offset_animation,
                                                                   self.aliveTimer)
        self.stick_offset_x = new_stick_offset[0]
        self.stick_offset_y = new_stick_offset[1]

        print("{}: {}, {}".format(self.aliveTimer,
                                  self.stick_offset_x,
                                  self.stick_offset_y))

        super(CardAttack, self).update(elapsed_s)
