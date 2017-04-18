import pygame
import constants
import player
import rm


class Game:

    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 480
        self.entities = []
        self.levels = {}
        self.current_level = None
        self.mainClock = pygame.time.Clock()

    def initialize(self):

        # Initialze pygame and the screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._running = True

        # Load all levels
        self.levels = rm.load_all_levels()

        # create the background image
        self.level_switch(self.levels[1])

        # Create the player object
        self.create_player()

    def level_switch(self, new_level):

        # create the surface for the background
        self.current_level = new_level

        # Perform the intitial background blit
        self.screen.blit(self.current_level.background, (0, 0))

    def create_player(self):

        self.player = player.Player()

        # load a sprite for the player
        self.player.set_image(rm.load_image('guy.png'))

        # Add the player to the entity list
        self.entities.append(self.player)

    def handle_event(self, event):

        if(event.type == pygame.QUIT):
            self._running = False

        # if the event was a keytype, pass to player
        self.player.handle_event(event)

    def update(self):

        # Get the time since the last update
        elapsed_ms = self.mainClock.tick(constants.FRAMELIMIT_FPS)

        # Call update on every object
        for entity in self.entities:
            entity.update(elapsed_ms)

    def undraw(self):

        # Call undraw on every object
        for entity in self.entities:
            entity.undraw(self.screen, self.current_level.background)

        # For now, re-draw the entire background
        # self.screen.blit(self.background, (0,0))

    def draw(self):

        # Call draw on every object
        for entity in self.entities:
            entity.draw(self.screen)

        # Flip the display
        pygame.display.flip()

    def quit(self):
        pygame.quit()

    def run(self):

        if(self.initialize() is False):
            self._running = False

        while(self._running):

            for event in pygame.event.get():
                self.handle_event(event)

            self.undraw()
            self.update()
            self.draw()

        self.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
