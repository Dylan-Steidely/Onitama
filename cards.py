

class Card:
    """This is the class for the cards and their stored movements"""

    def __init__(self, name, movement_A , movement_B,movement_C = (0,0),movement_D =(0,0) ):
        self.name = name
        self.movement_A = movement_A
        self.movement_B = movement_B
        self.movement_C = movement_C
        self.movement_D = movement_D

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

    def return_card_name(self):
        return self.name


from random import randint
tiger = Card('Tiger', (0, -2), (0, 1))
dragon = Card('Dragon', (-2, -1), (2, -1), (-1, 1), (1, 1))
frog = Card('Frog', (-1, -1), (-2, 0), (1, 1))
rabbit = Card('Rabbit', (1, -1), (2, 0), (-1, 1))
crab = Card('Crab', (0, -1), (-2, 0), (2, 0))
elephant = Card('Elephant', (-1, -1), (1, -1), (-1, 0), (1, 0))
goose = Card('Goose', (-1, -1), (-1, 0), (1, 0), (1, 1))
rooster = Card('Rooster', (1, -1), (-1, 0), (1, 0), (-1, 1))
monkey = Card('Monkey', (-1, -1), (1, -1), (1, 1), (-1, 1))
mantis = Card('Mantis', (-1, -1), (1, -1), (0, 1))
horse = Card('Horse', (0, -1), (-1, 0), (0, 1))
ox = Card('Ox', (0, -1), (1, 0), (0, 1))
crane = Card('Crane', (0, -1), (-1, 1), (1, 1))
boar = Card('Boar', (0, 1), (-1, 0), (1, 0))
eel = Card('Eel', (-1, -1), (1, 0), (-1, 1))
cobra = Card('Cobra', (1, -1), (-1, 0), (1, 1))

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

