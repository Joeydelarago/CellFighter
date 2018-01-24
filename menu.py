import pygame
import sys
import game_functions as gf


class Menu(object):
    def __init__(self, settings):
        self.state = "main"
        self.prevstate = None
        self.pointer = 0
        self.settings = settings
        self.MenuItems = []
        self.selected_item = lambda: self.MenuItems[self.pointer]
        self.set_menu_items()
        self.background = pygame.image.load('assets/menu.png')

    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        screen.blit(self.background, (0, 0))
        for item in self.MenuItems:
            item.draw(screen, settings)

    def set_menu_items(self):
        self.MenuItems = []
        self.pointer = 0
        screenx = self.settings.resolution()[0]
        screeny = self.settings.resolution()[1]
        print(self.settings.screensize)
        if self.state == "main":
            self.MenuItems.append(MenuItem(
                "start", "Start", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 50, screenx // 2))
            self.MenuItems.append(MenuItem(
                "settings", "Settings", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 50 + (screeny // 3), screenx // 2))
            self.MenuItems.append(MenuItem(
                "quit", "Quit", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 50 + (screeny // 3)*2, screenx // 2))
        elif self.state == "settings":
            self.MenuItems.append(MenuItem(
                "resolution", "<Res = " + str(screenx) + str(screeny) + ">", self.settings.resolution()[0] // 11, (255, 255, 255),
                self.settings.font, 50, screenx // 2))
            self.MenuItems.append(MenuItem(
                "volume", "<Volume = " + str(self.settings.volume) + ">", self.settings.resolution()[0] // 11, (255, 255, 255),
                self.settings.font, 50 + (screeny // 4), screenx // 2))
            self.MenuItems.append(MenuItem(
                "fullscreen", "Fullscreen", self.settings.resolution()[0] // 11, (255, 255, 255),
                self.settings.font, 50 + (screeny // 4)*2, screenx // 2))
            self.MenuItems.append(MenuItem(
                "return", "Return", self.settings.resolution()[0] // 11, (255, 255, 255),
                self.settings.font, 50 + (screeny // 4)*3, screenx // 2))
        elif self.state == "pause":
            self.MenuItems.append(MenuItem(
                "return", "Return", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 100, screenx // 2))
            self.MenuItems.append(MenuItem(
                "settings", "Settings", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 420, screenx // 2))
            self.MenuItems.append(MenuItem(
                "quit", "Quit", self.settings.resolution()[0] // 8, (255, 255, 255),
                self.settings.font, 740, screenx // 2))

        self.MenuItems[0].selected = True
        pygame.event.clear()

    def increase_pointer(self):
        self.selected_item().selected = False
        self.pointer += 1
        if self.pointer > len(self.MenuItems) - 1:
            self.pointer = 0
        self.selected_item().selected = True

    def decrease_pointer(self):
        self.selected_item().selected = False
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.MenuItems) - 1
        self.selected_item().selected = True

    def activate_selected_menu_item(self, event):

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
                    self.settings.respointer = ((self.settings.respointer + 1) % len(self.settings.resolutions))
                    self.selected_item().text = "<Resolution = " + str(self.settings.resolutions[self.settings.respointer]) + ">"
                    gf.update_screen_resolution(self.settings)
                    self.set_menu_items()
                elif self.selected_item().name == "volume" and self.settings.volume > 0:
                    self.settings.volume -= 1
                    self.selected_item().text = "<Volume = " + str(self.settings.volume) + ">"

            elif event == pygame.K_RIGHT:
                if self.selected_item().name == "resolution":
                    self.settings.respointer = ((self.settings.respointer - 1) % len(self.settings.resolutions))
                    self.selected_item().text = "<Resolution = " + str(self.settings.resolutions[self.settings.respointer]) + ">"
                    gf.update_screen_resolution(self.settings)
                    self.set_menu_items()
                elif self.selected_item().name == "volume" and self.settings.volume < 10:
                    self.settings.volume += 1
                    self.selected_item().text = "<Volume = " + str(self.settings.volume) + ">"

class JoinMenu(object):
    def __init__(self, settings):
        self.settings = settings
        self.colors = [(255, 000, 000), (000, 255, 000),
                       (000, 000, 255), (255, 255, 000)]

    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        for i in range(4):
            x = 20 + (i * settings.resolutions[settings.respointer][0] // 4)
            y = 20
            pygame.draw.rect(screen, (255, 255, 255), (x, y, settings.resolutions[settings.respointer][0] // 4 - 40,
                                                       settings.resolutions[settings.respointer][1] - 40))
            text = pygame.font.Font(self.settings.font, self.settings.resolution()[0] // 8 - 40).render("Join", 0, self.colors[i])
            screen.blit(text, (x, y))

        for i in range(len(settings.players)):
            pygame.draw.rect(screen, self.colors[i], (20 + (i * settings.resolutions[settings.respointer][0] // 4), 20, settings.resolutions[settings.respointer][0] // 4 - 40,
                                                       settings.resolutions[settings.respointer][1] - 40))




class MenuItem(object):

    def __init__(self, name, text, size, color, font, y, x):
        self.name = name
        self.text = text
        self.size = size
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.display_text = lambda text, size, color: pygame.font.Font(self.font, size).render(text, 0, color)
        self.selected = False

    def activate(self, settings):
        pass

    def draw(self, screen, settings):
        text = self.display_text(self.text, self.size, self.color)
        text_rect = text.get_rect()
        rect = pygame.rect.Rect((self.x - text_rect[2] // 2, self.y),
                                (text_rect[2], text_rect[3]))
        if self.selected:
            text = self.display_text(self.text, self.size, (255, 000, 000))
        else:
            #pygame.draw.rect(screen, (000, 000, 255), rect)
            pass

        screen.blit(text, rect)


