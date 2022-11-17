
import pygame
pygame.init()
from cards import Card
from cards import selected_cards_list
from cards import select_cards
from settings import Settings
from Board import Board_tile

class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Onitama")

    def run_game(self):
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


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

game = Game()
tile_0 = Board_tile(game, 0)
tile_1 = Board_tile(game, 1)
tile_2 = Board_tile(game, 2)
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
tile_22 = Board_tile(game, 22)
tile_23 = Board_tile(game, 23)
tile_24 = Board_tile(game, 24)

game.run_game()

