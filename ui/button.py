from primitives import entity


class Button(entity.Entity):

    def update(self, elapsed_s):
        pass

    ###########################
    # State Machine Functions #
    ###########################
    def setup_stateMachine(self):

        state_behaviors = {'idle': self.behave_idle,
                           'hover': self.behave_hover,
                           'click': self.behave_click}

        return state_behaviors

    def update_stateMachine(self, elapsed_s):

        # Idle is default state
        self.current_state = 'idle'

        # Change to hover state if hovered
        if(False):

            # Change to Clicked state if hovered and Clicked
            if(False):
                pass

    #####################
    # Behavior functions
    #####################
    def behave_idle(self, elapsed_s):
        pass

    def behave_hover(self, elapsed_s):
        pass

    def behave_click(self, elapsed_s):
        pass
