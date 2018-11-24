from ui import ui_element


class Ui_button(ui_element.Ui_element):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Ui_button, self).__init__(*args, **kwargs)

    #####################
    # Behavior functions
    #####################
    def hover(self):
        self.set_clip(1)

    def unhover(self):
        self.set_clip(0)

    def clicked(self, button):
        self.set_clip(2)

    def unclicked(self, button):
        self.set_clip(1)
