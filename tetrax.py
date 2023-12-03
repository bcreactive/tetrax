import pygame
import sys

from tile_L import Tile_L


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

        self.tile = Tile_L(self, self.x, self.y)
        self.tile.create_tile_blocks()

    def run_game(self):     
        while True:
            # if self.game_active:  
            if not self.moving_blocks:
                self.tile.create_tile_blocks()
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

    def check_bottom(self):
        for i in self.moving_blocks:
            if i.bottom >= self.screen_rect.bottom:
                self.tile.moving = False
                for j in self.moving_blocks:
                    self.static_blocks.append(j)
                self.moving_blocks = []  
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
        for block in self.moving_blocks:      
            pygame.draw.rect(self.screen, self.tile.color, block)
        for block in self.static_blocks:
            pygame.draw.rect(self.screen, self.tile.color, block)
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
