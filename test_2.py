import pygame
import sys

from block import Block
from tile_L import Tile_L


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode((520, 720))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Testris")
        self.bg_color = (0, 0, 0)

        self.play_field = pygame.Surface((400, 720))
        self.play_field_rect = pygame.Rect(0, 0, 400, 720)
        self.play_field_color = (100, 100, 100)
        self.play_field.fill(self.play_field_color)

        self.drop_speed = 20
        self.counter = 0

        # Tile position
        self.x = 160
        self.y = 0

        self.tile_posture = 0
        self.moving_blocks = []
        self.static_blocks = []

        self.game_active = False
        # self.create_tile(self.tile_1_pos[0])
        self.tile = Tile_L(self, self.x, self.y)
        self.tile.create_tile(self.tile_posture)
  
    def run_game(self):
        
        while True:
            # if not self.moving_blocks:
            #     self.create_new_tile(self.tile_1_pos[0])
            self.check_events()
            self.tile.update()
            # if self.game_active:
            # self.check_borders(self.play_field_rect)
            # self.check_turn()
            # self.check_drop()
            # for block in self.moving_blocks:  
            #     contact = block.check_bottom()
            #     if contact:
            #         for block in self.moving_blocks:
            #             block.moving = False
            #             self.static_blocks.append(block)
            #             self.moving_blocks.remove(block)
                # block.update()                      
            self.update_screen()
            self.clock.tick(self.fps)
            # self.check_drop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     

            # if self.game_active:
            buffer = []
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # if self.moving_blocks and not buffer:
                        if self.tile.leftmove_possible:
                            for i in self.tile.blocks:
                                i.x -= 40
                            buffer.append("event")
                        # for block in self.moving_blocks:
                        self.tile.moving_left = True
                        
                if event.key == pygame.K_RIGHT:
                    # if self.moving_blocks and not buffer:
                        # if self.moving_blocks[0].rightmove_possible:
                        if self.tile.rightmove_possible:
                            for i in self.tile.blocks:
                                i.x += 40
                            buffer.append("event")
                        # for block in self.moving_blocks:
                        self.tile.moving_right = True
                         
                if event.key == pygame.K_m:
                    self.turn_right()
                if event.key == pygame.K_n:
                    self.turn_left()
            buffer = []
                    
    def check_borders(self, field_rect):
        for block in self.moving_blocks:
            if block.rect.left <= field_rect.left:
                self.lock_left()
                return
            if block.rect.right >= field_rect.right:
                self.lock_right()    
                return             
            if (block.rect.left >= field_rect.left or
                block.rect.right <= field_rect.right):
                self.unlock()

    def create_new_tile(self, tile_pos):
        for pos in tile_pos:
            block = Block(self, pos[0], pos[1])
            self.moving_blocks.append(block)
    
    def check_turn(self):
        pass

    def check_drop(self):
        self.counter += 1
        if self.counter == self.drop_speed:
            if self.moving_blocks:
                self.t_y += 40
            self.counter = 0

    def lock_left(self):
        for i in self.moving_blocks:
            i.leftmove_possible = False        
        # print("left locked")

    def lock_right(self):
        for i in self.moving_blocks:
            i.rightmove_possible = False           
        # print("right locked") 

    def unlock(self):
        for i in self.moving_blocks:    
            i.rightmove_possible = True
            i.leftmove_possible = True
        # print("unlocked")

    def turn_right(self):
        if self.tile_posture == 3:
            self.tile_posture = 0
            # self.moving_blocks = []
            # self.create_tile(self.tile_1_pos[self.tile_posture])
        else:
            self.tile_posture += 1
        # for i in self.moving_blocks:
        #     self.moving_blocks.remove(i)
        # self.moving_blocks = []
        # self.create_tile(self.tile_1_pos[self.tile_posture])
            # block = Block(self, self.tile_1_pos[self.tile_posture][0], 
            #               self.tile_1_pos[self.tile_posture][1])
            # self.moving_blocks.append(block)
        # self.create_tile(self.tile_1_pos[self.tile_posture])
        # print(self.tile_posture)

    def turn_left(self):
        if self.tile_posture == 0:
            self.tile_posture = 3
            self.moving_blocks = []
            self.create_tile(self.tile_1_pos[self.tile_posture])
        else:
            self.tile_posture -= 1
            self.moving_blocks = []
            self.create_tile(self.tile_1_pos[self.tile_posture])

    # def create_tile(self, tile_pos):
    #     for pos in tile_pos:
    #         block = Block(self, pos[0], pos[1])
    #         self.moving_blocks.append(block)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.play_field, (0, 0))
        self.tile.drawme()
        # for block in self.moving_blocks:      
        #     block.drawme()
        # for block in self.static_blocks:
        #     block.drawme()
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
