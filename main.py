import pygame
import game_functions as gf
from settings import Settings
from menu import Menu
from player import Player

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()
    joystickPlayers = []
    keyboardPlayer = Player(screen, 1, (255, 000, 000), 100, 400, "keyboard")
    keyboardPlayer.active  = True
    joystickPlayers.append(Player(screen, 2, (255, 255, 000), 400, 100, "joystick"))
    joystickPlayers.append(Player(screen, 3, (255, 000, 255), 100, 100, "joystick"))
    joystickPlayers.append(Player(screen, 4, (000, 255, 000), 400, 400, "joystick"))
    settings = Settings(pygame.display.Info().current_h,
                        pygame.display.Info().current_w,keyboardPlayer,joystickPlayers)
    menu = Menu(settings)
    pygame.transform.scale(screen, settings.screensize)
    
    while True:
        clock.tick(30);


        if settings.state == "main":
            gf.check_events_menu(menu, settings)
            menu.draw(screen, settings)
        elif settings.state == "game":
            screen.fill((000, 255, 000))
            gf.check_events(screen,settings)
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
