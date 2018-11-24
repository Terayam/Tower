class Ui_handler():

    def __init__(self):

        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def update(self, dt):
        for element in self.elements:
            element.update(dt)

    def distribute_key_press(self, symbol):

        # If nothing is active, set the first element to active_element
        found_active = False
        for element in self.elements:

            if(element.active_element):
                found_active = True
                break

        if(found_active is False):
            self.elements[0].active_element = True

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
