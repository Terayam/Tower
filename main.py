import pyglet
import constants
import player
import rm


class Game(pyglet.window.Window):

    def __init__(self, *args, **kwargs):

        # Call the base class initialize
        super(Game, self).__init__(*args, **kwargs)

        self.entities = []
        self.levels = {}
        self.current_level = None

        # Load all levels
        self.levels = rm.load_all_levels()

        # create the background image
        self.level_switch(self.levels[1])
    #
    #     # Create the player object
    #     self.create_player()

    def level_switch(self, new_level):

        # create the surface for the background
        self.current_level = new_level

        # Perform the intitial background blit
        self.current_level.draw()
        # self.screen.blit(self.current_level.background, (0, 0))

    # def create_player(self):
    #
    #     self.player = player.Player()
    #
    #     # load a sprite for the player
    #     self.player.set_image(rm.load_image('guy.png'))
    #
    #     # Add the player to the entity list
    #     self.entities.append(self.player)
    #
    # def handle_event(self, event):
    #
    #     if(event.type == pygame.QUIT):
    #         self._running = False
    #
    #     # if the event was a keytype, pass to player
    #     self.player.handle_event(event)

    def undraw_all_entities(self):

        # Call undraw on every object
        for entity in self.entities:
            entity.undraw(self, self.current_level.background)

        # For now, re-draw the entire background
        # self.screen.blit(self.background, (0,0))

    def update(self, dt):

        # Undraw everything before moving them
        self.undraw_all_entities()

        # Call update on every object
        for entity in self.entities:
            entity.update(dt)

    def draw_all_entities(self):

        # Call draw on every object
        for entity in self.entities:
            entity.draw(self.screen)

        # # Flip the display
        # pygame.display.flip()

    def on_draw(self):

        # Draw the current level
        self.current_level.draw()

        # Draw entities
        self.draw_all_entities()

        # Flip is called automatically by the event loop


    def run(self):

        # Run Pyglet
        pyglet.app.run()

        # while(self._running):
        #
        #     for event in pygame.event.get():
        #         self.handle_event(event)
        #
        #     self.undraw()
        #     self.update()
        #     self.draw()
        #
        # self.quit()


if __name__ == "__main__":
    game = Game(width=640, height=480, vsync=True)
    game.run()
