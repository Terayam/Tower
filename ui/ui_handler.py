import pyglet


class Ui_handler():

    def __init__(self):

        self.keypress_response = {pyglet.window.key.W: self.menu_up,
                                  pyglet.window.key.D: self.menu_right,
                                  pyglet.window.key.S: self.menu_down,
                                  pyglet.window.key.A: self.menu_left,

                                  pyglet.window.key.UP: self.menu_up,
                                  pyglet.window.key.RIGHT: self.menu_right,
                                  pyglet.window.key.DOWN: self.menu_down,
                                  pyglet.window.key.LEFT: self.menu_left}

        self.elements = []
        self.active_element = None

    def add(self, element):

        self.elements = self.elements + element

        if(self.active_element is None):
            self.active_element = self.elements[0]
            self.active_element.is_active = True

    def update(self, dt):
        for element in self.elements:
            element.update(dt)

    # Key press reaction functions
    def menu_up(self):
        self.switch_node(0)

    def menu_right(self):
        self.switch_node(1)

    def menu_down(self):
        self.switch_node(2)

    def menu_left(self):
        self.switch_node(3)

    def switch_node(self, node_num):

        if(self.active_element.connection_nodes[node_num] is not None):

            destination_node = self.active_element.connection_nodes[node_num]

            self.active_element.is_active = False
            self.active_element = destination_node
            self.active_element.is_active = True

    def distribute_key_press(self, symbol):

        # Do any keypresses that this class is supposed to respond to
        if(symbol in self.keypress_response):
            self.keypress_response[symbol]()

        for element in self.elements:
            element.handle_key_press(symbol)

    def distribute_key_release(self, symbol):
        for element in self.elements:
            element.handle_key_release(symbol)

    def distribute_mouse_move(self, x, y):
        for element in self.elements:
            element.handle_mouse_move(x, y)

    def distribute_mouse_click(self, x, y, button):

        for element in self.elements:
            element.handle_click(x, y, button)

    def distribute_mouse_release(self, x, y, button):

        for element in self.elements:
            element.handle_release(x, y, button)
