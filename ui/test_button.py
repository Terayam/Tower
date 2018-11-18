from ui import ui_element


class Test_Button(ui_element.Ui_element):

    def __init__(self, *args, **kwargs):
        # Call the base class initializer
        super(Test_Button, self).__init__(*args, **kwargs)

        # Button was clicked
        self.was_clicked = False

    #####################
    # Behavior functions
    #####################
    def hover(self):
        self.set_clip(1)

    def unhover(self):
        self.set_clip(0)

    def clicked(self, button):

        self.was_clicked = True
        self.set_clip(2)

    def unclicked(self, button):

        if(self.was_clicked):
            self.was_clicked = False
            self.set_clip(1)
