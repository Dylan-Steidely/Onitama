import pygame
pygame.init()
class Settings:
    """A class to store all setting to Onitama"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (10, 10, 10)

#import punch audio
punch = pygame.mixer.Sound("sound/Punch.wav")
chop = pygame.mixer.Sound("sound/Chop.wav")
Strong_hit = pygame.mixer.Sound("sound/Strong_hit.wav")
sounds = [punch, chop]

#import background music
song1 = 'sound/emo_rap.wav'
song2 = 'sound/japanese_song.wav'
song3 = 'sound/m&m.wav'
song_list = [song1, song2, song3]