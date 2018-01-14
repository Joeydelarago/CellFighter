import pygame
import game_functions as gf
from settings import Settings
from menu import Menu, JoinMenu
from player import Player


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w)
    menu = Menu(settings)
    join_menu = JoinMenu(settings)
    pygame.transform.scale(screen, settings.screensize)
    
    while True:
        clock.tick(60)

        if settings.state == "main":
            gf.check_events_menu(menu, settings)
            menu.draw(screen, settings)
        elif settings.state == "join":
            gf.controller_check()
            gf.check_events_join(menu, settings, screen)
            join_menu.draw(screen, settings)

        elif settings.state == "game":
            screen.fill((87, 97, 114))
            gf.check_events(screen, menu, settings)
            for player in settings.players:
                player.update()
            for player in settings.players:
                player.draw()
        pygame.display.flip()


try:
    run_game()
except Exception as ex:
    trace.print_exc()
    pygame.display.quit()
    pygame.quit()
