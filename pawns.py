#from cards import Card
#from cards import selected_cards_list
import pygame
class Pieces:
    """ This class is for the 4 red and blue pawns and 1 red and blue king and will contain the following information: board location and status (alive vs. dead). """

    def __init__(self, x_location, y_location, status,game):
        """initailize the starting location in x and y, along with the status as alive"""
        self.x = x_location
        self.y = y_location
        self.status = status
        self.game = game

    def positionX(self):
        return self.x
    def positionY(self):
        return self.y

    def kill(self):
        self.status = 'dead'
        self.x = 0
        self.y = 0
    def create_team(self, t1, t2, t3, t4):
        self.team_piece_list = [t1, t2, t3, t4]
        # allows piece to recognize other team_members

    def create_enemy_team(self, t1, t2, t3, t4,t5):
        self.enemy_piece_list = [t1, t2, t3, t4,t5]
        # allows piece to recognize enemy pieces

    def check_killed_opponents(self):
        for enemy in self.enemy_piece_list:
            if self.x == enemy.positionX() and + self.y == enemy.positionY():
                enemy.kill()




class Red_pieces(Pieces):

    def __init__(self,x_location, y_location, status,game):
        super().__init__(x_location, y_location, status,game)
        self.image = pygame.image.load('images/redpawn.png')
        self.image_rect = self.image.get_rect()
    def check_legal_move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        move_y = card.return_movment_Y(movement_letter)
        validity = True
        if move_x + self.x < 1 or move_x + self.x > 5:
            validity = False
        if move_y + self.y < 1 or move_y + self.y > 5:
            validity = False
        for team_member in self.team_piece_list:
            if move_x + self.x == team_member.positionX() and move_y + self.y == team_member.positionY():
                validity = False
        return validity

    def move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        self.x += move_x
        print(self.x)
        move_y = card.return_movment_Y(movement_letter)
        self.y += move_y
        self.check_killed_opponents()

    def draw(self):
        coordinate = (self.x,self.y)
        if coordinate == (1,1):
            self.game.screen.blit(self.image, (10, 10))
        elif coordinate == (2,1):
            self.game.screen.blit(self.image,(140,10))
        elif coordinate == (3, 1):
            self.game.screen.blit(self.image, (270, 10))
        elif coordinate == (4, 1):
            self.game.screen.blit(self.image, (400, 10))
        elif coordinate == (5, 1):
            self.game.screen.blit(self.image, (530, 10))
        elif coordinate == (1,2):
            self.game.screen.blit(self.image, (10, 140))
        elif coordinate == (2,2):
            self.game.screen.blit(self.image,(140,140))
        elif coordinate == (3, 2):
            self.game.screen.blit(self.image, (270, 140))
        elif coordinate == (4, 2):
            self.game.screen.blit(self.image, (400, 140))
        elif coordinate == (5, 2):
            self.game.screen.blit(self.image, (530, 140))
        elif coordinate == (1,3):
            self.game.screen.blit(self.image, (10, 270))
        elif coordinate == (2,3):
            self.game.screen.blit(self.image,(140,270))
        elif coordinate == (3, 3):
            self.game.screen.blit(self.image, (270, 270))
        elif coordinate == (4, 3):
            self.game.screen.blit(self.image, (400, 270))
        elif coordinate == (5, 3):
            self.game.screen.blit(self.image, (530, 270))
        elif coordinate == (1, 4):
            self.game.screen.blit(self.image, (10, 400))
        elif coordinate == (2, 4):
            self.game.screen.blit(self.image, (140, 400))
        elif coordinate == (3, 4):
            self.game.screen.blit(self.image, (270, 400))
        elif coordinate == (4, 4):
            self.game.screen.blit(self.image, (400, 400))
        elif coordinate == (5, 4):
            self.game.screen.blit(self.image, (530, 400))
        elif coordinate == (1, 5):
            self.game.screen.blit(self.image, (10, 530))
        elif coordinate == (2, 5):
            self.game.screen.blit(self.image, (140, 530))
        elif coordinate == (3, 5):
            self.game.screen.blit(self.image, (270, 530))
        elif coordinate == (4, 5):
            self.game.screen.blit(self.image, (400, 530))
        elif coordinate == (5, 5):
            self.game.screen.blit(self.image, (530, 530))


class Blue_pieces(Pieces):

    def __init__(self,x_location, y_location, status,game):
        super().__init__(x_location, y_location, status,game)
        self.image = pygame.image.load('images/bluepawn.png')


    def check_legal_move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        move_y = card.return_movment_Y(movement_letter)
        validity = True
        if move_x - self.x < 1 or move_x - self.x > 5:
            validity = False
        if move_y - self.y < 1 or move_y - self.y > 5:
            validity = False
        for team_member in self.team_piece_list:
            if move_x + self.x == team_member.positionX() and move_y - self.y == team_member.positionY():
                validity = False
        return validity
    def move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        self.x -= move_x
        print(self.x)
        move_y = card.return_movment_Y(movement_letter)
        self.y -= move_y
        self.check_killed_opponents()

    def draw(self):
        coordinate = (self.x,self.y)
        if coordinate == (1,1):
            self.game.screen.blit(self.image, (10, 10))
        elif coordinate == (2,1):
            self.game.screen.blit(self.image,(140,10))
        elif coordinate == (3, 1):
            self.game.screen.blit(self.image, (270, 10))
        elif coordinate == (4, 1):
            self.game.screen.blit(self.image, (400, 10))
        elif coordinate == (5, 1):
            self.game.screen.blit(self.image, (530, 10))
        elif coordinate == (1,2):
            self.game.screen.blit(self.image, (10, 140))
        elif coordinate == (2,2):
            self.game.screen.blit(self.image,(140,140))
        elif coordinate == (3, 2):
            self.game.screen.blit(self.image, (270, 140))
        elif coordinate == (4, 2):
            self.game.screen.blit(self.image, (400, 140))
        elif coordinate == (5, 2):
            self.game.screen.blit(self.image, (530, 140))
        elif coordinate == (1,3):
            self.game.screen.blit(self.image, (10, 270))
        elif coordinate == (2,3):
            self.game.screen.blit(self.image,(140,270))
        elif coordinate == (3, 3):
            self.game.screen.blit(self.image, (270, 270))
        elif coordinate == (4, 3):
            self.game.screen.blit(self.image, (400, 270))
        elif coordinate == (5, 3):
            self.game.screen.blit(self.image, (530, 270))
        elif coordinate == (1, 4):
            self.game.screen.blit(self.image, (10, 400))
        elif coordinate == (2, 4):
            self.game.screen.blit(self.image, (140, 400))
        elif coordinate == (3, 4):
            self.game.screen.blit(self.image, (270, 400))
        elif coordinate == (4, 4):
            self.game.screen.blit(self.image, (400, 400))
        elif coordinate == (5, 4):
            self.game.screen.blit(self.image, (530, 400))
        elif coordinate == (1, 5):
            self.game.screen.blit(self.image, (10, 530))
        elif coordinate == (2, 5):
            self.game.screen.blit(self.image, (140, 530))
        elif coordinate == (3, 5):
            self.game.screen.blit(self.image, (270, 530))
        elif coordinate == (4, 5):
            self.game.screen.blit(self.image, (400, 530))
        elif coordinate == (5, 5):
            self.game.screen.blit(self.image, (530, 530))

class Red_King(Red_pieces):

    def __init__(self,x_location, y_location, status,game):
        super().__init__(x_location, y_location, status,game)
        self.image = pygame.image.load('images/redking.png')

class Blue_King(Blue_pieces):

    def __init__(self, x_location, y_location, status,game):
        super().__init__(x_location, y_location, status,game)
        self.image = pygame.image.load('images/blueking.png')






