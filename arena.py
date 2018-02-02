import pygame

class Arena(object):
    #Draws the arena.
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.background = pygame.image.load("assets/arena.png").convert()

    def draw_arena(self):
        #Draws the arena for the players to fight in.
        self.screen.fill((0, 0, 0))
        self.screen.fill(self.settings.arenaColor, (self.settings.arena_x, 0, self.settings.arena_dimension,self.settings.arena_dimension))
        self.screen.blit(self.background, (self.settings.arena_x, 0, self.settings.arena_dimension,self.settings.arena_dimension))

    def draw_game_sidebars(self):
        #Draws the sidebars in the gameloop that indicate the players statuses.
        screenx = self.settings.resolution()[0]
        screeny = self.settings.resolution()[1]
        borderx = (screenx - screeny) // 2
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 1", 0, (255, 0, 0))
        self.screen.blit(player_info, (0, 0))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (255, 0, 0))
        self.screen.blit(player_info, (0, screeny // 10))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (255, 0, 0))
        self.screen.blit(player_info, (0, screeny // 5))

        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 2", 0, (0, 255, 0))
        self.screen.blit(player_info, (0, screeny // 2))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (0, 255, 0))
        self.screen.blit(player_info, (0, (screeny // 2) + screeny // 10))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (0, 255, 0))
        self.screen.blit(player_info, (0, (screeny // 2) + screeny // 5))

        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 3", 0, (0, 0, 255))
        self.screen.blit(player_info, (screenx - (borderx), 0))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (0, 0, 255))
        self.screen.blit(player_info, (screenx - (borderx), screeny // 10))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (0, 0, 255))
        self.screen.blit(player_info, (screenx - (borderx), screeny // 5))

        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 20).render("Player 4", 0, (255, 255, 0))
        self.screen.blit(player_info, (screenx - (borderx), screeny // 2))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Wins:", 0, (255, 255, 0))
        self.screen.blit(player_info, (screenx - (borderx), screeny // 2 + screeny // 10))
        player_info = pygame.font.Font("assets/fonts/Montserrat-Medium.ttf", screenx // 25).render("Losses:", 0, (255, 255, 0))
        self.screen.blit(player_info, (screenx - (borderx), screeny // 2 + screeny // 5))
