import pygame
from globals import game
from icons import img
import main_quests_functions as mqf
from buttons import buttons
def game_map():
    running = True
    while running:
        game.screen.blit(img.main_map, (50, 50))
        mqf.dragon_treasure.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                mqf.dragon_treasure.click()
                if buttons.map_button.collidepoint(mx, my):
                    return