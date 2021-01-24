import pygame
from buttons import buttons
from globals import game
from icons import img
from dungeon_events import ActivityTypes, DesperateWoman

class Sinje:
    def __init__(self):
        self.quest_state = False
        self.finished = False
        self.img = img.desperate_woman_intro

    def loop(self):
        running = True
        while running:
            game.screen.blit(self.img, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_2.collidepoint(mx, my):
                        sinje.part1()
                    if buttons.event_return.collidepoint(mx, my):
                        return

    def part1(self):
        running = True
        while running:
            game.screen.blit(img.desperate_woman_part1, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_2.collidepoint(mx, my):
                        self.quest_state = True
                        ActivityTypes.append(DesperateWoman)
                        game.return_main()

sinje = Sinje()

class CriminalActivity:
    def __init__(self):
        self.quest_state = False
        self.finished = False

    def loop(self):
            running = True
            while running:
                game.screen.blit(img.criminal_activity_intro, (200, 50))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mx, my = pygame.mouse.get_pos()
                        if buttons.choice_2.collidepoint(mx, my):
                            sinje.part1()
                        if buttons.event_return.collidepoint(mx, my):
                            return

    def part1(self):
        running = True
        while running:
            game.screen.blit(img.criminal_activity_part1, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_2.collidepoint(mx, my):
                        self.quest_state = True
                        game.return_main()

criminal_activity = CriminalActivity()