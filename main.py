import pyglet
import constants
import player
import rm
import joystick_handler
import wall
import util


class Game(pyglet.window.Window):

    def __init__(self, *args, **kwargs):

        # Call the base class initialize
        super(Game, self).__init__(*args, **kwargs)

        self.sprite_batch = pyglet.graphics.Batch()
        self.entities = []
        self.levels = {}
        self.current_level = None

        ########################
        # Debugging Parameters #
        ########################
        self.debug_bbox = True

        # Check for a joystick
        self.joystick = None
        self.joystick_handler = joystick_handler.Joystick_handler()
        self.setup_joystick()

        # Scehdule the update function
        pyglet.clock.schedule_interval(self.update,
                                       1 / constants.FRAMELIMIT_FPS)

        # Load all levels
        self.levels = rm.load_all_levels()

        # create the background image
        self.level_switch(self.levels[1])

        # Create the player object
        self.create_player()

        # Create a rectangle to test collisions width
        pattern = pyglet.image.SolidColorImagePattern(color=(0, 0, 0, 0))
        wallimage = pattern.create_image(1, 1)
        self.test_rect = wall.Wall(wallimage)
        self.test_rect.x = 150
        self.test_rect.y = 250
        self.test_rect.bbox.x = 150
        self.test_rect.bbox.y = 250
        self.test_rect.bbox.w = 100
        self.test_rect.bbox.h = 120
        self.test_rect.bbox.color = util.random_color()
        self.entities.append(self.test_rect)

    def setup_joystick(self):

        # Load all joysicks
        joysticks = pyglet.input.get_joysticks()

        # If joysticks found, load and open the first one.
        if(joysticks):
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick_handler.set_joystick(self.joystick)

    def level_switch(self, new_level):

        # create the surface for the background
        self.current_level = new_level

        # Perform the intitial background blit
        self.current_level.draw()
        # self.screen.blit(self.current_level.background, (0, 0))

    def create_player(self):

        self.player = player.Player(pyglet.image.load('img/guy.png'),
                                    batch=self.sprite_batch)

        # Add the player to the entity list
        self.entities.append(self.player)

    def update(self, dt):

        # Update joystick events
        if(self.joystick):
            self.joystick_handler.update_joystate()

        # Give joystate to Player
        self.player.read_joystate(self.joystick_handler)

        # Call update on every object
        for ent in self.entities:
            ent.update(dt)

        # collide the player with the test rectangle
        self.player.collide(self.test_rect)

    def draw_all_entities(self):

        # Draw main sprite group
        self.sprite_batch.draw()

    def on_draw(self):

        # Draw the current level
        self.current_level.draw()

        # Draw bboxes if debug enabled
        if(self.debug_bbox):
            for ent in self.entities:
                ent.bbox.draw()

        # Draw entities
        self.draw_all_entities()

        # Flip is called automatically by the event loop

    def on_key_press(self, symbol, modifiers):

        # Send keypresses onto the player class
        self.player.handle_key_press(symbol)

    def on_key_release(self, symbol, modifiers):

        # Send keypresses onto the player class
        self.player.handle_key_release(symbol)

    def run(self):

        # Run Pyglet
        pyglet.app.run()


if __name__ == "__main__":
    game = Game(width=640, height=480, vsync=True)
    game.run()
