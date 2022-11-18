import pygame.image


class Card:
    """This is the class for the cards and their stored movements"""

    def __init__(self,red_u, red_s,blue_u,blue_s, movement_A , movement_B,movement_C = (0,0),movement_D =(0,0) ):
        self.red_u = pygame.image.load(f'images/{red_u}')
        self.red_s = pygame.image.load(f'images/{red_s}')
        self.blue_u = pygame.image.load(f'images/{blue_u}')
        self.blue_s = pygame.image.load(f'images/{blue_s}')
        self.movement_A = movement_A
        self.movement_B = movement_B
        self.movement_C = movement_C
        self.movement_D = movement_D
        """ 
        The attributes to a card are the names of the four image files and the touples for their movements
        """

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




from random import randint
tiger = Card('TigerRU.png','TigerRS.png','TigerBU.png','TigerBS.png', (0, -2), (0, 1))
dragon = Card('DragonRU.png','DragonRS.png','DragonBU.png','DragonBS.png', (-2, -1), (2, -1), (-1, 1), (1, 1))
frog = Card('FrogRS.png','FrogRS.png','FrogBU.png','FrogBS.png', (-1, -1), (-2, 0), (1, 1))
rabbit = Card('RabbitRU.png','RabbitRS.png','RabbitBU.png','RabbitBS.png', (1, -1), (2, 0), (-1, 1))
crab = Card('CrabRU.png','CrabRS.png','CrabBU.png','CrabBS.png', (0, -1), (-2, 0), (2, 0))
elephant = Card('ElephantRU.png','ElephantRS.png','ElephantBU.png','ElephantBS.png', (-1, -1), (1, -1), (-1, 0), (1, 0))
goose = Card('GooseRU.png','GooseRS.png','GooseBU.png','GooseBS.png', (-1, -1), (-1, 0), (1, 0), (1, 1))
rooster = Card('RoosterRU.png','RoosterRS.png','RoosterBU.png','RoosterBS.png', (1, -1), (-1, 0), (1, 0), (-1, 1))
monkey = Card('MonkeyRU.png','MonkeyRS.png','MonkeyBU.png','MonkeyBS.png', (-1, -1), (1, -1), (1, 1), (-1, 1))
mantis = Card('MantisRU.png','MantisRS.png','MantisBU.png','MantisBS.png', (-1, -1), (1, -1), (0, 1))
horse = Card('HorseRU.png','HorseRS.png','HorseBU.png','HorseBS.png', (0, -1), (-1, 0), (0, 1))
ox = Card('OxRU.png','OxRS.png','OxBU.png','OxBS.png', (0, -1), (1, 0), (0, 1))
crane = Card('CraneRU.png','CraneRS.png','CraneBU.png','CraneBS.png', (0, -1), (-1, 1), (1, 1))
boar = Card('BoarRU.png','BoarRS.png','BoarBU.png','BoarBS.png', (0, 1), (-1, 0), (1, 0))
eel = Card('EelRU.png','EelRS.png','EelBU.png','EelBS.png', (-1, -1), (1, 0), (-1, 1))
cobra = Card('CobraRU.png','CobraRS.png','CobraBU.png','CobraBS.png', (1, -1), (-1, 0), (1, 1))

""" Card Selection"""

card_name_list = [tiger, dragon, frog, rabbit, crab, elephant, goose,
                  rooster, monkey, mantis, horse, ox, crane, boar, eel, cobra]
selected_cards_list = []
def select_cards():
    while len(selected_cards_list) != 5:
        i = randint(0, 15)
        random_card = card_name_list[i]
        if random_card not in selected_cards_list:
            selected_cards_list.append(random_card)
            # help done by Nathan Faust
select_cards()

