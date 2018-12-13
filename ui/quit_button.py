import pyglet
from ui import menu_button


class Quit_button(menu_button.Menu_button):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Quit_button, self).__init__(*args, **kwargs)

    def handle_key_press(self, symbol):

        if((symbol is pyglet.window.key.ENTER) or
           (symbol is pyglet.window.key.NUM_ENTER)):
            self.quit()

    def unclicked(self, button):
        self.quit()

    def quit(self):

        if(self.is_active):
            pyglet.app.exit()
