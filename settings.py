import pygame

import game_functions as gf
class Settings(object):
    def __init__(self, height, width, players):
        self.screensize = (height, width)
        self.fullscreen = False
        self.players = players
        self.bg_color = (000, 100, 100)
