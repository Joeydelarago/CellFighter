import pygame
from time import sleep
import sys
from player import Player


def keydown_events(event, screen, player):
    if player.controlType == "keyboard":
        if event.key == pygame.K_UP:
            player.up = True
        if event.key == pygame.K_RIGHT:
            player.right = True
        if event.key == pygame.K_DOWN:
            player.down = True
        if event.key == pygame.K_LEFT:
            player.left = True
    if player.controlType == "keyboard":
        pass


def keyup_events(event, screen, player):
    if player.controlType == "keyboard":
        if event.key == pygame.K_UP:
            player.up = False
        if event.key == pygame.K_RIGHT:
            player.right = False
        if event.key == pygame.K_DOWN:
            player.down = False
        if event.key == pygame.K_LEFT:
            player.left = False
    if player.controlType == "keyboard":
        pass


def update_screen(screen):
    screen.fill("red")


def update_player():
    player.draw()


def check_player_collisions():
    pass

