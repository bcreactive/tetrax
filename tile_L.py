import pygame


class Tile_L:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

        self.drop_speed = game.drop_speed
        self.counter = 0
        self.posture = 0
        
        self.tile_positions = [[(0, 0), 
                                (0, 40), 
                                (0, 80), 
                                (40, 80)],

                                [(-40, 40), 
                                (0, 40), 
                                (40, 40), 
                                (-40, 80)],

                                [(-40, 0), 
                                (0, 0), 
                                (0, 40), 
                                (0, 80)],

                                [(-40, 40), 
                                (0, 40), 
                                (40, 40), 
                                (40, 80)]     
                                ]
        
                                # [[(self.x, self.y), 
                                # (self.x, self.y+40), 
                                # (self.x, self.y+80), 
                                # (self.x+40, self.y+80)],

                                # [(self.x-40, self.y+40), 
                                # (self.x, self.y+40), 
                                # (self.x+40, self.y+40), 
                                # (self.x-40, self.y+80)],

                                # [(self.x-40, self.y), 
                                # (self.x, self.y), 
                                # (self.x, self.y+40), 
                                # (self.x, self.y+80)],

                                # [(self.x-40, self.y+40), 
                                # (self.x, self.y+40), 
                                # (self.x+40, self.y+40), 
                                # (self.x+40, self.y+80)]     
                                # ]

        self.color = (100, 200, 250)

        self.rightmove_possible = True
        self.leftmove_possible = True
        self.moving_right = False
        self.moving_left = False
        self.moving = True
    
    def create_tile_blocks(self):
        self.game.x = 160
        self.game.y = 0
        for i in self.tile_positions[0]:
            block = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
            self.game.moving_blocks.append(block)
        self.moving = True
    
    def update_tile_blocks(self):
        if not self.posture == self.game.tile_posture:
            self.posture = self.game.tile_posture

            if self.moving:
                self.game.moving_blocks = []
                for i in self.tile_positions[self.posture]:
                    block = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
                    self.game.moving_blocks.append(block)

    def update(self):       
        self.x = self.game.x
        self.y = self.game.y
        self.update_tile_blocks()

                    

