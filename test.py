import pygame
from settings import Settings
class test:  # NOQA E302
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # pulls game settings from the settings.py file (screen height and width)
        # creates the surface with specified dimensions
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # screen rect probably not needed so will be removed soon
        self.settings.screen_width = self.screen.get_rect().width
        # screen rect probably not needed so will be removed soon
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Onitama")
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('RED wins by Rock', True, (0,0,0))
        textRect = text.get_rect()
        print(textRect)
        textRect.center = (287 // 2, 33 // 2)
        self.screen.blit(text, textRect)

test1 = test()

test1

pygame.display.flip()