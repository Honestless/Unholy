import pygame
import os
pygame.font.init()

class Fontz:
    def __init__(self):
        self.font_40 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 40)
        self.font_20 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 20)
        self.font_15 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 15)
        self.old_font_40 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 40)
        self.old_font_30 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 30)
        self.old_font_20 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 20)
        self.old_font_15 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 15)


fontz = Fontz()

