

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
            return self.movement_A(0)
        if movement_letter == 'B':
            return self.movement_B(0)
        if movement_letter == 'C':
            return self.movement_C(0)
        if movement_letter == 'D':
            return self.movement_D(0)

    def return_movment_Y(self, movement_letter):
        if movement_letter == 'A':
            return self.movement_A(1)
        if movement_letter == 'B':
            return self.movement_B(1)
        if movement_letter == 'C':
            return self.movement_C(1)
        if movement_letter == 'D':
            return self.movement_D(1)

""" """