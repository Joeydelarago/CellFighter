import pygame

import game_functions as gf
class Settings(object):
    def __init__(self, height, width, players):
        self.screensize = (width, height)
        self.fullscreen = False
        self.bg_color = (000, 100, 100)
