import pygame
import game_functions as gf
import settings
import menu
from player import Player

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    players = []
    player1 = Player(screen, 1, (255, 000, 000), 100, 100, "keyboard");
    players.append(player1)
    
    while True:
        screen.fill((000, 255, 000))
        for player in players:
            #player.update()
            pass

        for player in players:
            player.draw()
        pygame.display.flip()
run_game()
