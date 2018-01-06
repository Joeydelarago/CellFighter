import pygame


class Menu(object):
    def __init__(self, settings):
        self.state = "main"
        self.pointer = 0
        self.settings = settings
        self.currentMenuItems = []
        self.changeMenuItems("main")
    
    def draw(self, screen, settings):
        screen.fill(settings.bg_color)
        for item in self.currentMenuItems:
            item.draw(screen, settings)

    def changeMenuItems(self, newState):
        self.currentMenuItems = []
        self.pointer = 0
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
        self.pointer += 1
        if self.pointer > len(self.currentMenuItems) - 1:
            self.pointer = 0
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
        self.selected = False

    def draw(self, screen, settings):
        if self.selected:
            pygame.draw.rect(screen, (000, 100, 000), self.rect)
        else:
            pygame.draw.rect(screen, (000, 000, 255), self.rect)
        screen.blit(self.text, self.rect)


