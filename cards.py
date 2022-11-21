import pygame.image


class Card:
    """This is the class for the cards and their stored movements"""

    def __init__(self,red_u, red_s,blue_u,blue_s, movement_A,game , movement_B,movement_C = (0,0),movement_D =(0,0),card_stack_pos = 0 ):
        self.red_u = pygame.image.load(f'images/{red_u}')
        self.red_s = pygame.image.load(f'images/{red_s}')
        self.blue_u = pygame.image.load(f'images/{blue_u}')
        self.blue_s = pygame.image.load(f'images/{blue_s}')
        self.game = game
        self.movement_A = movement_A
        self.movement_B = movement_B
        self.movement_C = movement_C
        self.movement_D = movement_D
        self.pos = card_stack_pos
        """ 
        The attributes to a card are the names of the four image files and the touples for their movements
        """

    def update_position(self, new_pos ):
        self.pos = new_pos

    def return_movment_X(self, movement_letter):
        if movement_letter == 'A':
            return self.movement_A[0]
        if movement_letter == 'B':
            return self.movement_B[0]
        if movement_letter == 'C':
            return self.movement_C[0]
        if movement_letter == 'D':
            return self.movement_D[0]

    def return_movment_Y(self, movement_letter):
        if movement_letter == 'A' :
            return self.movement_A[1]
        if movement_letter == 'B' :
            return self.movement_B[1]
        if movement_letter == 'C':
            return self.movement_C[0]
        if movement_letter == 'D':
            return self.movement_D[0]

    def draw_cards(self):
        if self.pos == 1:
            self.blue_u_rect = self.blue_u.get_rect()
            self.game.screen.blit(self.blue_u, (620,0))
        elif self.pos == 2:
            self.blue_u_rect = self.blue_u.get_rect()
            self.game.screen.blit(self.blue_u, (620,50))
        elif self.pos == 3:
            self._u_rect = self.blue_u.get_rect()
            #self.game.screen.blit(turn, (620,300))
        elif self.pos == 4:
            self.red_u_rect = self.red_u.get_rect()
            self.game.screen.blit(self.ered_u, (620,550))
        elif self.pos == 5:
            self.red_u_rect = self.red_u.get_rect()
            self.game.screen.blit(self.red_u, (620,600))







""" Card Selection"""

