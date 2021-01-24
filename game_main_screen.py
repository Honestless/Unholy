import pygame
from globals import game
from icons import img
from stats import stats
from lcrender import left_column
from buttons import buttons
from blacksmith import blacksmith
from market import market
from battlesc import battle_screen
from training_field import training_field
from character_menu import character_menu
from tavern import tavern
from dungeon import dungeon_level_01
from maps import game_map
from my_quests import my_quests

def game_main_screen():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.riverwood_ui, (0, 0))
        if stats.level <= 20:
            game.screen.blit(img.not_available, (602, 349))
        if stats.level <= 30:
            game.screen.blit(img.not_available, (602, 421))
        if stats.level <= 30:
            game.screen.blit(img.not_available, (388, 565))
        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.first_left_button.collidepoint(mx, my):
                        blacksmith()
                    if buttons.second_left_button.collidepoint(mx, my):
                        market()
                    if buttons.third_left_button.collidepoint(mx, my):
                        print("")
                    if buttons.fourth_left_button.collidepoint(mx, my):
                        battle_screen()
                    if buttons.first_right_button.collidepoint(mx, my):
                        training_field()
                    if buttons.second_right_button.collidepoint(mx, my):
                        character_menu()
                    if buttons.third_right_button.collidepoint(mx, my):
                        tavern()
                    if buttons.fourth_right_button.collidepoint(mx, my):
                        print("nic")
                    if buttons.dungeon_button.collidepoint(mx, my):
                        dungeon_level_01()
                    if buttons.map_button.collidepoint(mx, my):
                        game_map()
                    if buttons.my_quests_button.collidepoint(mx, my):
                        my_quests()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()