import pygame
import game_functions as gf

from settings import Settings
from menu import Menu, JoinMenu
from player import Player
from arena import Arena


def run_game():
    """The initializer for all of the menus and screens. Also the main loop."""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w)
    gf.find_screen_resolution(settings)
    settings.default_res = settings.resolution()
    menu = Menu(settings)
    join_menu = JoinMenu(settings)
    arena = Arena(settings, screen)

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
            arena.draw_arena()
            arena.draw_game_sidebars()
            gf.check_events(screen, menu, settings)

            for player in settings.players:
                if player.alive:
                    player.update()
                    for player2 in settings.players:
                        if player != player2:
                            player.checkCollisions(player2)

            for player in settings.players:
                if player.alive:
                    player.draw()

            if settings.living_players == 1:
                gf.new_round(settings)
        pygame.display.flip()


try:
    run_game()
except Exception as ex:
    trace.print_exc()
    pygame.display.quit()
    pygame.quit()
