import pygame
import sys
from player import Player
from time import sleep


def controller_check():
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)


def keyboardPlayerEvents(event, screen, player, menu, settings):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player.up = -1
        if event.key == pygame.K_RIGHT:
            player.right = 1
        if event.key == pygame.K_DOWN:
            player.down = 1
            print("down")
        if event.key == pygame.K_LEFT:
            player.left = -1
        if event.key == pygame.K_0:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_ESCAPE:
            settings.state = "main"
            menu.state = "pause"
            menu.set_menu_items()

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player.up = 0
        if event.key == pygame.K_RIGHT:
            player.right = 0
        if event.key == pygame.K_DOWN:
            player.down = 0
        if event.key == pygame.K_LEFT:
            player.left = 0


def joystickControls(event, screen, players):
    pass


def check_events(screen, menu, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            keyboardPlayerEvents(event, screen, settings.keyboardPlayer, menu, settings)
        elif event.type == pygame.JOYBUTTONUP or\
                event.type == pygame.JOYBUTTONDOWN or\
                event.type == pygame.JOYAXISMOTION:
                pass


def check_events_menu(menu, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.decrease_pointer()
            elif event.key == pygame.K_DOWN:
                menu.increase_pointer()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                menu.activate_selected_menu_item(event.key)


def update_screen(screen, settings):
    screen.fill(settings.bgcolor)


def update_player():
    player.draw()


def check_player_collisions():
    pass