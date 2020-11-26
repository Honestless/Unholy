import pygame
import os
pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unholy: A chosen Hero")
clock = pygame.time.Clock()

# Fonts
font_40 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 40)
font_20 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 20)
font_15 = pygame.font.Font(os.path.join('fonts', 'TravelingTypewriter.ttf'), 15)
old_font_40 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 40)
old_font_30 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 30)
old_font_20 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 20)
old_font_15 = pygame.font.Font(os.path.join('fonts', 'old_typewriter.ttf'), 15)

# Colors
white = (255, 255, 255)
# UI, HUD and Backgrounds
riverwood_ui = pygame.image.load(os.path.join('images', 'main_game_bg.png'))
health_bar = pygame.image.load(os.path.join('images', 'health_bar.png'))
exp_bar = pygame.image.load(os.path.join('images', 'xp_bar.png'))
blacksmith_ui = pygame.image.load(os.path.join('images', 'blacksmith_ui.png'))
training_ui = pygame.image.load(os.path.join('images', 'training_ui.png'))
market_ui = pygame.image.load(os.path.join('images', 'market_ui.png'))
tavern_ui = pygame.image.load(os.path.join('images', 'tavern_ui.png'))
dl1_ui = pygame.image.load(os.path.join('images', 'dl1.png'))
main_menu_ui = pygame.image.load(os.path.join('images', 'main_menu_ui.png'))
options_ui = pygame.image.load(os.path.join('images', 'options_ui.png'))
credits_ui = pygame.image.load(os.path.join('images', 'credits_ui.png'))
game_intro_ui = pygame.image.load(os.path.join('images', 'game_intro_ui.png'))
# RES + LOAD ICONS
battle_icon = pygame.transform.scale(pygame.image.load(os.path.join('images', 'battle_icon.png')), (50, 50))
player_icon = pygame.transform.scale(pygame.image.load(os.path.join('images', 'player_icon.png')), (50, 50))
blank_bar = pygame.transform.scale(pygame.image.load(os.path.join('images', 'blank_bar.png')), (135, 33))
attack_icon = pygame.transform.scale(pygame.image.load(os.path.join('images', 'attack_icon.png')), (28, 28))
defence_icon = pygame.transform.scale(pygame.image.load(os.path.join('images', 'defence_icon.png')), (28, 28))
strength_icon = pygame.transform.scale(pygame.image.load(os.path.join('images', 'strength_icon.png')), (28, 28))

# Buttons Main Menu
new_game_menu_button = pygame.Rect(295, 265, 200, 50)
options_menu_button = pygame.Rect(295, 365, 200, 50)
credits_menu_button = pygame.Rect(295, 465, 200, 50)
quit_menu_button = pygame.Rect(295, 565, 200, 50)

# Buttons Riverwood
first_left_button = pygame.Rect(140, 350, 200, 50)
second_left_button = pygame.Rect(140, 420, 200, 50)
third_left_button = pygame.Rect(140, 490, 200, 50)
fourth_left_button = pygame.Rect(140, 565, 200, 50)
first_right_button = pygame.Rect(390, 350, 200, 50)
second_right_button = pygame.Rect(390, 420, 200, 50)
third_right_button = pygame.Rect(390, 490, 200, 50)
fourth_right_button = pygame.Rect(390, 565, 200, 50)
dungeon_button = pygame.Rect(600, 490, 130, 65)

# Buttons Blacksmith
upgrade_sword_button = pygame.Rect(150, 510, 125, 80)
upgrade_armor_button = pygame.Rect(307, 510, 125, 80)
upgrade_bow_button = pygame.Rect(465, 510, 125, 80)
upgrade_arrows_button = pygame.Rect(622, 510, 125, 80)
back_button_left = pygame.Rect(0, 595, 130, 55)
# Dungeons
dungeon_level = 1
# Player spec
health, max_health = 50, 50
armor, max_armor = 10, 50
exp, max_exp = 10, 250
sword_level, sword_max_level = 0, 10
agility_level, agility_max_level = 0, 10
strength_level, strength_max_level = 0, 10
armor_level, armor_max_level = 0, 10
bow_level, bow_max_level = 0, 10
arrow_level, arrow_max_level = 0, 10
attack_level, attack_max_level = 0, 10
attack, max_attack = 2, 30
defence_level, defence_max_level = 0, 30
level = 1
gold = 50000
day = 1


# LISTS
dg01_coord = [(167, 350), (177, 350), (287, 350), (397, 350), (507, 350), (617, 350),   # Row 1
              (167, 430), (177, 430), (287, 430), (397, 430), (507, 430), (617, 430),   # Row 2
              (167, 510), (177, 510), (287, 510), (397, 510), (507, 510), (617, 510),   # Row 3
              (167, 590), (177, 590), (287, 590), (397, 590), (507, 590), (617, 590),   # Row 4
              ]
dg_list = []
# upgrade prices sword, armor, bow, arrows.
sup_list = [150, 200, 250, 300, 300, 350, 350, 400, 500, 600, 600]   # Sword upgrade price
s = 0
aup_list = [150, 200, 250, 300, 300, 350, 350, 400, 500, 600, 600]   # Armor upgrade price
a = 0
bup_list = [250, 250, 250, 300, 350, 350, 350, 450, 450, 600, 600]   # Bow upgrade price
b = 0
wup_list = [150, 200, 200, 250, 250, 250, 300, 350, 350, 400, 400]   # Arrow upgrade price
w = 0


def boost_armor(value):
    global armor, max_armor
    armor = min(armor + value, max_armor)

def boost_health(value):
    global health, max_health
    health = min(health + value, max_health)

def boost_xp(value):
    global exp, max_exp
    exp = min(exp + value, max_exp)

def left_column_render():
    global level, health, max_health, exp, gold, max_exp

    # Bars px
    health_px = (health/max_health)*135
    xp_px = (exp/max_exp)*134
    armor_px = (armor/max_armor)*134

    level_text = font_20.render("Level:  " + str(level), True, white, 1)
    gold_text = font_20.render("Gold:  " + str(gold), True, white, 1)
    day_text = font_20.render("Day:  " + str(day), True, white, 1)
    health_text = font_20.render("HP:  " + str(health), True, white, 1)
    armor_text = font_20.render("Armor:  " + str(armor), True, white, 1)
    exp_text = font_20.render("Exp:  " + str(exp), True, white, 1)
    attack_text = font_15.render("Att:  " + str(attack), True, white, 1)
    defence_text = font_15.render("Def:  " + str(defence_level), True, white, 1)
    strength_text = font_15.render("Str:  " + str(strength_level), True, white, 1)
    res_health_bar = pygame.transform.scale(health_bar, (int(health_px), 34))
    armor_bar = pygame.transform.scale(pygame.image.load(os.path.join('images', 'armor_bar.png')), (int(armor_px), 24))
    res_exp_bar = pygame.transform.scale(exp_bar, (int(xp_px), 26))
    screen.blit(blank_bar, (1, 50))
    screen.blit(res_health_bar, (1, 50))
    screen.blit(blank_bar, (1, 83))
    screen.blit(armor_bar, (1, 89))
    screen.blit(blank_bar, (1, 115))
    screen.blit(res_exp_bar, (1, 118))
    screen.blit(health_text, (20, 54))
    screen.blit(armor_text, (20, 88))
    screen.blit(exp_text, (20, 118))
    screen.blit(level_text, (15, 165))
    screen.blit(gold_text, (15, 205))
    screen.blit(day_text, (15, 245))
    screen.blit(attack_icon, (3, 286))
    screen.blit(defence_icon, (3, 328))
    screen.blit(strength_icon, (3, 369))
    screen.blit(attack_text, (35, 289))
    screen.blit(defence_text, (35, 331))
    screen.blit(strength_text, (35, 372))
    if exp > 249:
        level += 1
        max_exp += 250
        gold += 50


def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_menu_ui, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if new_game_menu_button.collidepoint(mx, my):
                        game_intro()
                    if options_menu_button.collidepoint(mx, my):
                        options_menu()
                    if credits_menu_button.collidepoint(mx, my):
                        credits_menu()
                    if quit_menu_button.collidepoint(mx, my):
                        quit()


def credits_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(credits_ui, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if options_menu_button.collidepoint(mx, my):
                        return


def options_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(options_ui, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if new_game_menu_button.collidepoint(mx, my):
                        print("Audio")
                    if options_menu_button.collidepoint(mx, my):
                        print("Video")
                    if credits_menu_button.collidepoint(mx, my):
                        return


def game_intro():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(game_intro_ui, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if credits_menu_button.collidepoint(mx, my):
                        game_main_screen()


def game_main_screen():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(riverwood_ui, (0, 0))
        left_column_render()
        pygame.draw.rect(screen, (0, 0, 0), dungeon_button, 6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if first_left_button.collidepoint(mx, my):
                        blacksmith()
                    if second_left_button.collidepoint(mx, my):
                        market()
                    if third_left_button.collidepoint(mx, my):
                        print("")
                    if fourth_left_button.collidepoint(mx, my):
                        print("Fourth left button")
                    if first_right_button.collidepoint(mx, my):
                        training_field()
                    if second_right_button.collidepoint(mx, my):
                        boost_armor(5)
                        boost_health(5)
                        boost_xp(73)
                    if third_right_button.collidepoint(mx, my):
                        tavern()
                    if fourth_left_button.collidepoint(mx, my):
                        print("Fourth right button")
                    if dungeon_button.collidepoint(mx, my):
                        dungeon_level_01()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


def blacksmith():
    global gold, sword_level, s, a, b, w, armor_level, bow_level, arrow_level
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(blacksmith_ui, (0, 0))
        sword_level_text = font_20.render("" + str(sword_level), True, white, 1)
        armor_level_text = font_20.render("" + str(armor_level), True, white, 1)
        bow_level_text = font_20.render("" + str(bow_level), True, white, 1)
        arrow_level_text = font_20.render("" + str(arrow_level), True, white, 1)
        su_price = font_20.render("Price: " + str(sup_list[s]), True, white, 1)   # Sword upgrade price
        au_price = font_20.render("Price: " + str(aup_list[a]), True, white, 1)   # Armor upgrade price
        bu_price = font_20.render("Price: " + str(bup_list[b]), True, white, 1)   # Bow upgrade price
        aw_price = font_20.render("Price: " + str(wup_list[w]), True, white, 1)   # Arrow upgrade price
        screen.blit(sword_level_text, (230, 450))
        screen.blit(armor_level_text, (385, 450))
        screen.blit(bow_level_text, (547, 450))
        screen.blit(arrow_level_text, (705, 450))
        if sword_level < 10:
            screen.blit(su_price, (160, 540))
        elif sword_level == 10:
            screen.blit((old_font_20.render("Level 10/10", True, white)), (153, 540))
        if armor_level < 10:
            screen.blit(au_price, (320, 540))
        elif armor_level == 10:
            screen.blit((old_font_20.render("Level 10/10", True, white)), (313, 540))
        if bow_level < 10:
            screen.blit(bu_price, (480, 540))
        elif bow_level == 10:
            screen.blit((old_font_20.render("Level 10/10", True, white)), (473, 540))
        if arrow_level < 10:
            screen.blit(aw_price, (640, 540))
        elif arrow_level == 10:
            screen.blit((old_font_20.render("Level 10/10", True, white)), (633, 540))

        left_column_render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if back_button_left.collidepoint(mx, my):
                        return
                    if upgrade_sword_button.collidepoint(mx, my):
                        if gold > sup_list[s] and sword_level != 10:
                            sword_level += 1
                            gold -= sup_list[s]
                            s += 1
                    if upgrade_armor_button.collidepoint(mx, my):
                        if gold > aup_list[a] and armor_level != 10:
                            armor_level += 1
                            gold -= sup_list[a]
                            a += 1
                    if upgrade_bow_button.collidepoint(mx, my):
                        if gold > bup_list[b] and bow_level != 10:
                            bow_level += 1
                            gold -= bup_list[b]
                            b += 1
                    if upgrade_arrows_button.collidepoint(mx, my):
                        if gold > wup_list[w] and arrow_level != 10:
                            arrow_level += 1
                            gold -= bup_list[w]
                            w += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


def training_field():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(training_ui, (0, 0,))
        left_column_render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


def market():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(market_ui, (0, 0,))
        left_column_render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


def tavern():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(tavern_ui, (0, 0))
        left_column_render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


def dungeon_level_01():
    global dungeon_level
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(dl1_ui, (0, 0))
        dg_level_text = old_font_30.render("" + str(dungeon_level), True, white, 1)
        screen.blit(dg_level_text, (550, 8))
        screen.blit(player_icon, (167, 350))
        screen.blit(battle_icon, (277, 510))
        left_column_render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()


main_menu()
