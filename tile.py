import pygame


class Tile:
    def __init__(self, game, x, y, tile):
        self.game = game
        self.x = x
        self.y = y
        self.tile = tile

        self.drop_speed = game.drop_speed
        self.counter = 0
        self.posture = 0
        self.test_posture = 0
        
        self.tile_positions = self.get_tile_position(self.tile)

        # self.rightturn_possible = True
        # self.leftturn_possible = True
        # self.rightmove_possible = True
        # self.leftmove_possible = True
        self.moving_right = False
        self.moving_left = False
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
            block = Block(self.x + i[0], self.y + i[1], self.tile)
            self.game.moving_blocks.append(block)
            self.game.tile_posture = 0
        self.moving = True
    
    def update_tile_blocks(self):
        if not self.posture == self.game.tile_posture:
            self.posture = self.game.tile_posture

            if self.moving:
                self.game.moving_blocks = []
                for i in self.tile_positions[self.posture]:
                    block = Block(self.x + i[0], self.y + i[1], self.tile)
                    self.game.moving_blocks.append(block)

    def update(self):       
        self.x = self.game.x
        self.y = self.game.y
        self.update_tile_blocks()


class Block:
    def __init__(self, x, y, tile):
        self.color = self.get_color(tile)
        self.rect = pygame.Rect((x, y, 40, 40))

    def get_color(self, tile):
        if tile == "L":
            color = (221, 0, 0)
            return color
        
        elif tile == "Rev_L":
            color = (0, 221, 0)
            return color
        
        elif tile == "Bloc":
            color = (221, 0, 221)
            return color
        
        elif tile == "Z":
            color = (221, 221, 0)
            return color
        
        elif tile == "Rev_Z":
            color = (0, 0, 221)
            return color
        
        elif tile == "Tri":
            color = (0, 221, 221)
            return color
        
        elif tile == "Bar":
            color = (221, 221, 221)
            return color
        