import pygame
import sys
from random import choice, randint
from time import sleep

from tile import Tile, Block
from score_field import Scorefield
from button import Button


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode((520, 720))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tetrax")

        self.color_sets = [
            # pos_0: playfield, pos_1 - pos_8: blocks, pos_9: blockborder

                            [
                            (27, 36, 71), (144, 82, 188), (238, 181, 156),
                            (212, 128, 187), (226, 178, 126), (180, 117, 56),
                            (114, 75, 44), (39, 137, 205), (250, 214, 255),
                            ], 

                            [
                            (73, 65, 130), (246, 162, 168), (178, 82, 102),
                            (138, 196, 195), (178, 139, 120), (150, 104, 136),
                            (246, 216, 150), (236, 225, 231), (201, 212, 253),
                            ], 
                        
                            [
                            (250, 214, 255), (94, 113, 142), (178, 139, 120),
                            (114, 75, 44), (100, 54, 75), (105, 91, 89),
                            (239, 221, 145), (178, 82, 102), (55, 52, 51)
                            ], 
                        
                            [
                            (144, 82, 188), (71, 114, 56), (97, 165, 63), 
                            (143, 208, 50), (196, 241, 41), (252, 247, 190), 
                            (151, 237, 202), (70, 84, 86), (238, 181, 156)
                            ], 
                        
                            [
                            (136, 163, 188), (40, 44, 60), (105, 102, 130),
                            (184, 204, 216), (138, 196, 195), (70, 84, 86),
                            (72, 104, 89), (134, 198, 154),(241, 242, 255),
                            ], 
                        
                            [
                            (76, 61, 46), (236, 235, 231), (166, 158, 154), 
                            (89, 87, 87), (40, 44, 60), (86, 79, 91), 
                            (101, 73, 86), (136, 110, 106), (66, 191, 232),
                            ], 
                        
                            [
                            (101, 73, 86), (27, 36, 71), (39, 137, 205), 
                            (66, 191, 232), (230, 231, 240), (138, 161, 246),
                            (73, 65, 130), (206, 170, 237), (246, 122, 168),
                            ], 

                            [
                            (42, 30, 35), (255, 240, 137), (211, 151, 65), 
                            (76, 61, 46), (198 , 133, 86), (246, 162, 168), 
                            (100, 54, 75), (238, 230, 234), (252, 247, 190),
                            ], 
                        ] 
        self.color_set = self.color_sets[randint(0, 7)]
        self.bg_color = (0, 0, 0)

        self.play_field = pygame.Surface((400, 720))
        self.play_field_rect = pygame.Rect(0, 0, 400, 720)
        self.play_field_color = self.color_set[0]
        self.play_field.fill(self.play_field_color)

        self.title_screen = pygame.image.load("images/title_screen.png")
        # self.title_screen_rect = pygame.Rect((0, 0, 520, 720))

        # self.level_sound = pygame.mixer_music.load("sound/song.mp3")
        self.drop_speed = 60
        self.counter = 0

        self.x = 160
        self.y = 0
        self.tile_posture = 0

        self.moving_blocks = []
        self.static_blocks = []

        # self.tile_pool = ["Bar"]
        self.tile_pool = ["L", "Rev_L", "Bloc", "Z", "Rev_Z", "Tri", "Bar"]

        self.line_counter = 9
        self.level = 1

        self.game_active = False
        self.game_over = False

        self.rightmove_possible = True
        self.leftmove_possible = True
        self.rightturn_possible = True
        self.leftturn_possible = True
        self.step_active = True
        self.waiting = False
        # self.endscreen_visible = False

        self.current_tile = self.get_next_tile()
        self.next_tile = self.get_next_tile()

        self.tile = Tile(self, self.x, self.y, self.current_tile)
        self.tile.create_tile_blocks()

        self.scorefield = Scorefield(self)
        self.button = Button(self, "Play!")

    def run_game(self):     
        while True:
            if self.game_over:
                self.game_active = False
                pygame.mouse.set_visible(True)

            self.check_events()

            if self.game_active:                     
                self.tile_step()
                self.tile.update()
                self.check_full_lines()
                self.check_max_heigth()
                self.check_borders(self.play_field_rect)
                
                if self.waiting:
                    self.wait_to_lock()
                    
                self.check_drop_collision()
                self.check_bottom()
                self.check_tile_sides()       

                if not self.game_over:
                    if not self.moving_blocks and not self.waiting:
                        self.create_new_tile()

                self.check_full_lines()
                # self.tile.update()

                self.scorefield.update()

            self.update_screen()
            self.clock.tick(self.fps)

    def check_events(self):
        # Check for user input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.rightmove_possible and self.tile.moving:
                        self.move_right()
                           
                if event.key == pygame.K_LEFT:
                    if self.leftmove_possible and self.tile.moving:
                        self.move_left()
                
                if event.key == pygame.K_DOWN:
                    if self.tile.moving:
                        self.step_active = False
                        self.tile.fast_drop = True

                if event.key == pygame.K_m:
                    self.turn_right()

                if event.key == pygame.K_n:
                    self.turn_left()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.tile.fast_drop = False
                    # self.counter = 0
                    # self.tile.correct_grid_pos()
                    self.step_active = True

    def check_play_button(self, mouse_pos):
        # Start game when button is clicked and reset game stats.
        if not self.game_active:
            if self.button.rect.collidepoint(mouse_pos):
                sleep(1)
                self.__init__()
            # #     self.points = 0
            # #     self.tracks = [1, 2, 3, 4, 5]
         
                pygame.mouse.set_visible(False)
                self.game_active = True    

                # pygame.mixer.Channel(0).play(
                #     pygame.mixer.Sound("sound/song.mp3"))  
    
    def get_next_tile(self):
        next_tile = choice(self.tile_pool)
        return next_tile

    def create_new_tile(self):
        self.x = 160
        self.y = 40
        self.current_tile = self.next_tile
        self.next_tile = self.get_next_tile()
        self.counter = 0
        # self.counter = -self.drop_speed
        self.tile_posture = 0
        self.tile = Tile(self, self.x, self.y, self.current_tile)
        self.tile.create_tile_blocks()
        self.rightmove_possible = True
        self.leftmove_possible = True
        self.rightturn_possible = True
        self.leftturn_possible = True
        self.waiting = False
        self.tile.fast_drop_possible = True
        self.step_active = True

    def wait_to_lock(self):
        if self.counter == self.drop_speed-1:
            for i in self.moving_blocks:
                if i.rect.bottom == self.screen_rect.bottom:
                    self.lock_tile()

            for block in self.moving_blocks:
                test_x = block.rect.x
                test_y = block.rect.y + 40
                testrect = pygame.Rect(test_x, test_y, 40, 40)

                for i in self.static_blocks:
                    if testrect.colliderect(i.rect):
                        self.lock_tile()
    
    def lock_tile(self):
        for j in self.moving_blocks:
            self.static_blocks.append(j)
        self.scorefield.prev_blocks = []
        self.moving_blocks = [] 
        self.x = 160
        self.y = 0
        self.waiting = False

    def check_bottom(self):
        for i in self.moving_blocks:
            if i.rect.bottom == self.screen_rect.bottom:

                if self.tile.fast_drop and self.tile.fast_drop_possible:
                    self.step_active = False
                    self.tile.fast_drop_possible = False
                    self.lock_tile()
                    self.create_new_tile()
                    return
                
                else:
                    self.waiting = True
                    self.tile.fast_drop_possible = False
                    self.step_active = False
                    return
            
        self.tile.fast_drop_possible = True
        self.step_active = True

    def check_drop_collision(self):
        blocks = self.moving_blocks[:]
        for block in blocks:
            test_x = block.rect.x
            test_y = block.rect.y + 40
            testrect = pygame.Rect(test_x, test_y, 40, 40)

            for i in self.static_blocks:
                if testrect.colliderect(i.rect):

                    if self.tile.fast_drop and self.tile.fast_drop_possible:
                        self.tile.fast_drop_possible = False
                        self.lock_tile()
                        self.create_new_tile()
                    else:
                        self.waiting = True
                        self.tile.fast_drop_possible = False
                        self.step_active = False
                        return 
                
                self.tile.fast_drop_possible = True
                self.step_active = True

    def check_max_heigth(self):
        for block in self.static_blocks:
            if block.rect.y <= 0:
                print("game over!")
                self.game_over = True
                self.game_active = False
                return
        
    def tile_step(self):
        if self.tile.moving: 
            self.counter += 1
            if self.counter > self.drop_speed:
                self.counter = self.drop_speed
            if self.counter == self.drop_speed:
                self.counter  = 0
                if self.step_active:          
                    self.y += 40
                    for i in self.moving_blocks:  
                        i.rect.y += 40

    def check_borders(self, field_rect):
        for block in self.moving_blocks:
            if block.rect.left <= field_rect.left:
                self.leftmove_possible = False  
                return
            
            if block.rect.right >= field_rect.right:
                self.rightmove_possible = False  
                return  
                       
            if (block.rect.left >= field_rect.left or
                block.rect.right <= field_rect.right):
                self.rightmove_possible = True
                self.leftmove_possible = True
        
    def check_tile_sides(self):
        self.check_right_move()  
        self.check_left_move()

    def check_right_move(self):
        testblocks = []  
        for i in self.moving_blocks:
            testblock = Block(self, i.rect.x + 40, i.rect.y, self.tile.side_len, 
                              self.tile)
            testblocks.append(testblock)
   
        for i in testblocks:
            for j in self.static_blocks:
                collision = pygame.Rect.colliderect(i.rect, j.rect)
                if collision:
                    self.rightmove_possible = False
                    return

    def check_left_move(self):
        testblocks = []       
        for i in self.moving_blocks:
            testblock = Block(self, i.rect.x - 40, i.rect.y, self.tile.side_len, 
                               self.tile)
            testblocks.append(testblock)

        for i in testblocks:
            for j in self.static_blocks:   
                collision = pygame.Rect.colliderect(i.rect, j.rect)
                if collision:
                    self.leftmove_possible = False
                    return
                
    def move_right(self):
        self.x += 40
        for i in self.moving_blocks:
            i.rect.x += 40

    def move_left(self):
        self.x -= 40
        for i in self.moving_blocks:
            i.rect.x -= 40

    def check_right_turn(self):
        testrects = []
        testblocks = []
        testposture = 0
        
        # Create the posture to get position for test-tile.
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

        # Create Rect objects with origin side length.        
        for i in self.tile.tile_positions[testposture]:
            testrect = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
            testrects.append(testrect)
        
        # Testing play-field borders.
        for i in testrects:          
            if (i.left < self.play_field_rect.left or
                i.right > self.play_field_rect.right):
                return False
            
        # Create Rect objects with smaller side length.
        for i in self.tile.tile_positions[testposture]:
            testblock = pygame.Rect(self.x + i[0]+1, self.y + i[1]+1, 38, 38)
            testblocks.append(testblock)
        
        # Checking for collision with other tiles when turning right.
        for i in testblocks:
            for j in self.static_blocks:
                collision = pygame.Rect.colliderect(i, j.rect)
                if collision:
                    return False
                
        return True
            
    def check_left_turn(self):
        testrects = []
        testblocks = []
        testposture = 0

        # Create the posture to get position for test-tile.
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
            
        # Create Rect objects with origin side length.
        for i in self.tile.tile_positions[testposture]:
            testrect = pygame.Rect(self.x + i[0], self.y + i[1], 40, 40)
            testrects.append(testrect)
        
        # Testing play-field borders.
        for i in testrects:
            if (i.left < self.play_field_rect.left or
                i.right > self.play_field_rect.right):
                return False
        
        # Create Rect objects with smaller side length.
        for i in self.tile.tile_positions[testposture]:
            testblock = pygame.Rect(self.x + i[0]+1, self.y + i[1]+1, 38, 38)
            testblocks.append(testblock)
        
        # Checking for collision with other tiles when turning left.
        for i in testblocks:
            for j in self.static_blocks:
                collision = pygame.Rect.colliderect(i, j.rect)
                if collision:
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

    def raise_level(self):
        # play level up sound
        self.level += 1

        if self.drop_speed > 5:
            if self.level <= 10:
                self.drop_speed -= 5
            elif self.level > 10:
                self.drop_speed -= 2
        else:
            self.drop_speed = 6

        self.update_block_colors()

    def update_block_colors(self):  
        self.color_set = self.color_sets[randint(0, 7)]        
        self.play_field_color = self.color_set[0]
        self.play_field.fill(self.play_field_color)

        self.scorefield.color = self.play_field_color
        self.scorefield.frame_color = self.color_set[8]
        self.scorefield.text_color = self.color_set[8]

        for i in self.static_blocks:
            i.color = i.get_color()

    def remove_line(self, rects):
        remove_rects = rects
        y = remove_rects[0].y

        for i in remove_rects:
            for j in self.static_blocks:
                if i == j.rect:
                    self.static_blocks.remove(j)

        self.line_counter += 1

        if self.line_counter % 10 == 0:
            self.raise_level()
        # self.points += self.level * 100
        self.drop_restblocks(y)

    def drop_restblocks(self, y):
        for i in self.static_blocks:
            if i.rect.y < y:
                i.rect.y += 40

    def check_full_lines(self):
        all_rects = self.create_all_rects()
        static_rects = self.create_static_rects()
        x = 17
        for i in range(17):
            testline = []
            for i in all_rects[x]:
                if i in static_rects and not i in testline:
                    testline.append(i)

            if len(testline) < 10:
                x -= 1
                continue

            if len(testline) == 10:
                self.remove_line(testline)
                x -= 1
                continue
            
    def create_all_rects(self):
        testrects = []
        linerects = []
        x = 0
        y = 0

        for i in range(18):
            for i in range(10):
                testrect = pygame.Rect(x, y, 40, 40)
                linerects.append(testrect)
                x += 40
            testrects.append(linerects)
            linerects = []
            x = 0
            y += 40

        return testrects

    def create_static_rects(self):
        rects = []
        for i in self.static_blocks:
            rects.append(i)
        return rects
       
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.play_field, (0, 0))
        self.scorefield.drawme()

        if not self.game_active:
            self.screen.blit(self.title_screen, (0, 0))
            self.button.draw_button()

        if self.game_active:
            for block in self.moving_blocks:      
                pygame.draw.rect(self.screen, block.color, block)
                pygame.draw.rect(self.screen, self.color_set[8], block,
                                 width=4)
            for block in self.static_blocks:
                pygame.draw.rect(self.screen, block.color, block)
                pygame.draw.rect(self.screen, self.color_set[8], block,
                                 width=4)

        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
