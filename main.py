import pygame
import game_functions as gf
from settings import Settings
from menu import Menu
from player import Player

def run_game():
    pygame.init()
    players = []
    settings = Settings(pygame.display.Info().current_h/4,
                        pygame.display.Info().current_w/4,[])
    menu = Menu(settings)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.transform.scale(screen, settings.screensize)
    players.append(Player(screen, 1, (255, 000, 000), 100, 400, "keyboard"))
    players.append(Player(screen, 1, (255, 255, 000), 400, 100, "keyboard"));
    players.append(Player(screen, 1, (255, 000, 255), 100, 100, "keyboard"));
    players.append(Player(screen, 1, (000, 255, 000), 400, 400, "keyboard"));
    
    while True:
        if menu.state:
            gf.check_events_menu(menu)
            menu.draw(screen, settings)
        else:
            screen.fill((000, 255, 000))
            for player in players:
                gf.check_events(screen, player);
                player.update();
                player.draw();
        pygame.display.flip()
try:
    run_game()
except:
    pygame.quit()
