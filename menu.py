import pygame


class Menu(object):
    def __init__(self):
        self.state = "main"
        self.main_menu_items = []
        start_button = MenuItem
        self.main_menu_items.append((x, y, text))

    def draw(self, screen, settings):
        if self.state == "main":
            screen.fill(settings.bg_color)
            newFont=pygame.font.Font(textFont, textSize)
            newText=newFont.render(message, 0, textColor)
 
    return newText
        if self.state == "options":
            pass
        if self.state == "game_over":
            pass


class MenuItem(object):
    """docstring for MenuObject"""
    def __init__(self, text, size, color, font, x, y):
        self.text = test
        self.size = size
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        