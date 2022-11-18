import pygame
import sys
pygame.init()
class Board_tile:
    """
    0  1  2  3  4
    5  6  7  8  9
    10 11 12 13 14
    15 16 17 18 19
    20 21 22 23 24
    this is an arrangement of how the tiles will look like.
    each tile is given a tile_number which references its position so that it can be referenced
    additionally there are 4 states a tile can be:
    unseleceted which is the default for a tile
    selected which is used for selecting a tile and also lets the user know where the 'cursor' is
    possible unselcted tile is used to show a tile is an avilable move for the selected card
    possible selected is a selceted tile that is a possible move
    """

    def __init__(self, game, tile_number,selected = False,temple = False):
        self.game = game #the name of the instance of the game class is inputted here
        self.tile = tile_number #tile reference number
        self.selected = selected #to know if tile is selected or not
        self.possible = False #if tile is possible move
        if temple == True:
            self.tile_image = pygame.image.load('images/templetile.png')
        else:
            self.tile_image = pygame.image.load('images/unselectedtile.png')  # unselected default image
        self.tile_image_rect = self.tile_image.get_rect() #image rect


    def _update_select(self):
        # This method checks if tile is selceted and updates the image
        if self.selected == True:
            self.tile_image = pygame.image.load('images/selectedtile.png')
        if self.selected == True and self.possible == True:
            self.tile_image = pygame.image.load('images/selectedpossibletile.png')

    def _update_possible(self):
        #this method checks if tile is possible move and updates the image
        if self.possible == True and self.selected != True:
            self.tile_image = pygame.image.load('images/possibletile.png')

    def arrange_tile(self):
        #this method places tiles in their respective positions
        if self.tile == 0:
            self.game.screen.blit(self.tile_image,(0,0))
        elif self.tile == 1:
            self.game.screen.blit(self.tile_image, (130, 0))
        elif self.tile == 2:
            self.game.screen.blit(self.tile_image, (260, 0))
        elif self.tile == 3:
            self.game.screen.blit(self.tile_image, (390, 0))
        elif self.tile == 4:
            self.game.screen.blit(self.tile_image, (520, 0))
        elif self.tile == 5:
            self.game.screen.blit(self.tile_image,(0,130))
        elif self.tile == 6:
            self.game.screen.blit(self.tile_image, (130, 130))
        elif self.tile == 7:
            self.game.screen.blit(self.tile_image, (260, 130))
        elif self.tile == 8:
            self.game.screen.blit(self.tile_image, (390, 130))
        elif self.tile == 9:
            self.game.screen.blit(self.tile_image, (520, 130))
        elif self.tile == 10:
            self.game.screen.blit(self.tile_image, (0, 260))
        elif self.tile == 11:
            self.game.screen.blit(self.tile_image, (130, 260))
        elif self.tile == 12:
            self.game.screen.blit(self.tile_image, (260, 260))
        elif self.tile == 13:
            self.game.screen.blit(self.tile_image, (390, 260))
        elif self.tile == 14:
            self.game.screen.blit(self.tile_image, (520, 260))
        elif self.tile == 15:
            self.game.screen.blit(self.tile_image, (0, 390))
        elif self.tile == 16:
            self.game.screen.blit(self.tile_image, (130, 390))
        elif self.tile == 17:
            self.game.screen.blit(self.tile_image, (260, 390))
        elif self.tile == 18:
            self.game.screen.blit(self.tile_image, (390, 390))
        elif self.tile == 19:
            self.game.screen.blit(self.tile_image, (520, 390))
        elif self.tile == 20:
            self.game.screen.blit(self.tile_image, (0, 520))
        elif self.tile == 21:
            self.game.screen.blit(self.tile_image, (130, 520))
        elif self.tile == 22:
            self.game.screen.blit(self.tile_image, (260, 520))
        elif self.tile == 23:
            self.game.screen.blit(self.tile_image, (390, 520))
        elif self.tile == 24:
            self.game.screen.blit(self.tile_image, (520, 520))


    def run_tiler(self):
        #method combines the check and the arrnagement methods to make a tiler that when looped will tile the board
        self._update_select()
        self._update_possible()
        self.arrange_tile()



