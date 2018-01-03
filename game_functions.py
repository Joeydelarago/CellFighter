import pygame
from time import sleep
import sys

from player import Player

def controller_check():
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)

def keydown_events(event, screen, player):
    if player.controlType == "keyboard":
        if event.key == pygame.K_UP:
            player.up = -1
        if event.key == pygame.K_RIGHT:
            player.right = 1
        if event.key == pygame.K_DOWN:
            player.down = 1
        if event.key == pygame.K_LEFT:
            player.left = -1
    if player.controlType == "controller":
        pass


def keyup_events(event, screen, player):
    if player.controlType == "keyboard":
        if event.key == pygame.K_UP:
            player.up = 0
        if event.key == pygame.K_RIGHT:
            player.right = 0
        if event.key == pygame.K_DOWN:
            player.down = 0
        if event.key == pygame.K_LEFT:
            player.left = 0
    if player.controlType == "controller":
        pass

def check_events(screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydown_events(event, screen, player)
        if event.type == pygame.KEYUP:
            keyup_events(event, screen, player)

def check_events_menu(menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for item in menu.main_menu_items:
                if item.rect.collidepoint(pos):
                    print(item.name)
                    if item.name == "Start":
                        menu.state = False
                    else:
                        menu.state = item.name
        elif event.type == pygame.MOUSEBUTTONDOWN and event.butten != 1:
            pygame.quit()
            sys.exit()



def update_screen(screen, settings):
    screen.fill(settings.bgcolor)


def update_player():
    player.draw()


def check_player_collisions():
    pass