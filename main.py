import pyglet
import player
import rm
import collections
import levels

from input_handling import joystick_handler
from ui import test_button
from ui import ui_handler
from sound import bgmPlayer
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
        self.stateUpdateFunctions = {'run': self.updateRun,
                                     'pause': self.updatePause}

        #########################
        # Graphics initialization
        #########################
        self.sprite_batch_game = pyglet.graphics.Batch()
        self.sprite_batch_ui = pyglet.graphics.Batch()
        self.pause_batch_ui = pyglet.graphics.Batch()

        #########################
        # Initialize media player
        #########################
        rm.initialize_media()

        # Load music file to play
        bgmMusic = pyglet.media.load('assets/sound/sample_song.wav',
                                     streaming=False)

        # Create bgmplayer and set it up
        self.bgm = bgmPlayer.BgmPlayer()
        self.bgm.change_source(bgmMusic)
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
        self.current_level = levels.Debug1(self.sprite_batch_game,
                                           self.player)

        # Create a new ui button to interact with
        tb = test_button.Test_Button('assets/img/TestButton.png',
                                     gridX=1,
                                     gridY=3,
                                     batch=self.sprite_batch_ui)

        tb.x = 250
        tb.y = 25

        self.ui_handler = ui_handler.Ui_handler()
        self.ui_handler.add(tb)

        # Create a pause button to work with
        # Create a new ui button to interact with
        pb = test_button.Test_Button('assets/img/TestButton.png',
                                     gridX=1,
                                     gridY=3,
                                     batch=self.pause_batch_ui)

        pb.x = 400
        pb.y = 0

        self.pause_ui_handler = ui_handler.Ui_handler()
        self.pause_ui_handler.add(pb)

    def setup_joystick(self):

        # Load all joysicks
        joysticks = pyglet.input.get_joysticks()

        # If joysticks found, load and open the first one.
        if(joysticks):
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick_handler.set_joystick(self.joystick)

    def create_player(self):

        self.player = player.Player('assets/img/guy.png',
                                    gridX=10,
                                    gridY=10,
                                    batch=self.sprite_batch_game)

    def on_draw(self):

        # Draw the current level
        self.current_level.draw()

        # Draw entities
        self.draw_all_entities()

        # If in the paused state, draw GUI
        if(self.state == 'pause'):
            self.draw_pause_screen()

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

    def draw_all_entities(self):

        # Draw game entities first
        self.sprite_batch_game.draw()

        # Draw UI on top
        self.sprite_batch_ui.draw()

    def draw_pause_screen(self):
        self.pause_batch_ui.draw()

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

            if(symbol == pyglet.window.key.ESCAPE):

                if(self.state == 'pause'):
                    self.state = 'run'

                else:
                    self.state = 'pause'

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

    def on_mouse_motion(self, x, y, dx, dy):

        if(self.state == 'pause'):
            self.pause_ui_handler.distribute_mouse_move(x, y)

        else:
            self.ui_handler.distribute_mouse_move(x, y)

    def on_mouse_press(self, x, y, button, modifiers):

        # Actions activated on Press
        if(self.keyholdHandler[button] is False):

            if(self.state == 'pause'):
                self.pause_ui_handler.distribute_mouse_click(x, y, button)

            else:
                self.ui_handler.distribute_mouse_click(x, y, button)

        # Actions for held
        else:
            pass

        # Set state to held
        self.keyholdHandler[button] = True

    def on_mouse_release(self, x, y, button, modifiers):

        # Actions activated on release
        if(self.keyholdHandler[button] is True):

            if(self.state == 'pause'):
                self.pause_ui_handler.distribute_mouse_release(x, y, button)

            else:
                self.ui_handler.distribute_mouse_release(x, y, button)

        # Actions activated on unheld
        else:
            pass

        # Set state to unheld
        self.keyholdHandler[button] = False

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    ###########################################################################
    # Update functions
    ###########################################################################
    def update(self, dt):

        # Call update function of current state
        self.stateUpdateFunctions[self.state](dt)

    def updateRun(self, dt):
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

    def updatePause(self, dt):
        # Update joystick events
        if(self.joystick):
            self.joystick_handler.update_joystate()

        # Call update on all pause GUI Elements

    def run(self):

        # Set statemachine to running
        self.state = 'run'

        # Run Pyglet
        pyglet.app.run()


if __name__ == "__main__":
    game = Game(width=640, height=480, vsync=True)
    game.run()
