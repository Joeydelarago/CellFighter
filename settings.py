import pygame


class Settings(object):
    """ Holds the values for all settings in the game. Also hold the list of
        current players, possible resolutions and living players.

        Arguments:
            height (int): Height of the screen in pixels.
            width (int): Width of the screen in pixels.
        Attributes:
            fullscreen (bool): Is the screen fullscreened.
            bg_pointer (int): Points to the current background.
            backgrounds (list of str): List of all background locations.
            font (str): Location of font.
            players (list): List of active players.
            state (str): Which state the game is currently in, ie menu etc.
            volume (int): Game volume.
            resolution (lambda): Returns the current resolution for the game.
            resolutions (list of tuple): List of all valid resolutions.
            respointer (int): Current resolution of the game.
            arena_x (int): The x coordinate of the top left of the arena.
            arena_dimension (int): The arena width and height.
            living_players () ? @Sam
    """
    def __init__(self, height, width):
        self.screensize = (width, height)
        self.default_res = None
        self.fullscreen = True
        self.bg_pointer = 0
        self.background = lambda: self.backgrounds[self.bg_pointer]
        self.backgrounds = ['assets/arena1.png', 'assets/arena2.png',
                            'assets/arena3.png', 'assets/arena4.png',
                            'assets/arena5.png']
        self.font = "assets/fonts/ShareTechMono-Regular.ttf"
        self.players = []
        self.state = "main"
        self.volume = 10
        self.resolution = lambda: self.resolutions[self.respointer]
        self.resolutions = [(800, 600), (1024, 768), (1280, 768),
                            (1280, 1024), (1366, 768), (1600, 900),
                            (1920, 980), (1920, 1080)]
        self.respointer = None
        self.arena_x = (width-height)//2
        self.arena_dimension = height
        self.living_players = 0

    def add_player(self, player):
        self.players.append(player)
        self.living_players += 1

    def change_background(self):
        self.bg_pointer = (self.bg_pointer + 1) % (len(self.backgrounds) - 1)
