import pygame


class Menu(object):
    def __init__(self):
        self.state = "main"
        self.main_menu_items = []
        start_button = MenuItem("Start", 200, (000, 000, 000),
                                "Arial", 100)
        options_button = MenuItem("Options", 200, (000, 000, 000),
                                "Arial", 420)
        quit_button = MenuItem("Quit", 200, (000, 000, 000),
                                "Arial", 740)
        self.main_menu_items.append(start_button)
        self.main_menu_items.append(quit_button)
        self.main_menu_items.append(options_button)

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
    def __init__(self, text, size, color, font, y):
        self.text = text
        self.size = size
        self.y = y
        self.font = font
        self.color = color
        self.selected = False

    def draw(self, screen, settings):
        new_font = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", self.size) 
        new_text = new_font.render(self.text, 0, self.color)

        text_rect = new_text.get_rect()
        rect = ((settings.screensize[0] // 2 - text_rect[2] // 2, self.y), (text_rect[2],text_rect[3]))
        if self.selected:
            pygame.draw.rect(screen, (000, 100, 000), rect)
        else:    
            pygame.draw.rect(screen, (000, 000, 255), rect)
        screen.blit(new_text, rect)


        