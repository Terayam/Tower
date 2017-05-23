import pyglet
import constants
import player
import entity
import rm
import joystick_handler


class Game(pyglet.window.Window):

    def __init__(self, *args, **kwargs):

        # Call the base class initialize
        super(Game, self).__init__(*args, **kwargs)

        self.sprite_batch = pyglet.graphics.Batch()
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

        # Set current level
        # First level is at key 1
        self.current_level = self.levels[1]

        # Create the player object
        self.create_player()

        # Create an enemy to test with
        self.test_enemy = entity.Entity(pyglet.image.load('img/enemy.png'),
                                        batch=self.sprite_batch)

        self.test_enemy.x = 120
        self.test_enemy.y = 320
        self.test_enemy.bbox_to_image()
        self.test_enemy.collidable = True
        self.test_enemy.target = self.player
        self.test_enemy.behave = self.test_enemy.track_target
        self.test_enemy.tracking_gain = 4

    def setup_joystick(self):

        # Load all joysicks
        joysticks = pyglet.input.get_joysticks()

        # If joysticks found, load and open the first one.
        if(joysticks):
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick_handler.set_joystick(self.joystick)

    def create_player(self):

        self.player = player.Player(pyglet.image.load('img/guy.png'),
                                    batch=self.sprite_batch)

    def update(self, dt):

        # Update joystick events
        if(self.joystick):
            self.joystick_handler.update_joystate()

        # Give joystate to Player
        self.player.read_joystate(self.joystick_handler)

        # Call update on all enemies and projectiles
        self.test_enemy.update(dt)

        # Call update on the player
        self.player.update(dt)

        # collide the player with the walls
        for w in self.current_level.walls:
            w.collide(self.player)

        # Collide enemies and enemy projectiles with player projectiles

        # Collide enemies and enemy projectiles with walls

        # Collide the player with enemies and projectiles
        self.test_enemy.collide(self.player)

    def draw_all_entities(self):

        # Draw main sprite group
        self.sprite_batch.draw()

    def on_draw(self):

        # Draw the current level
        self.current_level.draw()

        # Draw bboxes if debug enabled
        if(self.debug_bbox):

            # draw all wall bounding boxes
            for w in self.current_level.walls:
                w.bbox.draw()

            # Draw player bounding boox
            self.player.bbox.draw()

            # Draw bboxes of enemies and projectiles
            self.test_enemy.bbox.draw()

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
