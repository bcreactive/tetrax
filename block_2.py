import pygame


class Block:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 40
        self.height = 40
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (100, 200, 250)

        # self.drop_speed = 60
        # self.counter = self.game.counter

        # self.rightmove_possible = True
        # self.leftmove_possible = True
        # self.moving_right = False
        # self.moving_left = False
        # self.moving = True
        
    # def check_bottom(self):
    #     if self.rect.bottom >= self.screen_rect.bottom:
    #         return True

    # def update(self):
    #     if self.moving:
    #         # self.counter += 1
    #         if self.moving_right and self.rightmove_possible:
    #             self.rect.x += self.width
    #             self.moving_right = False
                
    #         if self.moving_left and self.leftmove_possible:
    #             self.rect.x -= self.width
    #             self.moving_left = False

            # if self.counter == self.game.drop_speed:
            #     if not self.rect.bottom >= self.screen_rect.bottom:
            #         self.rect.y += self.height
            #     self.counter = 0    
            
    def drawme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
