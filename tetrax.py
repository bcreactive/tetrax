import pygame
import sys
from random import choice

from tile import Tile


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode((520, 720))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tetrax")
        self.bg_color = (0, 0, 0)

        self.play_field = pygame.Surface((400, 720))
        self.play_field_rect = pygame.Rect(0, 0, 400, 720)
        self.play_field_color = (100, 100, 100)
        self.play_field.fill(self.play_field_color)

        self.drop_speed = 40
        self.counter = 0

        self.x = 160
        self.y = 0
        self.tile_posture = 0

        self.moving_blocks = []
        self.static_blocks = []
        # self.moving_tile = []
        self.tiles = []

        self.tile_pool = ["L", "Rev_L", "Bloc", "Z", "Rev_Z", "Tri", "Bar"]
        self.next_tile = self.get_next_tile()

        self.tile = Tile(self, self.x, self.y, self.next_tile)
        self.tile.create_tile_blocks()

    def run_game(self):     
        while True:
            # if self.game_active:  
            if not self.moving_blocks:
                self.next_tile = self.get_next_tile()
                self.tile_posture = 0
                self.tile = Tile(self, self.x, self.y, self.next_tile)
                self.tile.create_tile_blocks()
                self.tiles.append(self.tile)
            self.check_events()
            self.check_bottom()
            
            self.tile_step()
            self.check_borders(self.play_field_rect)
            self.tile.update()
            self.check_turn()
            
            self.update_screen()
            self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     
            # if self.game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.tile.leftmove_possible and self.tile.moving:
                        self.x -= 40
                        for i in self.moving_blocks:
                            i.x -= 40
                    self.tile.moving_left = True
                        
                if event.key == pygame.K_RIGHT:
                    if self.tile.rightmove_possible and self.tile.moving:
                        self.x += 40
                        for i in self.moving_blocks:
                            i.x += 40
                    self.tile.moving_right = True
                         
                if event.key == pygame.K_m:
                    self.turn_right()

                if event.key == pygame.K_n:
                    self.turn_left()

    def get_next_tile(self):
        next_tile = choice(self.tile_pool)
        # self.posture = 0
        return next_tile

    def check_bottom(self):
        for i in self.moving_blocks:
            if i.bottom >= self.screen_rect.bottom:
                self.tile.moving = False
                for j in self.moving_blocks:
                    self.static_blocks.append(j)
                # self.static_tiles.append(self.current_tile) 
                self.moving_blocks = []  
                # self.current_tile = []
                self.x = 160
                self.y = 0
                # print(self.moving_blocks)
                # print(self.static_blocks)  
                return
        
    def tile_step(self):
        if self.tile.moving:  
            self.counter += 1
            if self.counter == self.drop_speed:          
                self.y += 40
                for i in self.moving_blocks:  
                    i.y += 40
                    self.counter = 0
            
    def check_borders(self, field_rect):
        for block in self.moving_blocks:
            if block.left <= field_rect.left:
                self.tile.leftmove_possible = False  
                return
            
            if block.right >= field_rect.right:
                self.tile.rightmove_possible = False  
                return  
                       
            if (block.left >= field_rect.left or
                block.right <= field_rect.right):
                self.tile.rightmove_possible = True
                self.tile.leftmove_possible = True

    def check_turn(self):
        pass

    def turn_right(self):
        if len(self.tile.tile_positions) == 4:     
            if not self.tile_posture > 3:
                self.tile_posture += 1 
            if self.tile_posture > 3:
                self.tile_posture = 0
            # print(len(self.tile.tile_positions))

        elif len(self.tile.tile_positions) == 2:
            if not self.tile_posture > 1:
                self.tile_posture += 1 
            if self.tile_posture > 1:
                self.tile_posture = 0
            # print(len(self.tile.tile_positions))

        elif len(self.tile.tile_positions) == 1:
            self.tile_posture = 0

        print(self.tile_posture)
        # if self.tile_posture == 3:
        #     self.tile_posture = 0
        # else:
        #     self.tile_posture += 1
            # print(len(self.tile.tile_positions))

    def turn_left(self):
        if len(self.tile.tile_positions) == 4:     
            if not self.tile_posture < 0:
                self.tile_posture -= 1 
            if self.tile_posture < 0:
                self.tile_posture = 3
            # print(len(self.tile.tile_positions))
        elif len(self.tile.tile_positions) == 2:
            if not self.tile_posture < 0:
                self.tile_posture -= 1 
            if self.tile_posture < 0:
                self.tile_posture = 1
            # print(len(self.tile.tile_positions))
        elif len(self.tile.tile_positions) == 1:
            self.tile_posture = 0
            # print(len(self.tile.tile_positions))
        print(self.tile_posture)

        # print(self.tile_posture)
        # if self.tile_posture == 0:
        #     self.tile_posture = 3
        # else:
        #     self.tile_posture -= 1

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.play_field, (0, 0))
        for block in self.moving_blocks:      
            pygame.draw.rect(self.screen, self.tile.color, block)
        for block in self.static_blocks:
            pygame.draw.rect(self.screen, self.tile.color, block)
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
