import pygame

import game_functions as gf
class Settings(object):
    def __init__(self, height, width):
        self.screensize = (width, height)
        self.fullscreen = False
        self.bg_color = (000, 100, 100)
        self.players = []
        self.state = "main" #main/game/pause/gameover
        self.volume = 10

    def add_player(self, player):
        self.players.append(player)

