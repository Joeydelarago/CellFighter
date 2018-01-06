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

    def addKeyboardPlayer(self, player):
    	self.keyboardPlayer = player;

    def addJoystickPlayer(self, player):
    	self.joystickPlayers.append(player)

