from ui import ui_element


class Menu_button(ui_element.Ui_element):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Menu_button, self).__init__(*args, **kwargs)

    #####################
    # Behavior functions
    #####################
    def hover(self):
        super(Menu_button, self).hover()
        self.set_clip(1)

    def unhover(self):
        super(Menu_button, self).unhover()
        self.set_clip(0)

    def clicked(self, button):
        self.set_clip(2)

    def unclicked(self, button):
        self.set_clip(1)
