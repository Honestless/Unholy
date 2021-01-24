import pygame
WIDTH = 800
HEIGHT = 650
white = (255, 255, 255)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.white = white
        self.black = (0, 0, 0)

    def return_main(self):
        import game_main_screen as gms
        gms.game_main_screen()
game = Game()
