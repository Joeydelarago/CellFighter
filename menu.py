import pygame
import sys


class Menu(object):
    def __init__(self, settings):
        self.state = "main"
        self.prevstate = None
        self.pointer = 0
        self.settings = settings
        self.MenuItems = []
        self.set_menu_items()

    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        for item in self.MenuItems:
            item.draw(screen, settings)

    def set_menu_items(self):
        self.MenuItems = []
        self.pointer = 0
        if self.state == "main":
            self.MenuItems.append(MenuItem(
                "start", "Start", 200, (000, 000, 000),
                "Arial", 50, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "settings", "Settings", 200, (000, 000, 000),
                "Arial", 50 + (self.settings.screensize[1] // 3), self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "quit", "Quit", 200, (000, 000, 000),
                "Arial", 50 + (self.settings.screensize[1] // 3)*2, self.settings.screensize[0] // 2))
        elif self.state == "settings":
            self.MenuItems.append(MenuItem(
                "volume", "<Volume = 1>", 200, (000, 000, 000),
                "Arial", 100, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "fullscreen", "Fullscreen", 200, (000, 000, 000),
                "Arial", 420, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "return", "Return", 200, (000, 000, 000),
                "Arial", 740, self.settings.screensize[0] // 2))
        elif self.state == "pause":
            self.MenuItems.append(MenuItem(
                "return", "Return", 200, (000, 000, 000),
                "Arial", 100, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "settings", "Settings", 200, (000, 000, 000),
                "Arial", 420, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "quit", "Quit", 200, (000, 000, 000),
                "Arial", 740, self.settings.screensize[0] // 2))

        self.MenuItems[0].selected = True
        pygame.event.clear()

    def increase_pointer(self):
        self.MenuItems[self.pointer].selected = False
        self.pointer += 1
        if self.pointer > len(self.MenuItems) - 1:
            self.pointer = 0
        self.MenuItems[self.pointer].selected = True

    def decrease_pointer(self):
        self.MenuItems[self.pointer].selected = False
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.MenuItems) - 1
        self.MenuItems[self.pointer].selected = True

    def activate_selected_menu_item(self, event):

        if self.state == "pause":
            if event == pygame.K_RETURN:
                if self.MenuItems[self.pointer].name == "settings":
                    self.prevstate = "pause"
                    self.state = "settings"
                    self.set_menu_items()
                if self.MenuItems[self.pointer].name == "quit":
                    pygame.quit()
                    pygame.display.quit()
                    sys.exit()
                if self.MenuItems[self.pointer].name == "return":
                    self.state = "main"
                    self.set_menu_items()

        if self.state == "main":
            if event == pygame.K_RETURN:
                if self.MenuItems[self.pointer].name == "start":
                    self.settings.state = "join"
                if self.MenuItems[self.pointer].name == "settings":
                    self.prevstate = "main"
                    self.state = "settings"
                    self.set_menu_items()
                if self.MenuItems[self.pointer].name == "quit":
                    pygame.quit()
                    pygame.display.quit()
                    sys.exit()

        if self.state == "settings":
            if event == pygame.K_RETURN:
                if self.MenuItems[self.pointer].name == "fullscreen":
                    if not self.settings.fullscreen:
                        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        self.settings.fullscreen = True
                    else:
                        pygame.display.set_mode((0, 0))
                        self.settings.fullscreen = False
                if self.MenuItems[self.pointer].name == "return":
                    self.state = self.prevstate
                    self.set_menu_items()

            if event == pygame.K_LEFT:
                if self.MenuItems[self.pointer].name == "volume" and self.settings.volume > 0:
                    self.settings.volume -= 1
                    self.MenuItems[self.pointer].text = "<Volume = " + str(self.settings.volume) + ">"

            if event == pygame.K_RIGHT:
                if self.MenuItems[self.pointer].name == "volume" and self.settings.volume < 10:
                    self.settings.volume += 1
                    self.MenuItems[self.pointer].text = "<Volume = " + str(self.settings.volume) + ">"

class JoinMenu(object):
    def __init__(self, settings):
        self.settings = settings
        self.colors = [(255, 000, 000), (000, 255, 000),
                       (000, 000, 255), (255, 255, 000)]

    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        for i in range(4):
            x = 20 + (i * settings.screensize[0] // 4)
            y = 20
            pygame.draw.rect(screen, (000, 000, 000), (x, y, settings.screensize[0] // 4 - 40,
                                                       settings.screensize[1] - 40))
            text = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", 200).render("Join", 0, self.colors[i])
            screen.blit(text, (x, y))

        for i in range(len(settings.players)):
            pygame.draw.rect(screen, self.colors[i], (20 + (i * settings.screensize[0] // 4), 20, settings.screensize[0] // 4 - 40,
                                                       settings.screensize[1] - 40))




class MenuItem(object):

    def __init__(self, name, text, size, color, font, y, x):
        self.name = name
        self.text = text
        self.size = size
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.display_text = lambda text, size, color: pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", size).render(text, 0, color)
        self.selected = False

    def activate(self, settings):
        pass

    def draw(self, screen, settings):
        text = self.display_text(self.text, self.size, self.color)
        text_rect = text.get_rect()
        rect = pygame.rect.Rect((self.x - text_rect[2] // 2, self.y),
                                (text_rect[2], text_rect[3]))
        if self.selected:
            pygame.draw.rect(screen, (000, 100, 000), rect)
        else:
            pygame.draw.rect(screen, (000, 000, 255), rect)

        screen.blit(text, rect)


