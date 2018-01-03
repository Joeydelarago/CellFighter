import pygame
import game_functions as gf
from settings import Settings
from menu import Menu
from player import Player

def run_game():
    pygame.init()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w,[])
    menu = Menu()
    screen = pygame.display.set_mode(settings.screensize)
    player1 = Player(screen, 1, (255, 000, 000), 100, 100, "keyboard");
    settings.players.append(player1)
    
    while True:
        if menu.state:
            gf.check_events_menu()
            menu.draw(screen, settings)
        else:
            gf.check_events()
            screen.fill((000, 255, 000))
            for player in players:
                #player.update()
                pass

            for player in players:
                player.draw()
        pygame.display.flip()
run_game()
