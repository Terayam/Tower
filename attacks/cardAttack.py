from util import constants
from primitives import entity


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

        self.aliveTimer = 0
        self.lifetime = 2.0

    ###########################
    # State Machine Functions #
    ###########################
    def setup_stateMachine(self):

        state_behaviors = {'default': self.stick_target}

        return state_behaviors

    def update_stateMachine(self, elapsed_s):

        self.aliveTimer += elapsed_s

        if(self.aliveTimer >= self.lifetime):
            self.current_state = 'delete'

    def setup_state_animations(self):

        animation_sequences = {'default': [0, 1, 2, 3]}

        return animation_sequences
