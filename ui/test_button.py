from ui import ui_element


class Test_Button(ui_element.Ui_element):

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
