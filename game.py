import sys
import pygame
from settings import Settings
from Board import Board_tile
from pawns import Blue_pieces
from pawns import Red_pieces
from pawns import Red_King
from pawns import Blue_King
from cards import selected_cards_list
from cards import selected_cards_pos_init
pygame.init()
class Game:  # NOQA E302
    def __init__(self):
        # General game set up
        pygame.init()
        self.settings = Settings()  # pulls game settings from the settings.py file (screen height and width)
        # creates the surface with specified dimensions
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # screen rect probably not needed so will be removed soon
        self.settings.screen_width = self.screen.get_rect().width
        # screen rect probably not needed so will be removed soon
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Onitama")  # name of the game and window

        # the following are starting parameters when the game boots initially

        # this first pair does the s and y coordinate for the selector along with the corresponding tuple
        self.selected_tile_coord_x = 3
        self.selected_tile_coord_y = 3
        self.selected_tile_coord = (self.selected_tile_coord_x, self.selected_tile_coord_y)

        self.possible_coord = (0, 0)

        self.movement = ''

        # this is the initial card selector variable deterimines where the card selector will start from
        self.selected_card_var = 4

        # turn order can either be 'blue' or 'red' if not than this is going to break
        self.turn = 'red'
    def event_checker(self):  # NOQA E301

        # event checker duh
        # sorry that was rude. I just feel like this one is kinda obvious
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # I like to exit the game so that my teachers don't realize I am not taking notes ;)
            elif event.type == pygame.KEYDOWN:
                # I only put key down events cause it was the only one I needed
                self.key_down(event)
    def key_down(self, event): # NOQA E301
        # If the key down events are triggered they will be funneled into here
        # WASD is for the tile selector
        if event.key == pygame.K_d:
            self.selected_tile_mover(0, 1)
        elif event.key == pygame.K_s:
            self.selected_tile_mover(1, 0)
        elif event.key == pygame.K_w:
            self.selected_tile_mover(-1, 0)
        elif event.key == pygame.K_a:
            self.selected_tile_mover(0, -1)
        # UP and Down is for the card selector
        elif event.key == pygame.K_UP:
            self.selected_card_mover(-1)
        elif event.key == pygame.K_DOWN:
            self.selected_card_mover(1)
        elif event.key == pygame.K_1:
            self.movement = 'A'
            self.unpossible_tiler()
            self.possible_tiler(self.movement)
        elif event.key == pygame.K_2:
            self.movement = 'B'
            self.unpossible_tiler()
            self.possible_tiler(self.movement)
        elif event.key == pygame.K_3:
            self.movement = 'C'
            self.unpossible_tiler()
            self.possible_tiler(self.movement)
        elif event.key == pygame.K_4:
            self.movement = 'D'
            self.unpossible_tiler()
            self.possible_tiler(self.movement)
        elif event.key == pygame.K_SPACE:
            self.move(self.movement)
            for cards in selected_cards_list:
                # List of selected_cards for the game is in the selected cards list and this cycles through and checks their
                # position and see where they belong
                if cards.pos == 1:  # top card
                    cards.image = cards.blue_u
                    self.screen.blit(cards.image, (620, 0))
                elif cards.pos == 2:  # 2nd top card
                    cards.image = cards.blue_u
                    self.screen.blit(cards.image, (620, 55))
                elif cards.pos == 3 and self.turn == 'red':  # middle card for red
                    self.screen.blit(cards.red_u, (620, 300))  # NOQA E231
                elif cards.pos == 3 and self.turn == 'blue':  # middle card for blue
                    self.screen.blit(cards.blue_u, (620, 300))  # NOQA E231
                elif cards.pos == 4:  # 2nd to bottom
                    cards.image = cards.red_u
                    self.screen.blit(cards.image, (620, 545))
                elif cards.pos == 5:  # bottom card
                    cards.image = cards.red_u
                    self.screen.blit(cards.image, (620, 600))
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
    def draw_cards(self):  # NOQA E301
        # method drawing cards
        for cards in selected_cards_list:
            # List of selected_cards for the game is in the selected cards list and this cycles through and checks their
            # position and see where they belong
            if cards.pos == 1:  # top card
                if cards.selected:
                    cards.image = cards.blue_s
                else:
                    cards.image = cards.blue_u
                self.screen.blit(cards.image, (620, 0))
            elif cards.pos == 2:  # 2nd top card
                if cards.selected:
                    cards.image = cards.blue_s
                else:
                    cards.image = cards.blue_u
                self.screen.blit(cards.image, (620, 55))
            elif cards.pos == 3 and self.turn == 'red':  # middle card for red
                self.screen.blit(cards.red_u, (620,300)) # NOQA E231
            elif cards.pos == 3 and self.turn == 'blue':  # middle card for blue
                self.screen.blit(cards.blue_u, (620,300))  # NOQA E231
            elif cards.pos == 4:  # 2nd to bottom
                if cards.selected:
                    cards.image = cards.red_s
                else:
                    cards.image = cards.red_u
                self.screen.blit(cards.image, (620, 545))
            elif cards.pos == 5:  # bottom card
                if cards.selected:
                    cards.image = cards.red_s
                else:
                    cards.image = cards.red_u
                self.screen.blit(cards.image, (620, 600))
    def update_card_image(self):  # NOQA E301
        # this makes the 
        num = self.selected_card_var - 1
        selected_cards_list[num].selected = True
        # print(f'{selected_cards_list[num]} turned {selected_cards_list[num].selected}')
        self.draw_cards()
    def selected_card_mover(self,direction): # NOQA E301
        if self.turn == 'red':
           if self.selected_card_var + direction <= 3: # NOQA
               #print(self.selected_card_var) # NOQA
                print('false')# NOQA
           elif self.selected_card_var + direction >= 6:
              #print(self.selected_card_var)
                print('false')
           else:
               num = self.selected_card_var -1
               self.selected_card_var += direction
               selected_cards_list[num].selected = False
               #print(self.selected_card_var)
               self.update_card_image()
        if self.turn == 'blue':
           if self.selected_card_var + direction <= 0:
              print('false')
              #print(self.selected_card_var)
           elif self.selected_card_var + direction >= 3:
              print('false')
              #print(self.selected_card_var)
           else:
               num = self.selected_card_var - 1
               self.selected_card_var += direction
               selected_cards_list[num].selected = False
               # print(f'{selected_cards_list[num]} turned {selected_cards_list[num].selected}')
               #print(self.selected_card_var)
               self.update_card_image()
    def selected_tile_mover(self,direction_X,direction_Y):
        # This method is the movement for the tile selector it takes inputs from the event checker to get the x and y direction of movement
        # the following series of statements will check to make sure the selector remains on the board by checking the x and y positions
        if self.selected_tile_coord_x + direction_X >= 6 :
            print('false')
        elif self.selected_tile_coord_x + direction_X <= 0:
            print('false')
        elif self.selected_tile_coord_y + direction_Y >= 6:
            print('false')
        elif self.selected_tile_coord_y + direction_Y <= 0:
            print('false')
        else:
        # if it passes the checks above this series of if statements. addmitadly this is pretty ugly code but it gets the job done.
        # it checks the x,y touple to see which tile it is...for every tile on the board...yeah all 25. kinda stupid.
        # if i have time i will rework this to a for loop....if this is still here it is because i didn't have time.
            if self.selected_tile_coord == (1, 1):
                tile_0.remove_selection()
            elif self.selected_tile_coord == (1, 2):
                tile_1.remove_selection()
            elif self.selected_tile_coord == (1, 3):
                tile_2.remove_selection()
            elif self.selected_tile_coord == (1, 4):
                tile_3.remove_selection()
            elif self.selected_tile_coord == (1, 5):
                tile_4.remove_selection()
            if self.selected_tile_coord == (2, 1):
                tile_5.remove_selection()
            elif self.selected_tile_coord == (2, 2):
                tile_6.remove_selection()
            elif self.selected_tile_coord == (2, 3):
                tile_7.remove_selection()
            elif self.selected_tile_coord == (2, 4):
                tile_8.remove_selection()
            elif self.selected_tile_coord == (2, 5):
                tile_9.remove_selection()
            elif self.selected_tile_coord == (3, 1):
                tile_10.remove_selection()
            elif self.selected_tile_coord == (3, 2):
                tile_11.remove_selection()
            elif self.selected_tile_coord == (3, 3):
                tile_12.remove_selection()
            elif self.selected_tile_coord == (3, 4):
                tile_13.remove_selection()
            elif self.selected_tile_coord == (3, 5):
                tile_14.remove_selection()
            elif self.selected_tile_coord == (4, 1):
                tile_15.remove_selection()
            elif self.selected_tile_coord == (4, 2):
                tile_16.remove_selection()
            elif self.selected_tile_coord == (4, 3):
                tile_17.remove_selection()
            elif self.selected_tile_coord == (4, 4):
                tile_18.remove_selection()
            elif self.selected_tile_coord == (4, 5):
                tile_19.remove_selection()
            elif self.selected_tile_coord == (5, 1):
                tile_20.remove_selection()
            elif self.selected_tile_coord == (5, 2):
                tile_21.remove_selection()
            elif self.selected_tile_coord == (5, 3):
                tile_22.remove_selection()
            elif self.selected_tile_coord == (5, 4):
                tile_23.remove_selection()
            elif self.selected_tile_coord == (5, 5):
                tile_24.remove_selection()
            # now that the original tile is no longer selected it is time to change the touple and do the same for the new selected tile
            self.selected_tile_coord_x += direction_X
            self.selected_tile_coord_y += direction_Y
            self.selected_tile_coord = (self.selected_tile_coord_x, self.selected_tile_coord_y)
            if self.selected_tile_coord == (1, 1):
                tile_0.add_selection()
            elif self.selected_tile_coord == (1, 2):
                tile_1.add_selection()
            elif self.selected_tile_coord == (1, 3):
                tile_2.add_selection()
            elif self.selected_tile_coord == (1, 4):
                tile_3.add_selection()
            elif self.selected_tile_coord == (1, 5):
                tile_4.add_selection()
            if self.selected_tile_coord == (2, 1):
                tile_5.add_selection()
            elif self.selected_tile_coord == (2, 2):
                tile_6.add_selection()
            elif self.selected_tile_coord == (2, 3):
                tile_7.add_selection()
            elif self.selected_tile_coord == (2, 4):
                tile_8.add_selection()
            elif self.selected_tile_coord == (2, 5):
                tile_9.add_selection()
            elif self.selected_tile_coord == (3, 1):
                tile_10.add_selection()
            elif self.selected_tile_coord == (3, 2):
                tile_11.add_selection()
            elif self.selected_tile_coord == (3, 3):
                tile_12.add_selection()
            elif self.selected_tile_coord == (3, 4):
                tile_13.add_selection()
            elif self.selected_tile_coord == (3, 5):
                tile_14.add_selection()
            elif self.selected_tile_coord == (4, 1):
                tile_15.add_selection()
            elif self.selected_tile_coord == (4, 2):
                tile_16.add_selection()
            elif self.selected_tile_coord == (4, 3):
                tile_17.add_selection()
            elif self.selected_tile_coord == (4, 4):
                tile_18.add_selection()
            elif self.selected_tile_coord == (4, 5):
                tile_19.add_selection()
            elif self.selected_tile_coord == (5, 1):
                tile_20.add_selection()
            elif self.selected_tile_coord == (5, 2):
                tile_21.add_selection()
            elif self.selected_tile_coord == (5, 3):
                tile_22.add_selection()
            elif self.selected_tile_coord == (5, 4):
                tile_23.add_selection()
            elif self.selected_tile_coord == (5, 5):
                tile_24.add_selection()
            #this is the dumbest thing that works ever
    def possible_tiler(self,movement):
        num = self.selected_card_var - 1
        if self.turn == 'red':
            for piece in red_team:
                #print(piece)
                #print(self.selected_tile_coord)
               # print(piece.coord)
                if self.selected_tile_coord == piece.coord:
                    possible_coord_x = selected_cards_list[num].return_movment_X(movement) + self.selected_tile_coord_y
                    #print(possible_coord_x,selected_cards_list[num].return_movment_X(movement))
                    possible_coord_y = selected_cards_list[num].return_movment_Y(movement) + self.selected_tile_coord_x
                    #print(possible_coord_y,selected_cards_list[num].return_movment_Y(movement))
                    self.possible_coord = (possible_coord_y, possible_coord_x)
                    #print(self.possible_coord)
                    if self.possible_coord == (1, 1):
                         tile_0.possible = True
                         tile_0.update_possible()
                         tile_0.run_tiler()
                    elif self.possible_coord == (1, 2):
                         tile_1.possible = True
                         tile_1.update_possible()
                         tile_1.run_tiler()
                    elif self.possible_coord == (1, 3):
                         tile_2.possible = True
                         tile_2.update_possible()
                         tile_2.run_tiler()
                    elif self.possible_coord == (1, 4):
                         tile_3.possible = True
                         tile_3.update_possible()
                         tile_3.run_tiler()
                    elif self.possible_coord == (1, 5):
                         tile_4.possible = True
                         tile_4.update_possible()
                         tile_4.run_tiler()
                    elif self.possible_coord == (2, 1):
                         tile_5.possible = True
                         tile_5.update_possible()
                         tile_5.run_tiler()
                    elif self.possible_coord == (2, 2):
                         tile_6.possible = True
                         tile_6.update_possible()
                         tile_6.run_tiler()
                    elif self.possible_coord == (2, 3):
                         tile_7.possible = True
                         tile_7.update_possible()
                         tile_7.run_tiler()
                    elif self.possible_coord == (2, 4):
                         tile_8.possible = True
                         tile_8.update_possible()
                         tile_8.run_tiler()
                    elif self.possible_coord == (2, 5):
                         tile_9.possible = True
                         tile_9.update_possible()
                         tile_9.run_tiler()
                    elif self.possible_coord == (3, 1):
                         tile_10.possible = True
                         tile_10.update_possible()
                         tile_10.run_tiler()
                    elif self.possible_coord == (3, 2):
                         tile_11.possible = True
                         tile_11.update_possible()
                         tile_11.run_tiler()
                    elif self.possible_coord == (3, 3):
                         tile_12.possible = True
                         tile_12.update_possible()
                         tile_12.run_tiler()
                    elif self.possible_coord == (3, 4):
                         tile_13.possible = True
                         tile_13.update_possible()
                         tile_13.run_tiler()
                    elif self.possible_coord == (3, 5):
                         tile_14.possible = True
                         tile_14.update_possible()
                         tile_14.run_tiler()
                    elif self.possible_coord == (4, 1):
                         tile_15.possible = True
                         tile_15.update_possible()
                         tile_15.run_tiler()
                    elif self.possible_coord == (4, 2):
                         tile_16.possible = True
                         tile_16.update_possible()
                         tile_16.run_tiler()
                    elif self.possible_coord == (4, 3):
                         tile_17.possible = True
                         tile_17.update_possible()
                         tile_17.run_tiler()
                    elif self.possible_coord == (4, 4):
                         tile_18.possible = True
                         tile_18.update_possible()
                         tile_18.run_tiler()
                    elif self.possible_coord == (4, 5):
                         tile_19.possible = True
                         tile_19.update_possible()
                         tile_19.run_tiler()
                    elif self.possible_coord == (5, 1):
                         tile_20.possible = True
                         tile_20.update_possible()
                         tile_20.run_tiler()
                    elif self.possible_coord == (5, 2):
                         tile_21.possible = True
                         tile_21.update_possible()
                         tile_21.run_tiler()
                    elif self.possible_coord == (5, 3):
                         tile_22.possible = True
                         tile_22.update_possible()
                         tile_22.run_tiler()
                    elif self.possible_coord == (5, 4):
                         tile_23.possible = True
                         tile_23.update_possible()
                         tile_23.run_tiler()
                    elif self.possible_coord == (5, 5):
                         tile_24.possible = True
                         tile_24.update_possible()
                         tile_24.run_tiler()
        if self.turn == 'blue':
            for piece in blue_team:
                if self.selected_tile_coord == piece.coord:
                    possible_coord_x = -selected_cards_list[num].return_movment_X(movement) + self.selected_tile_coord_y
                    #print(possible_coord_x, selected_cards_list[num].return_movment_X(movement))
                    possible_coord_y = -selected_cards_list[num].return_movment_Y(movement) + self.selected_tile_coord_x
                    #print(possible_coord_y, selected_cards_list[num].return_movment_Y(movement))
                    self.possible_coord = (possible_coord_y, possible_coord_x)
                    self.possible_coord = (possible_coord_y, possible_coord_x)
                    if self.possible_coord == (1, 1):
                         tile_0.possible = True
                         tile_0.update_possible()
                         tile_0.run_tiler()
                    elif self.possible_coord == (1, 2):
                         tile_1.possible = True
                         tile_1.update_possible()
                         tile_1.run_tiler()
                    elif self.possible_coord == (1, 3):
                         tile_2.possible = True
                         tile_2.update_possible()
                         tile_2.run_tiler()
                    elif self.possible_coord == (1, 4):
                         tile_3.possible = True
                         tile_3.update_possible()
                         tile_3.run_tiler()
                    elif self.possible_coord == (1, 5):
                         tile_4.possible = True
                         tile_4.update_possible()
                         tile_4.run_tiler()
                    elif self.possible_coord == (2, 1):
                         tile_5.possible = True
                         tile_5.update_possible()
                         tile_5.run_tiler()
                    elif self.possible_coord == (2, 2):
                         tile_6.possible = True
                         tile_6.update_possible()
                         tile_6.run_tiler()
                    elif self.possible_coord == (2, 3):
                         tile_7.possible = True
                         tile_7.update_possible()
                         tile_7.run_tiler()
                    elif self.possible_coord == (2, 4):
                         tile_8.possible = True
                         tile_8.update_possible()
                         tile_8.run_tiler()
                    elif self.possible_coord == (2, 5):
                         tile_9.possible = True
                         tile_9.update_possible()
                         tile_9.run_tiler()
                    elif self.possible_coord == (3, 1):
                         tile_10.possible = True
                         tile_10.update_possible()
                         tile_10.run_tiler()
                    elif self.possible_coord == (3, 2):
                         tile_11.possible = True
                         tile_11.update_possible()
                         tile_11.run_tiler()
                    elif self.possible_coord == (3, 3):
                         tile_12.possible = True
                         tile_12.update_possible()
                         tile_12.run_tiler()
                    elif self.possible_coord == (3, 4):
                         tile_13.possible = True
                         tile_13.update_possible()
                         tile_13.run_tiler()
                    elif self.possible_coord == (3, 5):
                         tile_14.possible = True
                         tile_14.update_possible()
                         tile_14.run_tiler()
                    elif self.possible_coord == (4, 1):
                         tile_15.possible = True
                         tile_15.update_possible()
                         tile_15.run_tiler()
                    elif self.possible_coord == (4, 2):
                         tile_16.possible = True
                         tile_16.update_possible()
                         tile_16.run_tiler()
                    elif self.possible_coord == (4, 3):
                         tile_17.possible = True
                         tile_17.update_possible()
                         tile_17.run_tiler()
                    elif self.possible_coord == (4, 4):
                         tile_18.possible = True
                         tile_18.update_possible()
                         tile_18.run_tiler()
                    elif self.possible_coord == (4, 5):
                         tile_19.possible = True
                         tile_19.update_possible()
                         tile_19.run_tiler()
                    elif self.possible_coord == (5, 1):
                         tile_20.possible = True
                         tile_20.update_possible()
                         tile_20.run_tiler()
                    elif self.possible_coord == (5, 2):
                         tile_21.possible = True
                         tile_21.update_possible()
                         tile_21.run_tiler()
                    elif self.possible_coord == (5, 3):
                         tile_22.possible = True
                         tile_22.update_possible()
                         tile_22.run_tiler()
                    elif self.possible_coord == (5, 4):
                         tile_23.possible = True
                         tile_23.update_possible()
                         tile_23.run_tiler()
                    elif self.possible_coord == (5, 5):
                         tile_24.possible = True
                         tile_24.update_possible()
                         tile_24.run_tiler()
    def unpossible_tiler(self):
        if self.possible_coord == (1, 1):
            tile_0.unpossible()
            tile_0.run_tiler()
        elif self.possible_coord == (1, 2):
            tile_1.unpossible()
            tile_1.run_tiler()
        elif self.possible_coord == (1, 3):
            tile_2.unpossible()
            tile_2.run_tiler()
        elif self.possible_coord == (1, 4):
            tile_3.unpossible()
            tile_3.run_tiler()
        elif self.possible_coord == (1, 5):
            tile_4.unpossible()
            tile_4.run_tiler()
        elif self.possible_coord == (2, 1):
            tile_5.unpossible()
            tile_5.run_tiler()
        elif self.possible_coord == (2, 2):
            tile_6.unpossible()
            tile_6.run_tiler()
        elif self.possible_coord == (2, 3):
            tile_7.unpossible()
            tile_7.run_tiler()
        elif self.possible_coord == (2, 4):
            tile_8.unpossible()
            tile_8.run_tiler()
        elif self.possible_coord == (2, 5):
            tile_9.unpossible()
            tile_9.run_tiler()
        elif self.possible_coord == (3, 1):
            tile_10.unpossible()
            tile_10.run_tiler()
        elif self.possible_coord == (3, 2):
            tile_11.unpossible()
            tile_11.run_tiler()
        elif self.possible_coord == (3, 3):
            tile_12.unpossible()
            tile_12.run_tiler()
        elif self.possible_coord == (3, 4):
            tile_13.unpossible()
            tile_13.run_tiler()
        elif self.possible_coord == (3, 5):
            tile_14.unpossible()
            tile_14.run_tiler()
        elif self.possible_coord == (4, 1):
            tile_15.unpossible()
            tile_15.run_tiler()
        elif self.possible_coord == (4, 2):
            tile_16.unpossible()
            tile_16.run_tiler()
        elif self.possible_coord == (4, 3):
            tile_17.unpossible()
            tile_17.run_tiler()
        elif self.possible_coord == (4, 4):
            tile_18.unpossible()
            tile_18.run_tiler()
        elif self.possible_coord == (4, 5):
            tile_19.unpossible()
            tile_19.run_tiler()
        elif self.possible_coord == (5, 1):
            tile_20.unpossible()
            tile_20.run_tiler()
        elif self.possible_coord == (5, 2):
            tile_21.unpossible()
            tile_21.run_tiler()
        elif self.possible_coord == (5, 3):
            tile_22.unpossible()
            tile_22.run_tiler()
        elif self.possible_coord == (5, 4):
            tile_23.unpossible()
            tile_23.run_tiler()
        elif self.possible_coord == (5, 5):
            tile_24.unpossible()
            tile_24.run_tiler()

    def move(self, movement):
        if self.turn == 'red':
            for piece in red_team:
                if piece.coord == self.selected_tile_coord:
                    piece.move_r(selected_cards_list[self.selected_card_var-1], movement)
                    selected_cards_list[self.selected_card_var-1], selected_cards_list[2] =\
                        selected_cards_list[2], selected_cards_list[self.selected_card_var-1]
                    selected_cards_pos_init()
                    self.turn_changer()
                    self.update_game()
        elif self.turn == 'blue':
            for piece in blue_team:
                if piece.coord == self.selected_tile_coord:
                    #print(movement)
                    piece.move_b(selected_cards_list[self.selected_card_var-1], movement)

                    
                    selected_cards_list[self.selected_card_var-1], selected_cards_list[2] =\
                        selected_cards_list[2], selected_cards_list[self.selected_card_var-1]
                    selected_cards_pos_init()
                    self.turn_changer()
                    self.update_game()

    def turn_changer(self):
        if self.turn == 'red':
            self.turn = 'blue'
            self.selected_card_var = 1
        elif self.turn == 'blue':
            self.turn = 'red'
            self.selected_card_var = 4
    def update_game(self):
        # this is the encompassing method for the game instance to update the changing parameters
        self.update_screen()  #screen updates
        self.event_checker() # event checker
        self.draw_cards() #function that contiuosly draws the cards
        # more cancerous programming that could be solved with a for loop and a list
        #again if this is still here as a comment it is cause i bit off more than i could chew and couldn't fix everything
        # in my defense i am not a programming god.....yet?
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
        #oh god more
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
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        #screen fill with background color

#<= >= != == <== ==> ligatures >= <= == !=


game = Game()
#tile instances
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
tile_12 = Board_tile(game, 12,True)
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

#red piece instances
r1 = Red_pieces(1,5,'alive',game)
r2 = Red_pieces(2,5,'alive',game)
r3 = Red_pieces(4,5,'alive',game)
r4 = Red_pieces(5,5,'alive',game)
R = Red_King(3,5,'alive',game)
red_team = [ r1, r2, r3, r4, R]
#blue piece instances
b1 = Blue_pieces(1,1,'alive',game)
b2 = Blue_pieces(2,1,'alive',game)
b3 = Blue_pieces(4,1,'alive',game)
b4 = Blue_pieces(5,1,'alive',game)
B = Blue_King(3,1,'alive',game)
blue_team = [b1,b2,b3,b4,B]
#red recognition methods
r1.create_team(r2,r3,r4,R)
r2.create_team(r1,r3,r4,R)
r3.create_team(r1,r2,r4,R)
r4.create_team(r1,r2,r3,R)
R.create_team(r1,r2,r3,r4)
#blue recognition methods
b1.create_team(b2,b3,b4,B)
b2.create_team(b1,b3,b4,B)
b3.create_team(b1,b2,b4,B)
b4.create_team(b1,b1,b3,B)
B.create_team(b1,b2,b3,b4)
#enemy recognition method
r1.create_enemy_team(b1,b2,b3,b4,B)
r2.create_enemy_team(b1,b2,b3,b4,B)
r3.create_enemy_team(b1,b2,b3,b4,B)
r4.create_enemy_team(b1,b2,b3,b4,B)
R.create_enemy_team(b1,b2,b3,b4,B)
#enemy recognition method
b1.create_enemy_team(r1,r2,r3,r4,R)
b2.create_enemy_team(r1,r2,r3,r4,R)
b3.create_enemy_team(r1,r2,r3,r4,R)
b4.create_enemy_team(r1,r2,r3,r4,R)
B.create_enemy_team(r1,r2,r3,r4,R)


game_open = True
while game_open == True:
    game.update_game()
    pygame.display.flip()