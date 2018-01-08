import pygame

import game_functions as gf
class Settings(object):
    def __init__(self, height, width):
        self.screensize = (width, height)
        self.fullscreen = False
        self.bg_color = (000, 100, 100)
        self.keyboardPlayer = None
        self.joystickPlayers = []
        self.state = "main" #main/game/pause/gameover
        self.volume = 10

    def addKeyboardPlayer(self, player):
        self.keyboardPlayer = player;

    def addJoystickPlayer(self, player):
        self.joystickPlayers.append(player)
    def addKeyboardPlayer(self, player):
        self.keyboardPlayer = player;

    def addJoystickPlayer(self, player):
        self.joystickPlayers.append(player)
         #74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c

