import entity


class Debt(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Debt, self).__init__(*args, **kwargs)

        self.bbox_to_image()
        self.collidable = True

        self.x = 120
        self.y = 320
        self.coef_friction = 100

        # Set up tracking
        self.tracking_accel = 600
        self.min_tracking_distance = 5
        self.max_tracking_distance = 150

    ###########################
    # State Machine Functions #
    ###########################
    def setup_stateMachine(self):

        state_behaviors = {}
        state_behaviors['default'] = self.track_target
        state_behaviors['collided'] = self.after_collision

        return state_behaviors

    def after_collision(self, elapsed_s):

        self.xAcc = 0
        self.yAcc = 0
        self.xVel = 10
        self.yVel = 10

    #######################
    # Collision functions #
    #######################
    def collide_with_player(self, overlap):
        self.current_state = 'collided'

        self.xAcc /= 2
        self.yAcc /= 2
        self.xVel /= 2
        self.yVel /= 2
