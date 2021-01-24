import pygame
from buttons import buttons
from globals import game
from icons import img
from lcrender import left_column
from random import choice, randint
from inventory import InventoryGrid
from stats import stats
from fontz import fontz
import time
INV_X = 150
INV_Y = 510

class Timer:
    def __init__(self):
        self.lastTime = time.time()

    def getTime(self):
        return time.time() - self.lastTime

    def resetTime(self):
        self.lastTime = time.time()

showTextTime = Timer()

def lost_game():
    if stats.health <= 0:
        running = True
        while running:
            game.screen.blit(img.battle_lost, (200, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.event_return.collidepoint(mx, my):
                        stats.boost_health(randint(5, 15))
                        stats.boost_day(1)
                        game.return_main()

# [219, 439, 669]  >>>> y = 90 also put the choice inside the loop to pick more enemies

class DungeonLevel:
    def __init__(self):
        self.level = 1
        self.game = game
        self.battle = 0
        self.battle_max = 3
        self.level_text = None
        self.battle_text = None

    def increase_battle_level(self, value):
        self.battle = self.battle + value

    def draw(self):
        self.level_text = fontz.font_40.render("" + str(self.level), True, game.white, 1)
        self.battle_text = fontz.font_20.render("Battle " + str(self.battle) + "/" + str(self.battle_max), True, game.white)
        self.game.screen.blit(self.level_text, (545, -4))
        self.game.screen.blit(self.battle_text, (10, 500))

    def increase_dungeon_level(self):
        if self.battle == self.battle_max:
            self.battle = 0
            self.level += 1
        if self.level == 5:
            self.battle_max = 5

dungeonlevel = DungeonLevel()

class Types:
    pass

class NoTypes(Types):
    def __init__(self):
        self.icon = None

class Looters(Types):
    def __init__(self):
        self.name = fontz.font_20.render("Looters", 1, game.white, 1)
        self.health = 10
        self.icon = img.looters_icon
        self.attack = randint(2, 5)
        self.attack_text = fontz.font_20.render("Attack: " + str(self.attack), 1, game.white, 1)
        self.shadow = img.battle_light
        self.selected = False

class Guard(Types):
    def __init__(self):
        self.name = fontz.font_20.render("Guard", 1, game.white, 1)
        self.health = 15
        self.icon = img.guard_icon
        self.attack = randint(3, 7)
        self.attack_text = fontz.font_20.render("Attack: " + str(self.attack), 1, game.white, 1)
        self.shadow = img.battle_light
        self.selected = False

class Hunter(Types):
    def __init__(self):
        self.name = fontz.font_20.render("Hunter", 1, game.white, 1)
        self.health = 20
        self.icon = img.hunter_icon
        self.attack = randint(4, 10)
        self.attack_text = fontz.font_20.render("Attack: " + str(self.attack), 1, game.white, 1)
        self.shadow = img.battle_light
        self.selected = False


EnemyTypes = [Guard, Looters]

class EnemyGroup:
    def __init__(self):
        self.enemyx = [439]  # 219, 669
        self.x = choice(self.enemyx)
        self.y = 98
        self.types = choice(EnemyTypes)()
        self.icon = self.types.icon
        self.health = self.types.health
        self.attack = self.types.attack
        self.attack_text = self.types.attack_text
        self.turn = False
        self.name = self.types.name
        self.exp = randint(5, 15)
        self.text = fontz.font_20.render("You received " + str(self.exp) + " experience", True, game.white)
        self.dead = False
        self.health_draw = fontz.font_20.render("Health: " + str(self.health), True, game.white, 1)
        self.my_death_was_already_processed = False

    def enemy_dead(self):
        if self.health <= 0:
            game.screen.blit(img.battle_won, (200, 50))
            game.screen.blit(self.text, (240, 250))
            self.my_death_was_already_processed = False
            return

    def decrease_health_2(self, value):
        self.health = max(self.health - value, 0)

    def get_icon(self):
        if self.types is not None:
            return self.types.icon
        elif self.types is None:
            return None

    def draw(self):
        self.health_draw = fontz.font_20.render("Health: " + str(self.health), True, game.white, 1)
        if self.types is None:
            self.types = choice(EnemyTypes)()
        if self.types.selected is True:
            game.screen.blit(self.types.shadow, (self.x - 80, self.y - 42))
            game.screen.blit(img.square_icon, (self.x - 9, self.y - 8))
        game.screen.blit(self.types.icon, (self.x, self.y))
        game.screen.blit(self.health_draw, (self.x - 30, self.y + 75))
        game.screen.blit(self.name, (self.x - 10, self.y - 35))
        game.screen.blit(self.attack_text, (self.x - 30, self.y + 100))


class Player:
    def __init__(self):
        self.decrease_health = stats.decrease_health
        self.health = stats.health
        self.armor = stats.armor
        self.exp = stats.exp
        self.sword_attack = stats.sword_attack
        self.bow_attack = stats.bow_attack
        self.bow_selected = False
        self.sword_selected = False
        self.turn = True

    def sword(self):
        pass

    def bow(self):
        pass

    def dead(self):
        if self.health <= 0:
            game.screen.blit(img.battle_lost, (200, 50))
            return

    def draw(self):
        if self.sword_selected is True:
            game.screen.blit(img.weapon_square, (221, 352))
        if self.bow_selected is True:
            game.screen.blit(img.weapon_square, (384, 352))
        game.screen.blit(img.sword, (221, 352))
        game.screen.blit(img.bow, (384, 352))

    def draw_damage(self):
        if showTextTime.getTime() > 2.0:
            pygame.draw.rect(game.screen, game.white, buttons.second_left_button, 1)
            # showTextTime.resetTime()

def battle_screen():
    enemy = EnemyGroup()
    player = Player()
    running = True
    inventory_grid = InventoryGrid(INV_X, INV_Y)
    while running:
        game.screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        if dungeonlevel.level <= 5:
            game.screen.blit(img.battle_screen, (0, 0))
            if buttons.second_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (359, 56))
            game.screen.blit(img.square_icon, (430, 90))
        elif 6 <= dungeonlevel.level <= 11:
            game.screen.blit(img.battle_screen2, (0, 0))
            if buttons.first_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (139, 56))
            if buttons.second_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (359, 56))
            game.screen.blit(img.square_icon, (210, 90))
            game.screen.blit(img.square_icon, (430, 90))
        elif dungeonlevel.level >= 11:
            game.screen.blit(img.battle_screen3, (0, 0))
            if buttons.first_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (139, 56))
            if buttons.second_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (359, 56))
            if buttons.third_enemy.collidepoint(mx, my):
                game.screen.blit(img.battle_light, (579, 56))
            game.screen.blit(img.square_icon, (210, 90))
            game.screen.blit(img.square_icon, (430, 90))
            game.screen.blit(img.square_icon, (660, 90))

        left_column.draw()
        inventory_grid.draw()
        enemy.draw()
        player.sword()
        player.draw()
        enemy.enemy_dead()
        lost_game()
        dungeonlevel.increase_dungeon_level()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    inventory_grid.click(mx, my)    # CLICK
                    if player.turn and player.health != 0:
                        if buttons.second_enemy.collidepoint(mx, my):
                            enemy.types.selected = True
                        elif buttons.bow.collidepoint(mx, my):
                            player.bow_selected = True
                        else:
                            enemy.types.selected = False
                            player.bow_selected = False
                        if buttons.second_enemy.collidepoint(mx, my):
                            enemy.types.selected = True
                        elif buttons.sword.collidepoint(mx, my):
                            player.sword_selected = True
                        else:
                            enemy.types.selected = False
                            player.sword_selected = False
                        if enemy.types.selected and player.bow_selected:
                            enemy.decrease_health_2(player.bow_attack)
                            enemy.types.selected = False
                            player.bow_selected = False
                            player.turn = False
                            enemy.turn = True
                        if enemy.types.selected and player.sword_selected:
                            enemy.decrease_health_2(player.sword_attack)
                            enemy.types.selected = False
                            player.sword_selected = False
                            player.turn = False
                            enemy.turn = True

                    if enemy.turn and enemy.health != 0:
                        stats.decrease_health(enemy.attack)
                        enemy.turn = False
                        player.turn = True

                    if buttons.back_button_left.collidepoint(mx, my):
                        if enemy.health <= 0:
                            if not enemy.my_death_was_already_processed:
                                dungeonlevel.increase_battle_level(1)
                                enemy.my_death_was_already_processed = True
                            stats.boost_xp(enemy.exp)
                            return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if enemy.health <= 0:
                        if not enemy.my_death_was_already_processed:
                            dungeonlevel.increase_battle_level(1)
                            enemy.my_death_was_already_processed = True
                        stats.boost_xp(enemy.exp)
                        return
                    else:                   # Delete this when game is finished.
                        return
        if stats.level <= 3:
            game.screen.blit(img.not_available, (150, 585))
            game.screen.blit(img.not_available, (225, 585))
        if stats.level <= 5:
            game.screen.blit(img.not_available, (300, 585))
            game.screen.blit(img.not_available, (377, 585))
        if stats.level <= 9:
            game.screen.blit(img.not_available, (452, 585))
            game.screen.blit(img.not_available, (530, 585))
        pygame.display.update()
