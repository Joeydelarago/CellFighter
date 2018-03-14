import pygame


class Arena(object):
    """Draws the arena.

        Arguments:
            settings (:obj:'Settings'): Settings stores the games settings.
            screen (:obj:'Surface'): The surface that images are drawn to.

        Attributes:
            background (:obj: 'image'): Current background for the game.
            text_color (tuple (R, G, B)): Color of the text in the game.
            font (str): Location of the games font.
            arena (:obj:'Surface'): Surface of the central arena square.
                To be used in future to tint the screen colors.
            arenar (:obj:'Surface'): Surface of the right sidebar. Used to tint
                the colors.
            arenal(:obj:'Surface'): Surface of the left sidebar. Used to tint
                the colors.
    """
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.background = pygame.image.load(self.settings.background()).convert()
        self.text_color = (200, 200, 200)
        self.font = "assets/fonts/Montserrat-Medium.ttf"
        self.arena = pygame.Surface((self.settings.arena_dimension,
                                     self.settings.arena_dimension))
        self.arena.set_alpha(0)
        self.arenar = pygame.Surface((self.settings.arena_x,
                                      self.settings.arena_dimension))
        self.arenar.set_alpha(60)
        self.arenal = pygame.Surface((self.settings.arena_x,
                                      self.settings.arena_dimension))
        self.arenal.set_alpha(60)

    def draw_arena(self):
        """Draws the arena for the players to fight in."""
        arena_x = self.settings.arena_x
        arena_size = self.settings.arena_dimension
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.arena, (arena_x, 0))

    def draw_game_sidebars(self):
        """Draws the sidebars with the players stats."""
        t = self.text_color
        f = self.font
        s = self.screen

        # Fills the left bar with a transparent color
        self.screen.blit(self.arenal, (0, 0))
        # Fills the right bar with a transparent color
        self.screen.blit(self.arenar, (self.settings.arena_x +
                                       self.settings.arena_dimension, 0))

        # Draws the sidebars in the gameloop that indicate the players statuses
        screenx = self.settings.resolution()[0]
        screeny = self.settings.resolution()[1]
        borderx = (screenx - screeny) // 2

        stats = pygame.font.Font(f, screenx // 20).render("Player 1", 0, t)
        s.blit(stats, (0, 0))
        stats = pygame.font.Font(f, screenx // 25).render("W:", 0, t)
        s.blit(stats, (0, screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("L:", 0, t)
        s.blit(stats, (screenx // 10, screeny // 10))

        stats = pygame.font.Font(f, screenx // 20).render("Player 2", 0, t)
        s.blit(stats, (0, screeny // 2))
        stats = pygame.font.Font(f, screenx // 25).render("W:", 0, t)
        s.blit(stats, (0, (screeny // 2) + screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("L:", 0, t)
        s.blit(stats, (screenx // 10, (screeny // 2) + screeny // 10))

        stats = pygame.font.Font(f, screenx // 20).render("Player 3", 0, t)
        s.blit(stats, (screenx - (borderx), 0))
        stats = pygame.font.Font(f, screenx // 25).render("W:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("L:", 0, t)
        s.blit(stats, (screenx - (borderx) + screenx // 10, screeny // 10))

        stats = pygame.font.Font(f, screenx // 20).render("Player 4", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 2))
        stats = pygame.font.Font(f, screenx // 25).render("W:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 2 + screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("L:", 0, t)
        s.blit(stats, (screenx - (borderx) + screenx // 10, screeny // 2 + screeny // 10))
