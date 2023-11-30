import pygame
from block_2 import Block


class Tile_L:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.x = x
        self.y = y

        self.color = (100, 200, 250)

        self.counter = self.game.counter

        self.posture = game.tile_posture

        self.tile_positions = [ [(self.x, self.y), 
                                (self.x, self.y+40), 
                                (self.x, self.y+80), 
                                (self.x+40, self.y+80)], 

                                [(self.x-40, self.y+40), 
                                (self.x, self.y+40), 
                                (self.x+40, self.y+40), 
                                (self.x-40, self.y+80)],

                                [(self.x-40, self.y), 
                                (self.x, self.y), 
                                (self.x, self.y+40), 
                                (self.x, self.y+80)],

                                [(self.x-40, self.y+40), 
                                (self.x, self.y+40), 
                                (self.x+40, self.y+40), 
                                (self.x+40, self.y+80)]     
                                ]

        self.blocks = []

        self.create_tile(self.posture)
        
        # for i in self.blocks:
        #     print(i.x, i.y)

        self.rightmove_possible = True
        self.leftmove_possible = True
        self.moving_right = False
        self.moving_left = False
        self.moving = True
        
    def check_bottom(self):
        for i in self.blocks:
            if i.rect.bottom >= self.screen_rect.bottom:
                self.moving = False
            
    # def create_blocks(self):
    #     for block in 
        
    def create_tile(self, posture):
        # if posture == 0:
            for i in self.tile_positions[posture]:
                block = Block(self.game, i[0], i[1])
                self.blocks.append(block)
        
    def update(self):
        self.check_bottom()
        if self.moving:
            self.counter += 1
            if self.moving_right and self.rightmove_possible:
                for i in self.blocks:
                    i.rect.x += i.width
                self.moving_right = False
                
            if self.moving_left and self.leftmove_possible:
                for i in self.blocks:
                    i.rect.x -= i.width
                self.moving_left = False

            if self.counter == self.game.drop_speed:
                for i in self.blocks:
                    if not i.rect.bottom >= self.screen_rect.bottom:
                        i.rect.y += i.height
                self.counter = 0    
            
    def drawme(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        for block in self.blocks:
            block.drawme()
            # pygame.draw.rect(self.screen, self.color, block.rect)
