import pygame
import sys
from random import choice

from tile import Tile, Block


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

        self.drop_speed = 60
        self.counter = 0

        self.x = 160
        self.y = 0
        self.tile_posture = 0

        # self.check_full_lines()

        self.moving_blocks = []
        self.static_blocks = []

        # self.tile_pool = ["Rev_Z"]
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
            
            self.check_events()

            self.check_borders(self.play_field_rect)
            self.check_drop_collision()
            self.check_bottom()
            self.tile_step()
            self.tile.update()
            # self.check_full_lines()
            
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
                            i.rect.x -= 40
                    self.tile.moving_left = True
                        
                if event.key == pygame.K_RIGHT:
                    if self.tile.rightmove_possible and self.tile.moving:
                        self.x += 40
                        for i in self.moving_blocks:
                            i.rect.x += 40
                    self.tile.moving_right = True
                
                if event.key == pygame.K_DOWN:
                    if self.tile.moving:
                        self.x += 40
                        for i in self.moving_blocks:
                            i.rect.y += 40
                         
                if event.key == pygame.K_m:
                    self.turn_right()

                if event.key == pygame.K_n:
                    self.turn_left()
                

    def get_next_tile(self):
        next_tile = choice(self.tile_pool)
        return next_tile

    def check_bottom(self):
        for i in self.moving_blocks:
            if i.rect.bottom >= self.screen_rect.bottom:
                self.tile.moving = False
                for j in self.moving_blocks:
                    self.static_blocks.append(j)
                self.moving_blocks = [] 
                self.x = 160
                self.y = 0
                return
            
    def check_drop_collision(self):
        for block in self.moving_blocks:
            test_x = block.rect.x
            test_y = block.rect.y + 40
            testrect = pygame.Rect(test_x, test_y, 40, 40)

            if testrect in self.static_blocks:
                self.tile.moving = False
                for j in self.moving_blocks:
                    self.static_blocks.append(j)
                self.moving_blocks = [] 
                self.x = 160
                self.y = 0
                testrect = ""
                return
    
    def tile_step(self):
        if self.tile.moving:  
            self.counter += 1
            if self.counter == self.drop_speed:          
                self.y += 40
                for i in self.moving_blocks:  
                    i.rect.y += 40
                    self.counter = 0
            
    def check_borders(self, field_rect):
        for block in self.moving_blocks:
            if block.rect.left <= field_rect.left:
                self.tile.leftmove_possible = False  
                return
            
            if block.rect.right >= field_rect.right:
                self.tile.rightmove_possible = False  
                return  
                       
            if (block.rect.left >= field_rect.left or
                block.rect.right <= field_rect.right):
                self.tile.rightmove_possible = True
                self.tile.leftmove_possible = True

    def check_right_turn(self):
        testrects = []
        testposture = 0
        
        if len(self.tile.tile_positions) == 4:     
            if not self.tile_posture == 3:
                testposture = self.tile_posture + 1 
            if self.tile_posture == 3:
                testposture = 0

        elif len(self.tile.tile_positions) == 2:
            if not self.tile_posture == 1:
                testposture = self.tile_posture + 1 
            if self.tile_posture == 1:
                testposture = 0
                
        for i in self.tile.tile_positions[testposture]:
            testrect = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
            testrects.append(testrect)
        
        for i in testrects:          
            if (i.left < self.play_field_rect.left or
                i.right > self.play_field_rect.right):
                # testposture = 0
                return False

        for i in self.static_blocks:
            for j in testrects:
                if i.rect.colliderect(j):
                    return False  
        return True
            
    def check_left_turn(self):
        testrects = []
        testposture = 0

        if len(self.tile.tile_positions) == 4:     
            if not self.tile_posture == 0:
                testposture = self.tile_posture - 1 
            if self.tile_posture == 0:
                testposture = 3
                
        elif len(self.tile.tile_positions) == 2:
            if not self.tile_posture == 0:
                testposture = self.tile_posture - 1 
            if self.tile_posture == 0:
                testposture = 1

        for i in self.tile.tile_positions[testposture]:
            testrect = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
            testrects.append(testrect)
        
        for i in testrects:
            if (i.left < self.play_field_rect.left or
                i.right > self.play_field_rect.right):
                # testposture = 0
                return False

        for i in self.static_blocks:
            for j in testrects:
                if i.rect.colliderect(j):
                    return False    
        return True 
            
    def turn_right(self):
        right_turn_possible = self.check_right_turn()
        if right_turn_possible:
            if len(self.tile.tile_positions) == 4:     
                if self.tile_posture >= 0:
                    self.tile_posture += 1 
                if self.tile_posture > 3:
                    self.tile_posture = 0

            elif len(self.tile.tile_positions) == 2:
                if self.tile_posture >= 0:
                    self.tile_posture += 1 
                if self.tile_posture > 1:
                    self.tile_posture = 0

    def turn_left(self):
        left_turn_possible = self.check_left_turn()
        if left_turn_possible:
            if len(self.tile.tile_positions) == 4:     
                if self.tile_posture >= 0:
                    self.tile_posture -= 1 
                if self.tile_posture < 0:
                    self.tile_posture = 3
                
            elif len(self.tile.tile_positions) == 2:
                if self.tile_posture >= 0:
                    self.tile_posture -= 1 
                if self.tile_posture < 0:
                    self.tile_posture = 1

    def check_side_move(self):
        pass

    def check_full_lines(self):
        # testrects = self.create_testrects()
        # index = 0
        # for i in testrects[index]:
        #     if i == self.static_blocks[i].rect:
                pass
        
    # def create_testrects(self):
    #     testrects = []
    #     linerects = []
    #     x = 0
    #     y = 0

    #     for i in range(18):
    #         for i in range(10):
    #             testrect = pygame.Rect(x, y, 40, 40)
    #             linerects.append(testrect)
    #             x += 40
    #         testrects.append(linerects)
    #         linerects = []
    #         x = 0
    #         y += 40

    #     return testrects

       
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.play_field, (0, 0))
        for block in self.moving_blocks:      
            pygame.draw.rect(self.screen, block.color, block)
            pygame.draw.rect(self.screen, (0, 0, 0), block, width=3)
        for block in self.static_blocks:
            pygame.draw.rect(self.screen, block.color, block)
            pygame.draw.rect(self.screen, (0, 0, 0), block, width=3)
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
