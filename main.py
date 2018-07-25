import pyglet
import player
import rm
import collections
import joystick_handler
import bgmPlayer
import levels

from util import constants

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
        # Graphics initialization
        #########################
        self.sprite_batch = pyglet.graphics.Batch()

        #########################
        # Initialize media player
        #########################
        rm.initialize_media()
        self.bgm = bgmPlayer.BgmPlayer()
        self.bgm.change_source(pyglet.media.load('./sound/sample_song.wav',
                               streaming=False))
        self.bgm.loop(True)
        self.bgm.play()

        ##########################
        # Initialize input methods
        ##########################

        # Initialize key states
        self.keyholdHandler = collections.defaultdict(bool)

        # Check for a joystick
        self.joystick = None
        self.joystick_handler = joystick_handler.Joystick_handler()
        self.setup_joystick()

        ####################
        # Gameplay setup
        ####################

        # Create the player object
        self.create_player()

        # Create game-scope entities
        self.game_entities = []

        # Create the current level
        self.current_level = None

        ########################
        # Debugging stuff
        ########################
        self.debug_bbox = True
        self.current_level = levels.Debug1(self.sprite_batch, self.player)

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

        # Call update on all game-scope entities
        for entity in self.game_entities:
            entity.update(dt)

        # Call update on all level entities
        for entity in self.current_level.entities:
            entity.update(dt)

        # Call update on the player
        self.player.update(dt)

        # Collide level entities with the player
        for entity in self.current_level.entities:
            entity.collide(self.player)

        # Collide enemies and enemy projectiles with player projectiles

        # Collide enemies and enemy projectiles with walls

        # Collide the player with enemies and projec yettiles
        for entity in self.current_level.entities:
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

            # Draw bboxes of game-scope entities
            for entity in self.game_entities:
                entity.bbox.draw()

            # Draw bboxes of level entities
            for entity in self.current_level.entities:
                entity.bbox.draw()

        # Flip is called automatically by the event loop

    def on_key_press(self, symbol, modifiers):

        # Send keypresses to the Game class
        self.handle_key_press(symbol)

        # Send keypresses to the player class
        self.player.handle_key_press(symbol)

        # Send keypresses to the game-scope entities

        # Send keypresses to the level entities

    def on_key_release(self, symbol, modifiers):

        # Sec keypresses to the Game class
        self.handle_key_release(symbol)

        # Send keypresses to the player class
        self.player.handle_key_release(symbol)

        # Send keypresses to the game-scope entities

        # Send keypresses to the level entities

    def handle_key_press(self, symbol):

        # Note:
        #      keyholdHandler is a defaultdict.  If the specified kery has not
        #      yet been registered in the dictionary as a key, it will be
        #      automaticall created in the False held state when it is checked
        #      here.

        # Actions activated on Press
        if(self.keyholdHandler[symbol] is False):

            #########################
            # Specific input handlers
            #########################
            if(symbol == pyglet.window.key.M):

                if(self.bgm.muted is False):
                    self.bgm.mute()

                else:
                    self.bgm.unmute()

        # Actions activated on Held
        else:
            pass

        # Set state to held
        self.keyholdHandler[symbol] = True

    def handle_key_release(self, symbol):

        # Actions activated on release
        if(self.keyholdHandler[symbol] is True):
            pass

        # Actions activated on unheld
        else:
            pass

        # Set state to unheld
        self.keyholdHandler[symbol] = False

    def run(self):

        # Run Pyglet
        pyglet.app.run()


if __name__ == "__main__":
    game = Game(width=640, height=480, vsync=True)
    game.run()
