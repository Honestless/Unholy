import pygame
from random import randint, choice
from stats import stats
from battlesc import battle_screen, dungeonlevel
from icons import img
from globals import game
from buttons import buttons
from fontz import fontz as ft
from inventory import inventory
from my_quests import main_quest

class DoorActivity:
    pass
class DesperateWoman:
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        running = True
        while running:
            game.screen.blit(img.desperate_woman_part2, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_2.collidepoint(mx, my):
                        battle_screen()
class DragonTreasure:
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        main_quest.add_item("Dragon Treasure")
        running = True
        while running:
            game.screen.blit(img.dragon_treasure_intro, (200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        ActivityTypes.remove(DragonTreasure)
                        return NoActivity()
            pygame.display.update()

class Letter(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        running = True
        while running:
            game.screen.blit(img.kneeling_icon, (200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
            pygame.display.update()

class Hangman(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        running = True
        while running:
            game.screen.blit(img.hangman_icon, (200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
            pygame.display.update()
# Done
class Kneeling(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        main_quest.add_item("The Kneeling One")
        running = True
        while running:
            game.screen.blit(img.kneeling_icon, (200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        ActivityTypes.remove(Kneeling)
                        return NoActivity()
            pygame.display.update()
# Done
class Mercenary(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon

    def activate(self):
        running = True
        while running:
            game.screen.blit(img.mercenary_icon, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
# Done
class NextLevel(DoorActivity):
    def __init__(self):
        self.icon = img.next_level
        self.level = dungeonlevel.level

    def activate(self):
        self.level += 1
        stats.boost_gold(30)

class BonusHealth(DoorActivity):
    def __init__(self):
        self.icon = img.health_icon
        self.boost_health = stats.boost_health
        self.randint_value = randint(5, 10)

    def activate(self):
        self.boost_health(self.randint_value)
        return NoActivity()
# Done
class BonusExp(DoorActivity):

    def __init__(self):
        self.icon = img.exp_bonus_icon
        self.boost_xp = stats.boost_xp
        self.a = 4
        self.b = 8
        self.randint_value = randint(self.a, self.b)
        self.text = ft.font_20.render("You received " + str(self.randint_value) + " experience", True, game.white)

    def activate(self):
        self.boost_xp(self.randint_value)
        running = True
        while running:
            game.screen.blit(img.experience_icon, (200, 50))
            game.screen.blit(self.text, (240, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
            pygame.display.update()
# Done
class NoActivity(DoorActivity):
    def __init__(self):
        self.icon = None

    def activate(self):
        return self
# Done
class Gold(DoorActivity):
    def __init__(self):
        self.icon = img.gold_icon
        self.gold = stats.boost_gold
        self.a = 5
        self.b = 10
        self.random_value = randint(self.a, self.b)
        self.text = ft.font_20.render("You received " + str(self.random_value) + " Gold", True, game.white)

    def activate(self):
        self.gold(randint(5, 10))
        running = True
        while running:
            game.screen.blit(img.gold_event, (200, 50))
            game.screen.blit(self.text, (240, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
            pygame.display.update()
# Done
class Battle(DoorActivity):

    def __init__(self):
        self.icon = img.battle_icon

    def activate(self):
        battle_screen()
        return NoActivity()
# Done
class Looters(DoorActivity):

    def __init__(self):
        self.icon = img.looters_icon

    def activate(self):
        pass
        return NoActivity()

class Prisoners(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon
        self.boost_gold = stats.boost_gold
        self.a = 10
        self.b = 35
        self.randint_value = randint(self.a, self.b)
        self.c = 5
        self.d = 15
        self.randint_value2 = randint(self.c, self.d)
        self.ItemsFound = ["apple", "bread", "cheese", "smallpotion"]
        self.item_found = choice(self.ItemsFound)

    def activate(self):
        running = True
        while running:
            game.screen.blit(img.prisoners_image, (200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        mx, my = pygame.mouse.get_pos()
                        if buttons.choice_2.collidepoint(mx, my):
                            self.boost_gold(self.randint_value2)
                            inventory.add_item(self.item_found)
                            running = True
                            while running:
                                game.screen.blit(img.prisoners_image3, (200, 50))
                                game.screen.blit(ft.font_20.render(str(self.randint_value2) + " gold", True, game.white),
                                                 (280, 230))
                                game.screen.blit(ft.font_20.render(str(self.item_found), True, game.white),
                                                 (280, 250))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        mx, my = pygame.mouse.get_pos()
                                        if buttons.event_return.collidepoint(mx, my):
                                            return NoActivity()
                        if buttons.choice_1.collidepoint(mx, my):
                            self.boost_gold(self.randint_value)
                            running = True
                            while running:
                                game.screen.blit(img.prisoners_image2, (200, 50))
                                game.screen.blit(ft.font_20.render(str(self.randint_value) + " gold", True, game.white),
                                                 (280, 200))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        mx, my = pygame.mouse.get_pos()
                                        if buttons.event_return.collidepoint(mx, my):
                                            return NoActivity()
            pygame.display.update()
# Done
class Thief(DoorActivity):
    def __init__(self):
        self.icon = img.events_icon
        self.a = 5
        self.b = 30
        self.randint_value = randint(self.a, self.b)
        self.c = 1
        self.d = 8
        self.randint_value2 = randint(self.c, self.d)

    def activate(self):
        running = True
        stats.decrease_gold(self.randint_value)
        stats.decrease_health(self.randint_value2)
        while running:
            game.screen.blit(img.thief_image, (200, 50))
            game.screen.blit(ft.font_20.render(str(self.randint_value) + " gold", True, game.white),
                             (405, 225))
            game.screen.blit(ft.font_20.render(str(self.randint_value2) + " HP", True, game.white),
                             (390, 180))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        return NoActivity()
            pygame.display.update()
# Done
ActivityTypes = [Battle, Thief, Hangman, Letter, DragonTreasure, Gold, Prisoners, BonusExp,
                 Kneeling, NoActivity, Mercenary, BonusHealth, NoActivity, NoActivity, NoActivity,
                 NoActivity, NoActivity, NoActivity, NoActivity, NoActivity, NoActivity, NoActivity,
                 NoActivity, NoActivity, NoActivity, NoActivity,
                 ]
# ActivityTypes = []