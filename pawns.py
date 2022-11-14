#from cards import Card
#from cards import selected_cards_list
class Pieces:
    """ This class is for the 4 red and blue pawns and 1 red and blue king and will contain the following information: board location and status (alive vs. dead). """

    def __init__(self, x_location, y_location, status):
        """initailize the starting location in x and y, along with the status as alive"""
        self.x = x_location
        self.y = y_location
        self.status = status

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

    #def check status



class Red_pieces(Pieces):

    def __init__(self,x_location, y_location, status):
        super().__init__(x_location, y_location, status)
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


class Blue_pieces(Pieces):

    def __init__(self,x_location, y_location, status):
        super().__init__(x_location, y_location, status)



    def check_legal_move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        move_y = card.return_movment_Y(movement_letter)
        validity = True
        if move_x + self.x < 1 or move_x + self.x > 5:
            validity = False
        if move_y - self.y < 1 or move_y - self.y > 5:
            validity = False
        for team_member in self.team_piece_list:
            if move_x + self.x == team_member.positionX() and move_y - self.y == team_member.positionY():
                validity = False
        return validity
    def move(self, card, movement_letter):
        move_x = card.return_movment_X(movement_letter)
        self.x += move_x
        print(self.x)
        move_y = card.return_movment_Y(movement_letter)
        self.y -= move_y
        self.check_killed_opponents()

class Red_King(Red_pieces):

    def __init__(self,x_location, y_location, status):
        super().__init__(x_location, y_location, status)

class Blue_King(Blue_pieces):

    def __init__(self, x_location, y_location, status):
        super().__init__(x_location, y_location, status)





r1 = Red_pieces(1,5,'alive')
r2 = Red_pieces(2,5,'alive')
r3 = Red_pieces(3,5,'alive')
r4 = Red_pieces(4,5,'alive')
R = Red_pieces(5,5,'alive')

b1 = Blue_pieces(1,0,'alive')
b2 = Blue_pieces(2,0,'alive')
b3 = Blue_pieces(3,0,'alive')
b4 = Blue_pieces(4,0,'alive')
B = Blue_King(5,0,'alive')

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