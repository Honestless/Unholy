import pygame
from globals import game
from icons import img
from buttons import buttons, map_locations
from fontz import fontz
from stats import stats
from random import randint
from character_menu import maininventory

class TheKneelingOne:
    def __init__(self):
        self.name = "The Kneeling One"
        self.text = fontz.font_20.render("The Kneeling One", True, game.white)
        self.quest_state = False
        self.tavern_button = buttons.third_right_button
        self.exp_text = fontz.font_20.render("You received 20 XP", True, game.white)
        self.finished = False

    def loop(self):
        running = True
        while running:
            game.screen.blit(img.the_kneeling_one_intro, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        self.quest_state = True
                        return

    def click(self):
        if self.quest_state:
            mx, my = pygame.mouse.get_pos()
            if self.tavern_button.collidepoint(mx, my):
                the_kneeling_one.part1()

    def part1(self):
        running = True
        while running:
            game.screen.blit(img.the_kneeling_one_part1, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_1.collidepoint(mx, my):
                        return the_kneeling_one.part2()

    def part2(self):
        running = True
        while running:
            game.screen.blit(img.the_kneeling_one_part2, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_1.collidepoint(mx, my):
                        return the_kneeling_one.part3()

    def part3(self):
        running = True
        while running:
            game.screen.blit(img.the_kneeling_one_part3, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_1.collidepoint(mx, my):
                        return the_kneeling_one.part4()

    def part4(self):
        running = True
        while running:
            game.screen.blit(img.the_kneeling_one_part4, (200, 50))
            game.screen.blit(self.exp_text, (250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        self.finished = True
                        stats.boost_xp(20)
                        the_kneeling_one.remove_item()
                        game.return_main()

    def remove_item(self):
        if self.finished:
            from my_quests import main_quest
            main_quest.remove_item(self.name)

the_kneeling_one = TheKneelingOne()

class DragonTreasure:
    def __init__(self):
        self.name = "Dragon Treasure"
        self.quest_state = False
        self.finished = False
        self.text = fontz.font_15.render("Dragon Treasure", True, game.black)
        self.icon = img.quest_icon
        self.map_location = map_locations.one
        self.boost_gold = stats.boost_gold
        self.a = 80
        self.b = 110
        self.value = randint(self.a, self.b)
        self.gold_text = fontz.font_15.render(str(self.value) + " gold and a gold necklace were added to inventory.", True, game.white)

    def loop(self):
        running = True
        while running:
            game.screen.blit(img.dragon_treasure_quest, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        self.quest_state = True
                        return

    def draw(self):
        if self.quest_state:
            game.screen.blit(self.text, (430, 50))
            game.screen.blit(self.icon, (470, 70))

    def click(self):
        if self.quest_state:
            mx, my = pygame.mouse.get_pos()
            if self.map_location.collidepoint(mx, my):
                dragon_treasure.part1()

    def part1(self):
        running = True
        while running:
            game.screen.blit(img.dragon_treasure_part1, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.choice_1.collidepoint(mx, my):
                        dragon_treasure.part2()
                    if buttons.choice_2.collidepoint(mx, my):
                        dragon_treasure.part3()

    def part2(self):
        self.boost_gold(self.value)
        maininventory.add_item("Dragon Necklace")
        running = True
        while running:
            game.screen.blit(img.dragon_treasure_part2, (200, 50))
            game.screen.blit(self.gold_text, (270, 285))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        self.finished = True
                        dragon_treasure.remove_item()
                        game.return_main()

    def part3(self):
        running = True
        while running:
            game.screen.blit(img.dragon_treasure_part3, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        self.finished = True
                        dragon_treasure.remove_item()
                        game.return_main()

    def remove_item(self):
        if self.finished:
            from my_quests import main_quest
            main_quest.remove_item(self.name)

dragon_treasure = DragonTreasure()

def quest_03():
    pass