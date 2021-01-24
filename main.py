import pygame
import os
from buttons import buttons
from globals import game
from icons import img
from tips import tips
from game_main_screen import game_main_screen
pygame.init()
pygame.display.set_caption("Unholy: A chosen Hero")
pygame.display.set_icon(pygame.image.load(os.path.join('unholy_logo.ico')))
clock = pygame.time.Clock()
FPS = 1

def main_menu():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.main_menu_ui, (0, 0))
        tips.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if buttons.new_game_menu_button.collidepoint(mx, my):
                        game_intro()
                    if buttons.options_menu_button.collidepoint(mx, my):
                        options_menu()
                    if buttons.credits_menu_button.collidepoint(mx, my):
                        credits_menu()
                    if buttons.quit_menu_button.collidepoint(mx, my):
                        quit()

def credits_menu():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.credits_ui, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if buttons.options_menu_button.collidepoint(mx, my):
                        return

def options_menu():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.options_ui, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if buttons.new_game_menu_button.collidepoint(mx, my):
                        print("Audio")
                    if buttons.options_menu_button.collidepoint(mx, my):
                        print("Video")
                    if buttons.credits_menu_button.collidepoint(mx, my):
                        return

def game_intro():
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.game_intro_ui, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.credits_menu_button.collidepoint(mx, my):
                        game_main_screen()

main_menu()
