from primitives import entity


class Ui_element(entity.Entity):

    def __init__(self, *args, **kwargs):

        # Call the base class initializer
        super(Ui_element, self).__init__(*args, **kwargs)

        # default bbox to image
        super(Ui_element, self).bbox_to_image()

    def update(self, elapsed_s):
        pass

    def handle_mouse_move(self, x, y):

        # Change to the hover state if the mouse is in the bounding box
        if(self.point_inside(x, y)):
            self.hover()

        else:
            self.unhover()

    def handle_click(self, x, y, button):

        # Perform click action if the click happened within the bounding box
        if(self.point_inside(x, y)):
            self.clicked(button)

    def handle_release(self, x, y, button):

        self.unclicked(button)

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
