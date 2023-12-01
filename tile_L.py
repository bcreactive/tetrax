import pygame


class Block:
    def __init__(self, x, y):
        # self.game = game
        # self.screen = game.screen
        # self.screen_rect = self.screen.get_rect()
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Tile_L:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.x = x
        self.y = y

        self.color = (100, 200, 250)

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

        self.blocks = []
        self.temp = []
        self.block_rects = []

        self.rightmove_possible = True
        self.leftmove_possible = True
        self.moving_right = False
        self.moving_left = False
        self.moving = True
    
    def create_tile_blocks(self):
        for i in self.tile_positions[0]:
            block = Block(i[0], i[1])
            self.temp.append(block)
        self.blocks = self.temp
        self.temp = []
 
    def check_bottom(self):
        for i in self.blocks:
            if i.rect.bottom >= self.screen_rect.bottom:
                self.moving = False
                return
       
    def check_turn(self):
        if self.posture == 0:
            print(0)
        if self.posture == 1:
            print(1)
        if self.posture == 2:
            print(2)
        if self.posture == 3:
            print(3)

    def update(self):
        
        self.posture = self.game.tile_posture
        # if self.game.tile_active:
        #     self.create_tile(self.posture)
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

            self.check_turn()
            self.check_bottom()
            
            if self.counter == self.game.drop_speed:
                for i in self.blocks:
                    i.rect.y += i.height

                self.counter = 0
                        
            
                    

            
    def drawme(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        for block in self.blocks:
            pygame.draw.rect(self.screen, self.color, block.rect)
            # pygame.draw.rect(self.screen, self.color, block.rect)
