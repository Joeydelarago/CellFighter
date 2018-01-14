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
        if event.key == pygame.K_LEFT:
            player.left = -1
        if event.key == pygame.K_0:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_ESCAPE:
            settings.state = "main"
            menu.state = "pause"
            menu.set_menu_items()
        if event.key == pygame.K_x:
            player.attack()

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player.up = 0
        if event.key == pygame.K_RIGHT:
            player.right = 0
        if event.key == pygame.K_DOWN:
            player.down = 0
        if event.key == pygame.K_LEFT:
            player.left = 0


def joystickControls(event, screen, player):
    if event.type == pygame.JOYAXISMOTION:
        if event.axis == 1:
            if event.value < -0.1:
                player.up = event.value
                player.down = 0
            elif event.value > 0.1:
                player.down = event.value
                player.up = 0
            else:
                player.up = 0
                player.down = 0
        elif event.axis == 0:
            if event.value < -0.1:
                player.left = event.value
                player.right = 0
            elif event.value > 0.1:
                player.right = event.value
                player.left = 0
            else:
                player.left = 0
                player.right = 0


def check_events(screen, menu, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for player in settings.players:
                if player.controllerID == "keyboard":
                    keyboardPlayerEvents(event, screen, player, menu, settings)
        elif event.type == pygame.JOYBUTTONUP or\
                event.type == pygame.JOYBUTTONDOWN or\
                event.type == pygame.JOYAXISMOTION:
            for player in settings.players:
                if player.controllerID == event.joy:
                    joystickControls(event, screen, player)



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

def check_events_join(menu, settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN and len(settings.players) > 0:
                settings.state = "game"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                for player in settings.players:
                    if player.controllerID == "keyboard":
                        return
                settings.add_player(Player(screen, settings, len(settings.players) + 1, (180, 80, 80), 100, 400, "keyboard"))

        elif event.type == pygame.JOYBUTTONDOWN:
            for player in settings.players:
                if event.joy == player.controllerID:
                    return 
            settings.add_player(Player(screen, settings, len(settings.players) + 1, (180, 80, 80), 100, 400, event.joy))

def update_screen(screen, settings):
    screen.fill(settings.bgcolor)


def update_player():
    player.draw()


def check_player_collisions():
    pass