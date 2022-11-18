import sys
import pygame
pygame.init()
from cards import Card
from cards import selected_cards_list
from cards import select_cards
from settings import Settings
from Board import Board_tile
from pawns import Blue_pieces
from pawns import Red_pieces
from pawns import Red_King
from pawns import Blue_King

class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Onitama")

    def event_checker(self):

    def key_down(self,event):



    def update_game(self):
        self._update_screen()

        tile_0.run_tiler()
        tile_1.run_tiler()
        tile_2.run_tiler()
        tile_3.run_tiler()
        tile_4.run_tiler()
        tile_5.run_tiler()
        tile_6.run_tiler()
        tile_7.run_tiler()
        tile_8.run_tiler()
        tile_9.run_tiler()
        tile_10.run_tiler()
        tile_11.run_tiler()
        tile_12.run_tiler()
        tile_13.run_tiler()
        tile_14.run_tiler()
        tile_15.run_tiler()
        tile_16.run_tiler()
        tile_17.run_tiler()
        tile_18.run_tiler()
        tile_19.run_tiler()
        tile_20.run_tiler()
        tile_21.run_tiler()
        tile_22.run_tiler()
        tile_23.run_tiler()
        tile_24.run_tiler()

        r1.draw()
        r2.draw()
        r3.draw()
        r4.draw()
        R.draw()
        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        B.draw()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

game = Game()
tile_0 = Board_tile(game, 0)
tile_1 = Board_tile(game, 1)
tile_2 = Board_tile(game, 2, False, True)
tile_3 = Board_tile(game, 3)
tile_4 = Board_tile(game, 4)
tile_5 = Board_tile(game, 5)
tile_6 = Board_tile(game, 6)
tile_7 = Board_tile(game, 7)
tile_8 = Board_tile(game, 8)
tile_9 = Board_tile(game, 9)
tile_10 = Board_tile(game, 10)
tile_11 = Board_tile(game, 11)
tile_12 = Board_tile(game, 12)
tile_13 = Board_tile(game, 13)
tile_14 = Board_tile(game, 14)
tile_15 = Board_tile(game, 15)
tile_16 = Board_tile(game, 16)
tile_17 = Board_tile(game, 17)
tile_18 = Board_tile(game, 18)
tile_19 = Board_tile(game, 19)
tile_20 = Board_tile(game, 20)
tile_21 = Board_tile(game, 21)
tile_22 = Board_tile(game, 22, False, True)
tile_23 = Board_tile(game, 23)
tile_24 = Board_tile(game, 24)

r1 = Red_pieces(1,5,'alive',game)
r2 = Red_pieces(2,5,'alive',game)
r3 = Red_pieces(4,5,'alive',game)
r4 = Red_pieces(5,5,'alive',game)
R = Red_King(3,5,'alive',game)

b1 = Blue_pieces(1,1,'alive',game)
b2 = Blue_pieces(2,1,'alive',game)
b3 = Blue_pieces(4,1,'alive',game)
b4 = Blue_pieces(5,1,'alive',game)
B = Blue_King(3,1,'alive',game)

r1.create_team(r2,r3,r4,R)
r2.create_team(r1,r3,r4,R)
r3.create_team(r1,r2,r4,R)
r4.create_team(r1,r2,r3,R)
R.create_team(r1,r2,r3,r4)

b1.create_team(b2,b3,b4,B)
b2.create_team(b1,b3,b4,B)
b3.create_team(b1,b2,b4,B)
b4.create_team(b1,b1,b3,B)
B.create_team(b1,b2,b3,b4)

r1.create_enemy_team(b1,b2,b3,b4,B)
r2.create_enemy_team(b1,b2,b3,b4,B)
r3.create_enemy_team(b1,b2,b3,b4,B)
r4.create_enemy_team(b1,b2,b3,b4,B)
R.create_enemy_team(b1,b2,b3,b4,B)

b1.create_enemy_team(r1,r2,r3,r4,R)
b2.create_enemy_team(r1,r2,r3,r4,R)
b3.create_enemy_team(r1,r2,r3,r4,R)
b4.create_enemy_team(r1,r2,r3,r4,R)
B.create_enemy_team(r1,r2,r3,r4,R)

game.update_game()
game_open = True
while game_open == True:
    pygame.display.flip()