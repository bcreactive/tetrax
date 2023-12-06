import pygame

from tile import Block


class Scorefield:
    def __init__(self, game):
        self.game = game
        # self.lines = self.game.line_counter

        # Font and color settings.
        self.color = (141, 90, 120)
        self.frame_color = (0, 0, 0)

        self.text_label_color = (10, 100, 100)
        self.text_color = (0, 0, 0)

        self.font = pygame.font.SysFont(None, 36)
        self.lines_font = pygame.font.SysFont(None, 54)

        self.load_positions()
        self.create_rects()

        self.prep_next()
        self.prep_level()
        self.prep_lines()

    def load_positions(self):
        # Position, Surfaces, Rects.
        self.width =  120
        self.x_position = 400

        self.next_y = 0
        self.next_heigth = 240
        self.next_img = pygame.Surface((1, 1))
        self.next_rect = pygame.Rect(0, 0, 0, 0)

        self.level_y = 240
        self.level_heigth = 160
        self.level_img = pygame.Surface((1, 1))
        self.level_rect = pygame.Rect(0, 0, 0, 0)
        
        self.lines_y = 400
        self.lines_heigth = 160
        self.lines_img = pygame.Surface((1, 1))
        self.lines_rect = pygame.Rect(0, 0, 0, 0)
        self.lines_val_img = pygame.Surface((1, 1)) 
        self.lines_val_rect = pygame.Rect(0, 0, 0, 0)

        self.empty_y = 560
        self.empty_heigth = 160

    def create_rects(self):
        self.next_srfc_rect = pygame.Rect(self.x_position, self.next_y,
                                        self.width, self.next_heigth)
        
        self.level_srfc_rect = pygame.Rect(self.x_position, self.level_y,
                                        self.width, self.level_heigth)
        
        self.lines_srfc_rect = pygame.Rect(self.x_position, self.lines_y,
                                        self.width, self.lines_heigth)
        
        self.empty_srfc_rect = pygame.Rect(self.x_position, self.empty_y,
                                        self.width, self.empty_heigth)

    def prep_next(self):
        # Get a rendered image with the level.
        next_str = "Next:"
        self.next_img = self.font.render(next_str, True, self.text_color,
                                            self.color)   
           
        self.next_rect = self.next_img.get_rect()
        self.next_rect.center = self.next_srfc_rect.center
        self.next_rect.top = self.next_srfc_rect.y + 20

    def prep_level(self):
        # Get a rendered image with the level.
        level_str = "Level:"
        self.level_img = self.font.render(level_str, True, self.text_color,
                                            self.color)   
           
        self.level_rect = self.level_img.get_rect()
        self.level_rect.center = self.level_srfc_rect.center
        self.level_rect.top = self.level_srfc_rect.y + 20

    def prep_lines(self):
        self.lines = self.game.line_counter
        # Get a rendered image with the destroyed lines.
        lines_str = "Lines:"
        self.lines_img = self.font.render(lines_str, True, self.text_color,
                                            self.color)   
        
               
        self.lines_rect = self.lines_img.get_rect()
        self.lines_rect.center = self.lines_srfc_rect.center
        self.lines_rect.top = self.lines_srfc_rect.y + 20

        self.lines_val = f"{self.lines}"
        self.lines_val_img = self.lines_font.render(self.lines_val, True, self.text_color,
                                            self.color)

        self.lines_val_rect = self.lines_val_img.get_rect()
        self.lines_val_rect.center = self.lines_srfc_rect.center
        self.lines_val_rect.top = self.lines_srfc_rect.y + 75

    def drawme(self):
        pygame.draw.rect(self.game.screen, self.color, self.next_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.next_srfc_rect, width=4)
        self.game.screen.blit(self.next_img, self.next_rect)
        
        pygame.draw.rect(self.game.screen, self.color, self.level_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.level_srfc_rect, width=4)
        self.game.screen.blit(self.level_img, self.level_rect)
        
        pygame.draw.rect(self.game.screen, self.color, self.lines_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.lines_srfc_rect, width=4)
        self.game.screen.blit(self.lines_img, self.lines_rect)
        self.game.screen.blit(self.lines_val_img, self.lines_val_rect)
        
        pygame.draw.rect(self.game.screen, self.color, self.empty_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.empty_srfc_rect, width=4)
        


