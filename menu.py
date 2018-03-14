import pygame
import sys
import game_functions as gf


class Menu(object):
    """A class that draws the main menu and sub menus except the join menu.
        Arguments:
            settings (:obj: 'Settings'): An object that stores all the game
                settings.

        Attributes:
            state (str): Defines the state in which the menu is.
            prevstate (str): Defines the previous state so that it can be
                returned too.
            pointer (int): Points to the current menu item in the menu state.
            menu_items (list of :obj:'MenuItem'): List of items in the current
                menu state.
            selected_item (:obj:'MenuItem'): Item that is currently selected in
                menu.
            background (:obj:'image'): Current background image for menu.
    """
    def __init__(self, settings):
        self.state = "main"
        self.prevstate = None
        self.pointer = 0
        self.settings = settings
        self.menu_items = []
        self.selected_item = lambda: self.menu_items[self.pointer]
        self.set_menu_items()
        self.background = pygame.image.load('assets/menu.png').convert()

    def draw(self, screen, settings):
        """draw the background and menu."""
        screen.blit(self.background, (0, 0))
        for item in self.menu_items:
            item.draw(screen, settings)

    def set_menu_items(self):
        """update the current menu items to reflect the menu state."""
        self.menu_items = []
        self.pointer = 0
        screenx = self.settings.resolution()[0]
        screeny = self.settings.resolution()[1]
        print(self.settings.screensize)
        if self.state == "main":
            self.menu_items.append(MenuItem(
                "start",
                "Start",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font,
                50, screenx // 2))
            self.menu_items.append(MenuItem(
                "settings",
                "Settings",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font, 50 + (screeny // 3),
                screenx // 2))
            self.menu_items.append(MenuItem(
                "quit",
                "Quit",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font,
                50 + (screeny // 3)*2, screenx // 2))

        elif self.state == "settings":
            self.menu_items.append(MenuItem(
                "resolution",
                "<Res = " + str(screenx) + str(screeny) + ">",
                self.settings.resolution()[0] // 11,
                (255, 255, 255),
                self.settings.font,
                50, screenx // 2))
            self.menu_items.append(MenuItem(
                "volume",
                "<Volume = " + str(self.settings.volume) + ">",
                self.settings.resolution()[0] // 11,
                (255, 255, 255),
                self.settings.font, 50 + (screeny // 4),
                screenx // 2))
            self.menu_items.append(MenuItem(
                "fullscreen", "Fullscreen",
                self.settings.resolution()[0] // 11,
                (255, 255, 255),
                self.settings.font,
                50 + (screeny // 4)*2,
                screenx // 2))
            self.menu_items.append(MenuItem(
                "return",
                "Return",
                self.settings.resolution()[0] // 11,
                (255, 255, 255),
                self.settings.font,
                50 + (screeny // 4)*3,
                screenx // 2))
        elif self.state == "pause":
            self.menu_items.append(MenuItem(
                "return",
                "Return",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font,
                100,
                screenx // 2))
            self.menu_items.append(MenuItem(
                "settings",
                "Settings",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font,
                420,
                screenx // 2))
            self.menu_items.append(MenuItem(
                "quit",
                "Quit",
                self.settings.resolution()[0] // 8,
                (255, 255, 255),
                self.settings.font,
                740,
                screenx // 2))

        self.menu_items[0].selected = True
        pygame.event.clear()

    def increase_pointer(self):
        """Increase the pointer for the current menu items."""
        self.selected_item().selected = False
        self.pointer += 1
        if self.pointer > len(self.menu_items) - 1:
            self.pointer = 0
        self.selected_item().selected = True

    def decrease_pointer(self):
        """Decrease the pointer for the current menu items."""
        self.selected_item().selected = False
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.menu_items) - 1
        self.selected_item().selected = True

    def activate_selected_menu_item(self, event):
        """Activate the currently selected menu item."""
        if self.state == "pause":
            if event == pygame.K_RETURN:
                if self.selected_item().name == "settings":
                    self.prevstate = "pause"
                    self.state = "settings"
                    self.set_menu_items()
                elif self.selected_item().name == "quit":
                    pygame.quit()
                    pygame.display.quit()
                    sys.exit()
                elif self.selected_item().name == "return":
                    self.settings.state = "game"
                    self.set_menu_items()

        elif self.state == "main":
            if event == pygame.K_RETURN:
                if self.selected_item().name == "start":
                    self.settings.state = "join"
                elif self.selected_item().name == "settings":
                    self.prevstate = "main"
                    self.state = "settings"
                    self.set_menu_items()
                elif self.selected_item().name == "quit":
                    pygame.quit()
                    pygame.display.quit()
                    sys.exit()

        elif self.state == "settings":
            if event == pygame.K_RETURN:
                if self.selected_item().name == "fullscreen":
                    if not self.settings.fullscreen:
                        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        self.settings.fullscreen = True
                        self.set_menu_items()
                    else:
                        pygame.display.set_mode((0, 0))
                        self.settings.fullscreen = False
                elif self.selected_item().name == "return":
                    self.state = self.prevstate
                    self.set_menu_items()

            elif event == pygame.K_LEFT:
                if self.selected_item().name == "resolution":
                    self.settings.respointer = ((self.settings.respointer + 1)
                        % len(self.settings.resolutions))
                    self.selected_item().text = "<Resolution = " \
                        + str(self.settings.resolutions[self.settings.respointer]) \
                        + ">"
                    gf.update_screen_resolution(self.settings)
                    self.set_menu_items()
                elif self.selected_item().name == "volume" and self.settings.volume > 0:
                    self.settings.volume -= 1
                    self.selected_item().text = "<Volume = " + str(self.settings.volume) + ">"

            elif event == pygame.K_RIGHT:
                if self.selected_item().name == "resolution":
                    self.settings.respointer = ((self.settings.respointer - 1)
                        % len(self.settings.resolutions))
                    self.selected_item().text = "<Resolution = " \
                        + str(self.settings.resolutions[self.settings.respointer]) \
                        + ">"
                    gf.update_screen_resolution(self.settings)
                    self.set_menu_items()
                elif self.selected_item().name == "volume" \
                        and self.settings.volume < 10:
                    self.settings.volume += 1
                    self.selected_item().text = "<Volume = " + \
                                                str(self.settings.volume) + \
                                                ">"


class JoinMenu(object):
    """ Draws the join menu.

        Arguments:
            settings(:obj: settings): Settings object that stores all settings.

        Attributes:
            text_color (tuple): RGB tuple for color of text.
            background (image): Image to blit as background.
            colors (list of tuple): List of the four player colors as tuples.
    """
    def __init__(self, settings):
        self.settings = settings
        self.text_color = (230, 230, 230)
        self.background = pygame.image.load('assets/menu.png').convert()
        self.colors = [(255, 000, 000), (000, 255, 000),
                       (000, 000, 255), (255, 255, 000)]

    def draw(self, screen, settings):
        """Draws the Join screen"""
        screen.blit(self.background, (0, 0))
        width = settings.resolutions[settings.respointer][0]
        height = settings.resolutions[settings.respointer][1]
        for i in range(4):
            x = 40 + (width // 8)
            y = 40 + (height // 8)
            if i == 1 or i == 3:
                x = x*4 + 40
            if i == 2 or i == 3:
                y = y*4
            text = pygame.font.Font(self.settings.font, width // 8 - 40).render("Join", 0, self.text_color)
            print('screen', x, y)
            screen.blit(text, (x, y))

        for i in range(len(settings.players)):
            x = 40 + (width // 8)
            y = 40 + (height // 8)
            if i == 1 or i == 3:
                x = x*4 + 40
            if i == 2 or i == 3:
                y = y*4
            text = pygame.font.Font(self.settings.font, width // 8 - 40).render("Join", 0, self.colors[i])
            screen.blit(text, (x, y))


class MenuItem(object):
    """MenuItem models the values of a button in the menu screen.

        Arguments:
            name (str): Name used to reference the menu item.
            text (str): Text to be displayed by items.
            size (int): Size of the text.
            color (tuple (R, G, B)): Tuple of RGB values for text color.
            font (str): Font of the text displayed
            x, y (int): co-ordinates on screen.

        Attributes:
            selected (bool): whether this item is selected or not
            display_text (:obj:'Font'): The object that is blitted to screen.
    """
    def __init__(self, name, text, size, color, font, y, x):
        self.name = name
        self.text = text
        self.size = size
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.display_text = lambda text, size, color: \
            pygame.font.Font(self.font, size).render(text, 0, color)
        self.selected = False

    def draw(self, screen, settings):
        """Draws the text for the button at it's x and y co ordinates at size 'size'."""
        text = self.display_text(self.text, self.size, self.color)
        text_rect = text.get_rect()
        rect = pygame.rect.Rect((self.x - text_rect[2] // 2, self.y),
                                (text_rect[2], text_rect[3]))
        if self.selected:
            text = self.display_text(self.text, self.size, (255, 000, 000))

        screen.blit(text, rect)
