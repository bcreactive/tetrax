import pygame

from tile import Block


class Scorefield:
    def __init__(self, game):
        self.game = game

        # Font and color settings.
        self.color = (141, 90, 120)
        self.frame_color = (0, 0, 0)

        self.text_label_color = (10, 100, 100)
        self.text_color = (0, 0, 0)

        self.font = pygame.font.SysFont(None, 36)
        self.number_font = pygame.font.SysFont(None, 54)

        self.prev_tile = self.game.next_tile
        self.prev_blocks = []
        self.tile_positions = []

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

        self.level_y = 236
        self.level_heigth = 164
        self.level_img = pygame.Surface((1, 1))
        self.level_rect = pygame.Rect(0, 0, 0, 0)
        self.level_val_img = pygame.Surface((1, 1)) 
        self.level_val_rect = pygame.Rect(0, 0, 0, 0)
        
        self.lines_y = 396
        self.lines_heigth = 164
        self.lines_img = pygame.Surface((1, 1))
        self.lines_rect = pygame.Rect(0, 0, 0, 0)
        self.lines_val_img = pygame.Surface((1, 1)) 
        self.lines_val_rect = pygame.Rect(0, 0, 0, 0)

        self.empty_y = 556
        self.empty_heigth = 164

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
        self.create_prev_tile()
    
    def create_prev_tile(self):
        # Create tile blocks for preview-tile.
        self.tile_positions = []
        self.prev_x = 440
        self.prev_y = 100
        self.load_corr_pos()

        self.tile_positions = self.get_tile_position(self.prev_tile)

        for i in self.tile_positions[0]:
            block = Block(self.game, self.prev_x + i[0], self.prev_y + i[1], 20,
                          self.prev_tile)
            self.prev_blocks.append(block)

    def load_corr_pos(self):
        # Optimized positions for preview-tiles.
        if self.prev_tile == "Z" or self.prev_tile == "Rev_Z":
            self.prev_x = 450
            self.prev_y = 110
        elif self.prev_tile == "Rev_L":
            self.prev_x = 460
        elif self.prev_tile == "Bar":
            self.prev_x = 470
        elif self.prev_tile == "Bloc":
            self.prev_y = 110

    def get_tile_position(self, tile):
        if tile == "L":
            positions = [
                        [(0, 0),
                        (0, 20),
                        (0, 40),
                        (20, 40)],
                    
                        [(-20, 20),
                        (0, 20),
                        (20, 20),
                        (-20, 40)],
                    
                        [(-20, 0),
                        (0, 0),
                        (0, 20),
                        (0, 40)],
                        
                        [(-20, 20),
                        (0, 20),
                        (20, 20),
                        (20, 0)]     
                        ]
            return positions
            
        elif tile == "Rev_L":
            positions = [
                        [(0, 0),
                        (0, 20),
                        (0, 40),
                        (-20, 40)],
                    
                        [(-20, 0),
                        (-20, 20),
                        (0, 20),
                        (20, 20)],
                    
                        [(-20, 0),
                        (0, 0),
                        (-20, 20),
                        (-20, 40)],
                        
                        [(-20, 20),
                        (0, 20),
                        (20, 20),
                        (20, 40)]     
                        ]
            return positions
        
        elif tile == "Bloc":
            positions = [
                        [(0, 0),
                        (20, 0),
                        (0, 20),
                        (20, 20)]
                        ] 
            return positions
            
        elif tile == "Z":
            positions = [
                        [(-20, 0),
                        (0, 0),
                        (0, 20),
                        (20, 20)],
                    
                        [(20, 0),
                        (20, 20),
                        (0, 20),
                        (0, 40)]
                        ]
            return positions
            
        elif tile == "Rev_Z":
            positions = [
                        [(0, 0),
                        (20, 0),
                        (-20, 20),
                        (0, 20)],
                    
                        [(0, 0),
                        (0, 20),
                        (20, 20),
                        (20, 40)]
                        ]
            return positions
            
        elif tile == "Tri":
            positions = [
                        [(0, 0),
                        (0, 20),
                        (20, 20),
                        (0, 40)],
                    
                        [(-20, 20),
                        (0, 20),
                        (20, 20),
                        (0, 40)],
                    
                        [(0, 0),
                        (-20, 20),
                        (0, 20),
                        (0, 40)],
                        
                        [(0, 0),
                        (-20, 20),
                        (0, 20),
                        (20, 20)]     
                        ]
            return positions

        elif tile == "Bar":
            positions = [
                        [(-20, 0),
                        (-20, 20),
                        (-20, 40),
                        (-20, 60)],
                    
                        [(-40, 40),
                        (-20, 40),
                        (0, 40),
                        (20, 40)]
                        ]
            return positions
        
    def prep_level(self):
        # Get a rendered image with the level.
        self.level = self.game.level
        level_str = "Level:"
        self.level_img = self.font.render(level_str, True, self.text_color,
                                            self.color)   
           
        self.level_rect = self.level_img.get_rect()
        self.level_rect.center = self.level_srfc_rect.center
        self.level_rect.top = self.level_srfc_rect.y + 20

        self.level_val = f"{self.level}"
        self.level_val_img = self.number_font.render(
                            self.level_val, True, self.text_color,self.color)

        self.level_val_rect = self.level_val_img.get_rect()
        self.level_val_rect.center = self.level_srfc_rect.center
        self.level_val_rect.top = self.level_srfc_rect.y + 75

    def prep_lines(self):
        # Get a rendered image with the destroyed lines.
        self.lines = self.game.line_counter
        lines_str = "Lines:"
        self.lines_img = self.font.render(lines_str, True, self.text_color,
                                            self.color)   
        
        self.lines_rect = self.lines_img.get_rect()
        self.lines_rect.center = self.lines_srfc_rect.center
        self.lines_rect.top = self.lines_srfc_rect.y + 20

        self.lines_val = f"{self.lines}"
        self.lines_val_img = self.number_font.render(
                            self.lines_val, True, self.text_color, self.color)

        self.lines_val_rect = self.lines_val_img.get_rect()
        self.lines_val_rect.center = self.lines_srfc_rect.center
        self.lines_val_rect.top = self.lines_srfc_rect.y + 75

    def update(self):       
        self.prev_tile = self.game.next_tile
        self.prep_next()

        self.lines = self.game.line_counter
        self.prep_lines()

        self.level = self.game.level
        self.prep_level()

    def drawme(self):
        # Draw next tile.
        pygame.draw.rect(self.game.screen, self.color, self.next_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.next_srfc_rect, width=4)
        self.game.screen.blit(self.next_img, self.next_rect)

        for block in self.prev_blocks:      
            pygame.draw.rect(self.game.screen, block.color, block)
            pygame.draw.rect(self.game.screen, (0, 0, 0), block, width=2)
        
        # Draw current level.
        pygame.draw.rect(self.game.screen, self.color, self.level_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.level_srfc_rect, width=4)
        self.game.screen.blit(self.level_img, self.level_rect)
        self.game.screen.blit(self.level_val_img, self.level_val_rect)

        # Draw amount of destroyed lines.
        pygame.draw.rect(self.game.screen, self.color, self.lines_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.lines_srfc_rect, width=4)
        self.game.screen.blit(self.lines_img, self.lines_rect)
        self.game.screen.blit(self.lines_val_img, self.lines_val_rect)
        
        # Draw empty field.
        pygame.draw.rect(self.game.screen, self.color, self.empty_srfc_rect)
        pygame.draw.rect(self.game.screen, self.frame_color,
                         self.empty_srfc_rect, width=4)
        


