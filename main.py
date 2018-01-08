import pygame
import game_functions as gf
from settings import Settings
from menu import Menu
from player import Player


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w)
    settings.addKeyboardPlayer(Player(screen, settings, 1, (255, 000, 000),
                                      100, 400, "keyboard"))
    settings.addJoystickPlayer(Player(screen, settings, 2, (255, 255, 000),
                                      400, 100, "joystick"))
    settings.addJoystickPlayer(Player(screen, settings, 3, (255, 000, 255),
                                      100, 100, "joystick"))
    settings.addJoystickPlayer(Player(screen, settings, 4, (000, 255, 000),
                                      400, 400, "joystick"))
#>>>>>>> 74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c

    settings.keyboardPlayer.active = True
    menu = Menu(settings)
    pygame.transform.scale(screen, settings.screensize)
    
    while True:
        clock.tick(60)

        if settings.state in ["main","settings"] :
            gf.check_events_menu(menu, settings)
            menu.draw(screen, settings)
        elif settings.state == "game":
            screen.fill((000, 255, 000))
            gf.check_events(screen, settings)
            if settings.keyboardPlayer.active:
                settings.keyboardPlayer.update()
                settings.keyboardPlayer.draw()
        pygame.display.flip()


try:
    run_game()
except Exception as ex:
    trace.print_exc()
    pygame.display.quit()
    pygame.quit()
