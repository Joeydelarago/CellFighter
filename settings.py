import pygame


class Settings(object):
    def __init__(self, height, width):
        self.screensize = (width, height)
        self.default_res = None
        self.fullscreen = True
        self.bg_color = (000, 100, 100)
        self.players = []
        self.state = "main"
        self.volume = 10
        self.resolution = lambda : self.resolutions[self.respointer]
        self.resolutions = [(800, 600), (1024, 768), (1280, 768),
                            (1280, 1024), (1366, 768), (1600, 900),
                            (1920, 980), (1920, 1080)]
        self.respointer = None

    def add_player(self, player):
        self.players.append(player)

