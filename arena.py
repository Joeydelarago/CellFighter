import pygame


class Arena(object):
    # Draws the arena.
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.background = pygame.image.load(self.settings.background()).convert()
        self.color = (0, 0, 0)
        self.sidebar_color = (0, 0, 0)
        self.text_color = (230, 230, 230)
        self.font = "assets/fonts/Montserrat-Medium.ttf"
        # color for arena overlay
        self.arena = pygame.Surface((self.settings.arena_dimension,
                                     self.settings.arena_dimension))
        self.arena.set_alpha(0)
        #  color overlay for right bar
        self.arenar = pygame.Surface((self.settings.arena_x,
                                      self.settings.arena_dimension))
        self.arenar.set_alpha(120)
        # color overlay for left bar
        self.arenal = pygame.Surface((self.settings.arena_x,
                                      self.settings.arena_dimension))
        self.arenal.set_alpha(120)

    def draw_arena(self):
        # Draws the arena for the players to fight in
        arena_x = self.settings.arena_x
        arena_size = self.settings.arena_dimension
        color = self.settings.arenaColor
        self.screen.blit(self.background, (0, 0))
        self.arena.fill(self.color)
        self.screen.blit(self.arena, (arena_x, 0))

    def draw_game_sidebars(self):
        t = self.text_color
        f = self.font
        s = self.screen

        # Fills the left bar with a transparent color
        self.arenal.fill(self.sidebar_color)
        self.screen.blit(self.arenal, (0, 0))
        # Fills the right bar with a transparent color
        self.arenar.fill(self.sidebar_color)
        self.screen.blit(self.arenar, (self.settings.arena_x +
                                       self.settings.arena_dimension, 0))

        # Draws the sidebars in the gameloop that indicate the players statuses
        screenx = self.settings.resolution()[0]
        screeny = self.settings.resolution()[1]
        borderx = (screenx - screeny) // 2

        stats = pygame.font.Font(f, screenx // 20).render("Player 1", 0, t)
        s.blit(stats, (0, 0))
        stats = pygame.font.Font(f, screenx // 25).render("Wins:", 0, t)
        s.blit(stats, (0, screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("Losses:", 0, t)
        s.blit(stats, (0, screeny // 5))

        stats = pygame.font.Font(f, screenx // 20).render("Player 2", 0, t)
        s.blit(stats, (0, screeny // 2))
        stats = pygame.font.Font(f, screenx // 25).render("Wins:", 0, t)
        s.blit(stats, (0, (screeny // 2) + screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("Losses:", 0, t)
        s.blit(stats, (0, (screeny // 2) + screeny // 5))

        stats = pygame.font.Font(f, screenx // 20).render("Player 3", 0, t)
        s.blit(stats, (screenx - (borderx), 0))
        stats = pygame.font.Font(f, screenx // 25).render("Wins:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("Losses:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 5))

        stats = pygame.font.Font(f, screenx // 20).render("Player 4", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 2))
        stats = pygame.font.Font(f, screenx // 25).render("Wins:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 2 + screeny // 10))
        stats = pygame.font.Font(f, screenx // 25).render("Losses:", 0, t)
        s.blit(stats, (screenx - (borderx), screeny // 2 + screeny // 5))
