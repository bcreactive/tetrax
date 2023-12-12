import pygame


class Tile:
    def __init__(self, game, x, y, tile):
        self.game = game
        self.x = x
        self.y = y
        self.tile = tile
        self.side_len = 40

        self.drop_speed = game.drop_speed
        self.counter = 0
        self.posture = 0
        self.test_posture = 0
        
        self.tile_positions = self.get_tile_position(self.tile)

        self.moving_right = False
        self.moving_left = False
        self.fast_drop_possible = True
        self.fast_drop = False
        self.moving = True
    
    def get_tile_position(self, tile):
        if tile == "L":
            positions = [
                        [(0, 0),
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
                        (40, 0)]     
                        ]
            return positions
            
        elif tile == "Rev_L":
            positions = [[
                        (0, 0),
                        (0, 40),
                        (0, 80),
                        (-40, 80)],
                    
                        [(-40, 0),
                        (-40, 40),
                        (0, 40),
                        (40, 40)],
                    
                        [(-40, 0),
                        (0, 0),
                        (-40, 40),
                        (-40, 80)],
                        
                        [(-40, 40),
                        (0, 40),
                        (40, 40),
                        (40, 80)]     
                        ]
            return positions
        
        elif tile == "Bloc":
            positions = [[
                        (0, 0),
                        (40, 0),
                        (0, 40),
                        (40, 40)]
                        ] 
            return positions
            
        elif tile == "Z":
            positions = [[
                        (-40, 0),
                        (0, 0),
                        (0, 40),
                        (40, 40)],
                    
                        [(40, 0),
                        (40, 40),
                        (0, 40),
                        (0, 80)]
                        ]
            return positions
            
        elif tile == "Rev_Z":
            positions = [
                        [(0, 0),
                        (40, 0),
                        (-40, 40),
                        (0, 40)],
                    
                        [(0, 0),
                        (0, 40),
                        (40, 40),
                        (40, 80)]
                        ]
            return positions
            
        elif tile == "Tri":
            positions = [
                        [(0, 0),
                        (0, 40),
                        (40, 40),
                        (0, 80)],
                    
                        [(-40, 40),
                        (0, 40),
                        (40, 40),
                        (0, 80)],
                    
                        [(0, 0),
                        (-40, 40),
                        (0, 40),
                        (0, 80)],
                        
                        [(0, 0),
                        (-40, 40),
                        (0, 40),
                        (40, 40)]     
                        ]
            return positions

        elif tile == "Bar":
            positions = [
                        [(-40, 0),
                        (-40, 40),
                        (-40, 80),
                        (-40, 120)],
                    
                        [(-80, 80),
                        (-40, 80),
                        (0, 80),
                        (40, 80)]
                        ]
            return positions

    def create_tile_blocks(self):
        self.x = 160
        self.y = 0

        for i in self.tile_positions[0]:
            block = Block(self.game, self.x + i[0], self.y + i[1], self.side_len,
                          self.tile)
            self.game.moving_blocks.append(block)
            self.game.tile_posture = 0
        self.moving = True
    
    def update_tile_blocks(self):
        if not self.posture == self.game.tile_posture:
            self.posture = self.game.tile_posture

            if self.moving:
                self.game.moving_blocks = []
                # self.x = self.game.x
                # self.y = self.game.y   
                for i in self.tile_positions[self.posture]:
                    block = Block(self.game, self.x + i[0], self.y + i[1], self.side_len,
                                  self.tile)
                    self.game.moving_blocks.append(block)

    def check_fast_drop(self):   
        for i in self.game.moving_blocks:
            if i.rect.bottom == self.game.screen_rect.bottom:
                self.fast_drop_possible = False

        for i in self.game.moving_blocks:
            # test_x = block.rect.x
            # test_y = block.rect.y + 40
            # testrect = pygame.Rect(test_x, test_y, 40, 40)

            for j in self.game.static_blocks:
                if i.rect.colliderect(j.rect):
                    self.fast_drop_possible = False

        if self.fast_drop_possible and self.fast_drop and self.moving:
            self.game.y += 40
            
            for i in self.game.moving_blocks:
                i.rect.y += 40

    def correct_grid_pos(self):
        pass
        # print(self.game.moving_blocks[0].rect.y % self.side_len)
        # if self.game.moving_blocks[0].rect.y % self.side_len != 0:

        #     for i in self.game.moving_blocks:
        #         i.rect.y += 20

    def update(self): 
        self.x = self.game.x
        self.y = self.game.y  
        # if not self.fast_drop:  
        #     self.correct_grid_pos()
        self.check_fast_drop()   
        self.update_tile_blocks()


class Block:
    def __init__(self, game, x, y, side, tile):
        self.game = game
        self.piece = tile
        self.color = self.get_color()
        # self.border_color = self.game.color_set[9]
        self.rect = pygame.Rect((x, y, side, side))

    def get_color(self):
        if self.piece == "L":
            color = self.game.color_set[1]
            return color
        
        elif self.piece == "Rev_L":
            color = self.game.color_set[2]
            return color
        
        elif self.piece == "Bloc":
            color = self.game.color_set[3]
            return color
        
        elif self.piece == "Z":
            color = self.game.color_set[4]
            return color
        
        elif self.piece == "Rev_Z":
            color = self.game.color_set[5]
            return color
        
        elif self.piece == "Tri":
            color = self.game.color_set[6]
            return color
        
        elif self.piece == "Bar":
            color = self.game.color_set[7]
            return color
        
        