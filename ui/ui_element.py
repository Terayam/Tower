import collections
from primitives import entity


class Ui_element(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Ui_element, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Ui_element, self).bbox_to_image()

        # Current mouse state
        self.mouse_x = 0
        self.mouse_y = 0
        self.is_active = False
        self.was_clicked = False
        self.was_released = False
        self.mouse_buttons = collections.defaultdict(bool)

        # Keyboard reaction matrix
        self.keypress_reaction = {}
        self.key_release_reaction = {}

        # UI connected nodes
        self.connection_nodes = [None,  # Up
                                 None,  # Right
                                 None,  # Down
                                 None]  # Left

    def update_mouse(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    def update(self, elapsed_s):

        # If this element is the active element, set to hovered
        if(self.is_active):
            self.hover()

        # Change to the hover state if the mouse is in the bounding box
        if(self.point_inside(self.mouse_x, self.mouse_y)):

            if(self.was_clicked):
                self.clicked(self.mouse_buttons)

            elif(self.was_released):
                self.was_released = False
                self.unclicked(self.mouse_buttons)

            elif(not self.is_active):
                self.hover()

        else:

            # If the mouse was clicked, but is now outside the button without
            # being released, clear the clicked state without calling the
            # clicked or released action
            if(self.was_clicked):
                self.was_clicked = False

            if(not self.is_active):
                self.unhover()

    def handle_key_press(self, symbol):
        if(symbol in self.keypress_reaction):
            self.keypress_reaction[symbol]()

    def handle_key_release(self, symbol):
        if(symbol in self.key_release_reaction):
            self.keypress_reaction[symbol]()

    def handle_mouse_move(self, x, y):
        self.update_mouse(x, y)

    def handle_click(self, x, y, button):

        self.update_mouse(x, y)
        self.mouse_buttons[button] = True

        # Perform click action if the click happened within the bounding box
        if(self.point_inside(self.mouse_x, self.mouse_y)):

            self.was_clicked = True

    def handle_release(self, x, y, button):

        self.update_mouse(x, y)
        self.mouse_buttons[button] = False

        if(self.was_clicked):

            self.was_clicked = False

            if(self.point_inside(self.mouse_x, self.mouse_y)):
                self.was_released = True

    def connect(self, up=None, right=None, down=None, left=None):
        self.connection_nodes[0] = up
        self.connection_nodes[1] = right
        self.connection_nodes[2] = down
        self.connection_nodes[3] = left

    #####################
    # Behavior functions
    #####################
    def hover(self):
        pass

    def unhover(self):
        pass

    def clicked(self, button):
        pass

    def unclicked(self, button):
        pass
