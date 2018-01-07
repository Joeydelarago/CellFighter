import pygame


class Menu(object):
    def __init__(self, settings):
        self.state = "main"
        self.pointer = 0
        self.settings = settings
<<<<<<< HEAD
        self.MenuItems = []
        self.set_menu_items()

=======
        self.currentMenuItems = []
        self.changeMenuItems("main")
    
>>>>>>> 74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c
    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        for item in self.MenuItems:
            item.draw(screen, settings)

    def set_menu_items(self):
        self.MenuItems = []
        self.pointer = 0
<<<<<<< HEAD
        if self.state == "main":
            self.MenuItems.append(MenuItem(
                "start", "Start", 200, (000, 000, 000),
                "Arial", 100, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "settings", "Settings", 200, (000, 000, 000),
                "Arial", 420, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "quit", "Quit", 200, (000, 000, 000),
                "Arial", 740, self.settings.screensize[0] // 2))
        if self.state == "settings":
            self.MenuItems.append(MenuItem(
                "fullscreen", "Fullscreen", 200, (000, 000, 000),
                "Arial", 100, self.settings.screensize[0] // 2))
            self.MenuItems.append(MenuItem(
                "volume", "<Volume = 1>", 200, (000, 000, 000),
                "Arial", 420, self.settings.screensize[0] // 2))

        self.MenuItems[0].selected = True

    def increase_pointer(self):
        self.MenuItems[self.pointer].selected = False
=======
        if newState == "main":
            self.currentMenuItems.append(MenuItem("Start", 200, (000, 000, 000),
                                                  "Arial", 100, self.settings))
            self.currentMenuItems.append(MenuItem("Settings", 200, (000, 000, 000),
                                                  "Arial", 420, self.settings))
            self.currentMenuItems.append(MenuItem("Quit", 200, (000, 000, 000),
                                                  "Arial", 740, self.settings))
        if newState == "settings":
            self.state = "settings"
            self.currentMenuItems.append(MenuItem("Fullscreen", 200, (000, 000, 000),
                                                  "Arial", 100, self.settings))
            
        self.currentMenuItems[0].selected = True

    def increasePointer(self):
        self.currentMenuItems[self.pointer].selected = False
>>>>>>> 74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c
        self.pointer += 1
        if self.pointer > len(self.MenuItems) - 1:
            self.pointer = 0
<<<<<<< HEAD
        self.MenuItems[self.pointer].selected = True

    def decrease_pointer(self):
        self.MenuItems[self.pointer].selected = False
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.MenuItems) - 1
        self.MenuItems[self.pointer].selected = True

    def activate_selected_menu_item(self, event):

        if self.state == "main":
            if event == pygame.K_RETURN:
                if self.MenuItems[self.pointer].name == "start":
                    self.settings.state = "game"

                if self.MenuItems[self.pointer].name == "settings":
                    self.state = "settings"
                    self.set_menu_items()

        if self.state == "settings":
            if event == pygame.K_RETURN:
                if self.MenuItems[self.pointer].name == "fullscreen":
                    if not self.settings.fullscreen:
                        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        self.settings.fullscreen = True
                    else:
                        pygame.display.set_mode((0, 0))
                        self.settings.fullscreen = False

            if event == pygame.K_LEFT:
                if self.MenuItems[self.pointer].name == "volume" and self.settings.volume > 0:
                    self.settings.volume -= 1
                    self.MenuItems[self.pointer].text = "<Volume = " + str(self.settings.volume) + ">"

            if event == pygame.K_RIGHT:
                if self.MenuItems[self.pointer].name == "volume" and self.settings.volume < 10:
                    self.settings.volume += 1
                    self.MenuItems[self.pointer].text = "<Volume = " + str(self.settings.volume) + ">"


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
=======
        self.currentMenuItems[self.pointer].selected = True

    def decreasePointer(self):
        self.currentMenuItems[self.pointer].selected = False
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = len(self.currentMenuItems) - 1
        self.currentMenuItems[self.pointer].selected = True

    def activateSelectedMenuItem(self):
        if self.state == "main":
            if self.currentMenuItems[self.pointer].name == "Start":
                self.settings.state = "game"
            if self.currentMenuItems[self.pointer].name == "Settings":
                self.settings.state = "settings"
                self.changeMenuItems("settings")
        if self.state == "settings":
            if self.currentMenuItems[self.pointer].name == "Fullscreen":
                if self.settings.fullscreen == False:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    self.settings.fullscreen = True
                else:
                    pygame.display.set_mode((0, 0))
                    self.settings.fullscreen = False

class MenuItem(object):

    def __init__(self, text, size, color, font, y, settings):
        self.name = text
        self.text = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf",
                                     size).render(text, 0, color)
        text_rect = self.text.get_rect()
        self.rect = pygame.rect.Rect((settings.screensize[0] // 2 -
                                      text_rect[2] // 2, y),
                                     (text_rect[2], text_rect[3]))
>>>>>>> 74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c
        self.selected = False

    def activate(self, settings):
        pass

    def draw(self, screen, settings):
        text = self.display_text(self.text, self.size, self.color)
        text_rect = text.get_rect()
        rect = pygame.rect.Rect((self.x - text_rect[2] // 2, self.y),
                                (text_rect[2], text_rect[3]))
        if self.selected:
<<<<<<< HEAD
            pygame.draw.rect(screen, (000, 100, 000), rect)
        else:
            pygame.draw.rect(screen, (000, 000, 255), rect)

        screen.blit(text, rect)
=======
            pygame.draw.rect(screen, (000, 100, 000), self.rect)
        else:
            pygame.draw.rect(screen, (000, 000, 255), self.rect)
        screen.blit(self.text, self.rect)
>>>>>>> 74f75c3360a5c8ee5311b3d25ae60f9f87a59d3c


