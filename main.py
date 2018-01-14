import pygame
import game_functions as gf
from settings import Settings
from menu import Menu, JoinMenu
from player import Player


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w)
    for i in range(len(settings.resolutions)):
        print(pygame.display.Info().current_w, settings.resolutions[i][0])
        if settings.resolutions[i][0] == pygame.display.Info().current_w and \
           settings.resolutions[i][1] == pygame.display.Info().current_h:
            settings.respointer = i
    if settings.respointer == None:
        settings.respointer = 1
        for i in range(len(settings.resolutions)):
            if pygame.display.Info().current_w // pygame.display.Info().current_h == settings.resolutions[i][0] // settings.resolutions[i][1]:
                respointer = i
    settings.default_res = settings.resolution()
    menu = Menu(settings)
    join_menu = JoinMenu(settings)
    
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
            gf.draw_arena(screen, settings)
            gf.draw_game_sidebars(screen, settings)
            gf.check_events(screen, menu, settings)
            for player in settings.players:
                player.update()
            for player1 in settings.players:
                for player2 in settings.players:
                    if player1 != player2:
                       player1.checkCollisions(player2)
            for player in settings.players:
                player.draw()
        pygame.display.flip()


try:
    run_game()
except Exception as ex:
    trace.print_exc()
    pygame.display.quit()
    pygame.quit()
