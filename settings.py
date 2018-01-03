import pygame

import game_functions as gf
class Settings(object):
    def __init__(self, height, width, players):
        self.screensize = (height, width)
        self.fullscreen = False
        self.players = players
        self.bg_color = (000, 100, 100)

def run_game():
    pygame.init()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w,[])
    screen = pygame.display.set_mode((1000, 1000))
    
    while True:
        screen.fill((000, 255, 000))
        gf.check_events()
        pygame.display.flip()

run_game()