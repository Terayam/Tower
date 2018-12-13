import pyglet
from ui import menu_button


class Quit_button(menu_button.Menu_button):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Quit_button, self).__init__(*args, **kwargs)

        # Keyboard reaction matrix
        self.keypress_reaction = {pyglet.window.key.ENTER: self.quit,
                                  pyglet.window.key.NUM_ENTER: self.quit}

    def unclicked(self, button):

        self.set_clip(1)

        # Quit the game
        self.quit()

    def quit(self):
        if(self.is_active):
            pyglet.app.exit()
