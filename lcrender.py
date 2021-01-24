import pygame
import os
from globals import game
from stats import stats
from fontz import fontz
from icons import img
class LeftColumnRender:
    def __init__(self):
        self.game = game
        self.pygame = pygame

    def draw(self):
        self.health_px = (stats.health / stats.max_health) * 135
        self.xp_px = (stats.exp / stats.max_exp) * 134
        self.armor_px = (stats.armor / stats.max_armor) * 134
        self.res_health_bar = pygame.transform.scale(img.health_bar, (int(self.health_px), 34))
        self.armor_bar = pygame.transform.scale(pygame.image.load(os.path.join('images', 'armor_bar.png')),
                                                (int(self.armor_px), 24))
        self.res_exp_bar = pygame.transform.scale(img.exp_bar, (int(self.xp_px), 26))
        self.level_text = fontz.font_20.render("Level:  " + str(stats.level), True, game.white)
        self.gold_text = fontz.font_20.render("Gold:  " + str(stats.gold), True, game.white)
        self.day_text = fontz.font_20.render("Day:  " + str(stats.day), True, game.white)
        self.health_text = fontz.font_20.render("HP:  " + str(stats.health), True, game.white)
        self.armor_text = fontz.font_20.render("Armor:  " + str(stats.armor), True, game.white)
        self.exp_text = fontz.font_20.render("Exp:  " + str(stats.exp), True, game.white)
        self.attack_text = fontz.font_15.render("Att:  " + str(stats.attack), True, game.white)
        self.defence_text = fontz.font_15.render("Def:  " + str(stats.defence_level), True, game.white)
        self.strength_text = fontz.font_15.render("Str:  " + str(stats.strength_level), True, game.white)
        self.quests_text = fontz.font_20.render("My Quests", True, game.white)
        self.bounties_text = fontz.font_20.render("My bounties", True, game.white)
        self.game.screen.blit(img.blank_bar, (1, 50))
        self.game.screen.blit(self.res_health_bar, (1, 50))
        self.game.screen.blit(img.blank_bar, (1, 83))
        self.game.screen.blit(self.armor_bar, (1, 89))
        self.game.screen.blit(img.blank_bar, (1, 115))
        self.game.screen.blit(self.res_exp_bar, (1, 118))
        self.game.screen.blit(self.health_text, (20, 54))
        self.game.screen.blit(self.armor_text, (20, 88))
        self.game.screen.blit(self.exp_text, (20, 118))
        self.game.screen.blit(self.level_text, (15, 165))
        self.game.screen.blit(self.gold_text, (15, 205))
        self.game.screen.blit(self.day_text, (15, 245))
        self.game.screen.blit(img.attack_icon, (3, 286))
        self.game.screen.blit(img.defence_icon, (3, 328))
        self.game.screen.blit(img.strength_icon, (3, 369))
        self.game.screen.blit(self.attack_text, (35, 289))
        self.game.screen.blit(self.defence_text, (35, 331))
        self.game.screen.blit(self.strength_text, (35, 372))
        self.game.screen.blit(self.quests_text, (20, 412))
        self.game.screen.blit(self.bounties_text, (5, 453))
left_column = LeftColumnRender()
