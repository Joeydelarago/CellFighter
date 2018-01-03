import pygame
import game_functions as gf
import settings
import menu
from player import Player

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Cell Fighter")

run_game()