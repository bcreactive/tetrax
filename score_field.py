import pygame


class Scorefield:
    def __init__(self, game):
        self.game = game

        self.color = (101, 50, 200)
        self.frame_color = (0, 0, 0)
        self.WIDHT =  160
        self.X_POSITION = 400

        self.next_y = 0
        self.next_heigth = 240

        self.level_y = 240
        self.level_heigth = 160

        self.lines_y = 400
        self.lines_heigth = 160

        self.empty_y = 560
        self.empty_heigth = 160

        self.create_rects()

    def create_rects(self):
        self.next_rect = pygame.Rect(self.X_POSITION, self.next_y,
                                        self.WIDHT, self.next_heigth)
        
        self.level_rect = pygame.Rect(self.X_POSITION, self.level_y,
                                        self.WIDHT, self.level_heigth)
        
        self.lines_rect = pygame.Rect(self.X_POSITION, self.lines_y,
                                        self.WIDHT, self.lines_heigth)
        
        self.empty_rect = pygame.Rect(self.X_POSITION, self.empty_y,
                                        self.WIDHT, self.empty_heigth)
        
        # self.next_surface = pygame.Surface(self.X_POSITION, self.next_y)
        # self.next_surface.fill(10, 50, 200)
        # self.level_surface = pygame.Surface(self.X_POSITION, self.level_y)
        # self.next_surface.fill(10, 50, 200)
        # self.lines_surface = pygame.Surface(self.X_POSITION, self.lines_y)
        # self.next_surface.fill(10, 50, 200)
        # self.empty_surface = pygame.Surface(self.X_POSITION, self.empty_y)
        # self.next_surface.fill(10, 50, 200)
    
    def drawme(self):
        pygame.draw.rect(self.game.screen, self.color, self.next_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.next_rect, width=4)
        
        pygame.draw.rect(self.game.screen, self.color, self.level_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.level_rect, width=4)
        
        pygame.draw.rect(self.game.screen, self.color, self.lines_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.lines_rect, width=4)
        
        pygame.draw.rect(self.game.screen, self.color, self.empty_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.empty_rect, width=4)

