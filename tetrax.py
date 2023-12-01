import pygame
import sys

# from block import Block
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

        self.drop_speed = 40
        self.counter = 0

        # Tile position
        self.x = 160
        self.y = 0

        self.tile_posture = 0
        self.moving_blocks = []
        self.static_blocks = []

        self.moving_tile = []

        self.game_active = False
        self.tile_active = False
        # self.create_tile(self.tile_1_pos[0])
        self.tile = Tile_L(self, self.x, self.y)
        self.tile.create_tile_blocks()
  
    def run_game(self):
        
        while True:
            # print(self.y)
            # if self.game_active:  
            ## if not self.moving_blocks:
            #     self.tile.create_tile(self.tile_posture) 
            self.check_events()
            self.check_borders(self.play_field_rect)
            self.update_posture()
            # self.check_drop()
            self.tile.update()
                     
            self.update_screen()
            self.clock.tick(self.fps)
            # self.check_drop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     

            # if self.game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.tile.leftmove_possible:
                        for i in self.tile.blocks:
                            i.x -= 40
                    self.tile.moving_left = True
                        
                if event.key == pygame.K_RIGHT:
                    if self.tile.rightmove_possible:
                        for i in self.tile.blocks:
                            i.x += 40
                    self.tile.moving_right = True
                         
                if event.key == pygame.K_m:
                    self.turn_right()

                if event.key == pygame.K_n:
                    self.turn_left()
                    
    def check_borders(self, field_rect):
        for block in self.tile.blocks:
            if block.rect.left <= field_rect.left:
                self.tile.leftmove_possible = False  
                # self.lock_left()
                return
            if block.rect.right >= field_rect.right:
                self.tile.rightmove_possible = False  
                # self.lock_right()    
                return             
            if (block.rect.left >= field_rect.left or
                block.rect.right <= field_rect.right):
                self.tile.rightmove_possible = True
                self.tile.leftmove_possible = True
                # self.unlock()

    # def check_drop(self):
    #     self.counter += 1
    #     if self.counter == self.drop_speed:
    #         self.y += 40 
    #         self.counter = 0    
    # def create_new_tile(self, tile_pos):
    #     for pos in tile_pos:
    #         block = Block(self, pos[0], pos[1])
    #         # self.moving_blocks.append(block)
    #         self.moving_tile.append(self.tile)

    def update_posture(self):
        pass

    def check_turn(self):
        pass

    def lock_left(self):
        self.tile.leftmove_possible = False        

    def lock_right(self):
        self.tile.rightmove_possible = False           

    def unlock(self):
        self.tile.rightmove_possible = True
        self.tile.leftmove_possible = True


    def turn_right(self):
        if self.tile_posture == 3:
            self.tile_posture = 0
        else:
            self.tile_posture += 1

    def turn_left(self):
        if self.tile_posture == 0:
            self.tile_posture = 3
        else:
            self.tile_posture -= 1


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
