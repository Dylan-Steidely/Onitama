import sys
import pygame

from settings import Settings
class Onitama:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Onitama")

        def run_game(self):
            """Start the main loop for the game."""

            while True:
                #Watch for keyboard and mouse events.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                #Redraw teh screen each pass through the loop
                self.screen.fill(self.settings.bg_color)

                pygame.dispaly.flip()