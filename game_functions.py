import pygame
from time import sleep
import sys

from player import Player


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

def check_events_menu():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen(screen, settings):
    screen.fill(settings.bgcolor)


def update_player():
    player.draw()


def check_player_collisions():
    pass