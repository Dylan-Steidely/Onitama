import sys
import pygame
pygame.init()
from random import randint
from cards import Card

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

card_name_list = ['tiger', 'dragon', 'frog', 'rabbit', 'crab', 'elephant', 'goose',
                  'rooster', 'monkey', 'mantis', 'horse', 'ox', 'crane', 'boar', 'eel', 'cobra']
def select_cards():
    selected_cards_list = []
    while len(selected_cards_list) != 5:
        i = randint(0, 15)
        random_card = card_name_list[i]
        if random_card not in selected_cards_list:
            selected_cards_list.append(random_card)
select_cards()
class Picture():
    def __init__(self,image_address):
