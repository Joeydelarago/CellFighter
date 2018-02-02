import pygame
import sys
import math
from player import Player
from time import sleep


def controller_check():
    #Checks for controllers creates and object for each and
    #initializes them and appends them to the joysticks list.
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)


def keyboardPlayerEvents(event, screen, player, menu, settings):
    #Checks for events from the keyboard.
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
    #Checks for events from controllers associated with players.
    if event.type == pygame.JOYAXISMOTION:
        if event.axis == 1:
            if math.sqrt(pygame.joystick.Joystick(event.joy).get_axis(0)**2 + event.value**2) > 0.25:
                if abs(event.value) > 1:
                    event.value = math.copysign(1,event.value)
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
            if math.sqrt(pygame.joystick.Joystick(event.joy).get_axis(0)**2 + event.value**2) > 0.25:
                if abs(event.value) > 1:
                    event.value = math.copysign(1,event.value)
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
    #Checks for events and forwards them to the keyboard event handler,
    #the joystick event handler or quits.
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
    #Checks for events in the menus.
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
    #Checks for events in the join screen menu and adds players and their
    #associated controlers if the press a button.
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

def draw_arena(screen, settings):
    #Draws the arena for the players to fight in.
    screen.fill((0, 0, 0))
    screen.fill(settings.arenaColor, (settings.arena_x, 0, settings.arena_dimension,settings.arena_dimension))

def draw_game_sidebars(screen, settings):
    #Draws the sidebars in the gameloop that indicate the players statuses.
    screenx = settings.resolution()[0]
    screeny = settings.resolution()[1]
    borderx = (screenx - screeny) // 2
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 1", 0, (255, 0, 0))
    screen.blit(player_info, (0, 0))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (255, 0, 0))
    screen.blit(player_info, (0, screeny // 10))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (255, 0, 0))
    screen.blit(player_info, (0, screeny // 5))

    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 2", 0, (0, 255, 0))
    screen.blit(player_info, (0, screeny // 2))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (0, 255, 0))
    screen.blit(player_info, (0, (screeny // 2) + screeny // 10))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (0, 255, 0))
    screen.blit(player_info, (0, (screeny // 2) + screeny // 5))

    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 3", 0, (0, 0, 255))
    screen.blit(player_info, (screenx - (borderx), 0))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (0, 0, 255))
    screen.blit(player_info, (screenx - (borderx), screeny // 10))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (0, 0, 255))
    screen.blit(player_info, (screenx - (borderx), screeny // 5))

    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 4", 0, (255, 255, 0))
    screen.blit(player_info, (screenx - (borderx), screeny // 2))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (255, 255, 0))
    screen.blit(player_info, (screenx - (borderx), screeny // 2 + screeny // 10))
    player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (255, 255, 0))
    screen.blit(player_info, (screenx - (borderx), screeny // 2 + screeny // 5))

def update_screen(screen, settings):
    #Fills the screen with the default background color.
    screen.fill(settings.bgcolor)

def update_screen_resolution(settings):
    #Updates the screen resolution when changed and the arena size to match.
    pygame.display.set_mode(settings.resolutions[settings.respointer])
    settings.arena_x = ((settings.resolution()[0] - settings.resolution()[1]) // 2)
    settings.arena_dimension = settings.resolution()[1]
    settings.fullscreen = False

def update_player():
    player.draw()

def new_round(settings):
    for player in settings.players:
        player.respawn()
    settings.living_players -= 1


def check_player_collisions():
    pass
