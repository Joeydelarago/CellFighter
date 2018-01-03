import pygame


class Menu(object):
    def __init__(self, settings):
        self.state = "main"
        self.main_menu_items = []
        start = MenuItem("Start", 200, (000, 000, 000),
                                "Arial", 100, settings)
        options = MenuItem("Options", 200, (000, 000, 000),
                                "Arial", 420, settings)
        quit = MenuItem("Quit", 200, (000, 000, 000),
                                "Arial", 740, settings)
        self.main_menu_items.append(start)
        self.main_menu_items.append(quit)
        self.main_menu_items.append(options)

    def draw(self, screen, settings):
        if self.state == "main":
            screen.fill(settings.bg_color)
            for item in self.main_menu_items:
                item.draw(screen, settings)
        if self.state == "options":
            pass
        if self.state == "game_over":
            pass


class MenuItem(object):
    """docstring for MenuObject"""
    def __init__(self, text, size, color, font, y, settings):
        self.name = text
        self.text =  pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", size).render(text, 0, color)
        text_rect = self.text.get_rect()
        self.rect = pygame.rect.Rect((settings.screensize[0] // 2 - text_rect[2] // 2, y), (text_rect[2],text_rect[3]))
        self.selected = False

    def draw(self, screen, settings):
        if self.selected:
            pygame.draw.rect(screen, (000, 100, 000), self.rect)
        else:    
            pygame.draw.rect(screen, (000, 000, 255), self.rect)
        screen.blit(self.text, self.rect)


        