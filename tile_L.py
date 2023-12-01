import pygame


class Block:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = (100, 200, 250)

    def drawme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Tile_L:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.x = x
        self.y = y

        self.drop_speed = game.drop_speed
        self.counter = 0

        self.posture = 0
        self.tile_positions = [[(self.x, self.y), 
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

        self.rightmove_possible = True
        self.leftmove_possible = True
        self.moving_right = False
        self.moving_left = False
        self.moving = True
    
    def create_tile_blocks(self):
        for i in self.tile_positions[0]:
            block = Block(self.game, i[0], i[1])
            self.game.moving_blocks.append(block)
   

    def update(self):       
        self.posture = self.game.tile_posture
        
        if self.moving:  
            self.counter += 1
            
            if self.moving_right and self.rightmove_possible:
                for i in self.game.moving_blocks:
                    i.rect.x += i.width
                self.moving_right = False
                
            if self.moving_left and self.leftmove_possible:
                for i in self.game.moving_blocks:
                    i.rect.x -= i.width
                self.moving_left = False

            if self.counter == self.game.drop_speed:
                for i in self.game.moving_blocks:
                    i.rect.y += i.height

                self.counter = 0
                        
            
                    

            
    # def drawme(self):
    #     # pygame.draw.rect(self.screen, self.color, self.rect)
    #     for block in self.blocks:
    #         pygame.draw.rect(self.screen, self.color, block.rect)
            # pygame.draw.rect(self.screen, self.color, block.rect)
