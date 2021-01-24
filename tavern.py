import pygame
from globals import game
from icons import img
from lcrender import left_column
from buttons import buttons
from tavern_quests_view import RandomQuestsGrid
from my_quests import my_quests
from main_quests_functions import the_kneeling_one

QUESTS_X = 200
QUESTS_Y = 200
def tavern():
    random_quest = RandomQuestsGrid(QUESTS_X, QUESTS_Y)
    running = True
    while running:
        game.screen.blit(img.tavern_ui, (0, 0))
        left_column.draw()
        random_quest.draw()
        if the_kneeling_one.quest_state is True:
            the_kneeling_one.part1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    random_quest.click(mx, my)
                    if buttons.back_button_left.collidepoint(mx, my):
                        game.return_main()
                    if buttons.my_quests_button.collidepoint(mx, my):
                        my_quests()
                    if buttons.quest_button.collidepoint(mx, my):
                        tavern()
                    if buttons.bounties_button.collidepoint(mx, my):
                        bounties_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.return_main()
        pygame.display.update()

def bounties_menu():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.tavern_ui, (0, 0))
        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.back_button_left.collidepoint(mx, my):
                        game.return_main()
                    if buttons.my_quests_button.collidepoint(mx, my):
                        my_quests()
                    if buttons.quest_button.collidepoint(mx, my):
                        tavern()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.return_main()
        pygame.display.update()