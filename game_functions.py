import pygame
import sys
import math
from player import Player
from time import sleep


def controller_check():
    """ Checks for controllers creates and object for each and initializes them
        and appends them to the joysticks list.
    """
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)


def keyboardPlayerEvents(event, screen, player, menu, settings):
    """Checks for events from the keyboard."""
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
        if event.key == pygame.K_z:
            player.dash()

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
    """Checks for events from controllers associated with players."""
    if event.type == pygame.JOYAXISMOTION:
        if event.axis == 1:
            if math.sqrt(pygame.joystick.Joystick(event.joy).get_axis(0)
                         ** 2
                         + event.value**2) > 0.25:
                if abs(event.value) > 1:
                    event.value = math.copysign(1, event.value)
                if event.value < -0:
                    player.up = event.value
                    player.down = 0
                elif event.value > 0:
                    player.down = event.value
                    player.up = 0
            else:
                player.up = 0
                player.down = 0
        elif event.axis == 0:
            if math.sqrt(pygame.joystick.Joystick(event.joy).get_axis(0)
                         ** 2
                         + event.value**2) > 0.25:
                if abs(event.value) > 1:
                    event.value = math.copysign(1, event.value)
                if event.value < -0:
                    player.left = event.value
                    player.right = 0
                elif event.value >= 0:
                    player.right = event.value
                    player.left = 0
            else:
                player.left = 0
                player.right = 0
    elif event.type == pygame.JOYBUTTONDOWN:
        print(event.button)
        if event.button == 2:
            player.attack()
        elif event.button == 0:
            player.dash()


def check_events(screen, menu, settings):
    """ Checks for events and forwards them to the keyboard event handler,
        the joystick event handler or quits.
    """
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
    """Checks for events in the menus."""
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
    """ Checks for events in the join screen menu and adds players and their
        associated controlers if the press a button.
    """
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
                settings.add_player(Player(screen,
                                           settings,
                                           len(settings.players) + 1,
                                           (180, 80, 80), 100, 400,
                                           "keyboard"))

        elif event.type == pygame.JOYBUTTONDOWN:
            for player in settings.players:
                if event.joy == player.controllerID:
                    return
            settings.add_player(Player(screen,
                                       settings,
                                       len(settings.players) + 1,
                                       (180, 80, 80),
                                       100,
                                       400,
                                       event.joy))


def update_screen_resolution(settings):
    """Updates the screen resolution, and arean size when res is changed"""
    pygame.display.set_mode(settings.resolutions[settings.respointer])
    settings.arena_x = ((settings.resolution()[0]
                         - settings.resolution()[1]) // 2)
    settings.arena_dimension = settings.resolution()[1]
    settings.fullscreen = False


def find_screen_resolution(settings):
    """Finds a game resolution appropriate for the screen"""
    monitor_w = pygame.display.Info().current_w
    monitor_h = pygame.display.Info().current_h
    for i in range(len(settings.resolutions)):
        # This checks if the monitors resolution matches any of the
        # avaliable ones.
        if settings.resolutions[i][0] == monitor_w and \
           settings.resolutions[i][1] == monitor_h:
            settings.respointer = i

    if settings.respointer is None:
        # If a match resolutoin can't be found it will try to find one with
        # the same aspect ratio.
        settings.respointer = 1
        for i in range(len(settings.resolutions)):
            if (monitor_w // monitor_h ==
               settings.resolutions[i][0] // settings.resolutions[i][1]):
                respointer = i


def update_player():
    player.draw()


def new_round(settings):
    for player in settings.players:
        player.respawn()
    settings.living_players -= 1


def check_player_collisions():
    pass
