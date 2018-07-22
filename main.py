import pyglet
import constants
import player
import rm
import joystick_handler
import bgmPlayer
import levels


class Game(pyglet.window.Window):

    def __init__(self, *args, **kwargs):

        # Call the base class initialize
        super(Game, self).__init__(*args, **kwargs)

        ##############
        # Engine Setup
        ##############

        # Scehdule the update function
        pyglet.clock.schedule_interval(self.update,
                                       1 / constants.FRAMELIMIT_FPS)

        #####################
        # State Machine Setup
        #####################
        self.state = 'init'

        #########################
        # Initialize media player
        #########################
        rm.initialize_media()
        self.bgm = bgmPlayer.BgmPlayer()
        self.bgm.change_source(pyglet.media.load('./sound/sample_song.wav',
                               streaming=False))
        self.bgm.loop(True)
        self.bgm.play()

        self.sprite_batch = pyglet.graphics.Batch()
        self.current_level = None

        ##########################
        # Initialize input methods
        ##########################

        # Check for a joystick
        self.joystick = None
        self.joystick_handler = joystick_handler.Joystick_handler()
        self.setup_joystick()

        ####################
        # Load initial level
        ####################
        self.entities = []
        self.current_level = None

        # Set current level
        self.current_level = levels.Debug1(self.sprite_batch)

        # Get entities from level
        self.entities.extend(self.current_level.entities)

        # Create the player object
        self.create_player()

        ########################
        # Debugging stuff
        ########################
        self.debug_bbox = True

        # Create an enemy to test with
        self.entities[3].target = self.player

    def setup_joystick(self):

        # Load all joysicks
        joysticks = pyglet.input.get_joysticks()

        # If joysticks found, load and open the first one.
        if(joysticks):
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick_handler.set_joystick(self.joystick)

    def create_player(self):

        self.player = player.Player('img/guy.png',
                                    gridX=10,
                                    gridY=10,
                                    batch=self.sprite_batch)

    def update(self, dt):

        # Update joystick events
        if(self.joystick):
            self.joystick_handler.update_joystate()

        # Give joystate to Player
        self.player.read_joystate(self.joystick_handler)

        # Call update on all enemies and projectiles
        for entity in self.entities:
            entity.update(dt)

        # Call update on the player
        self.player.update(dt)

        # Collide entities with the player
        for entity in self.entities:
            entity.collide(self.player)

        # Collide enemies and enemy projectiles with player projectiles

        # Collide enemies and enemy projectiles with walls

        # Collide the player with enemies and projectiles
        for entity in self.entities:
            self.player.collide(entity)

    def draw_all_entities(self):

        # Draw main sprite group
        self.sprite_batch.draw()

    def on_draw(self):

        # Draw the current level
        self.current_level.draw()

        # Draw entities
        self.draw_all_entities()

        # Draw bboxes if debug enabled
        if(self.debug_bbox):

            # Draw player bounding boox
            self.player.bbox.draw()

            # Draw bboxes of enemies and projectiles
            for entity in self.entities:
                entity.bbox.draw()

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
