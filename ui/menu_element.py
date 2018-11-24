from ui import ui_element
import pyglet


class Menu_element(ui_element.Ui_element):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Menu_element, self).__init__(*args, **kwargs)

        # Fill out keypress reaction menu
        self.keypress_reaction = {pyglet.window.key.W: self.menu_up,
                                  pyglet.window.key.D: self.menu_right,
                                  pyglet.window.key.S: self.menu_down,
                                  pyglet.window.key.A: self.menu_left}

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

        if(self.connection_nodes[node_num] is not None):
            self.active_element = False
            self.connection_nodes[node_num].active_element = True
