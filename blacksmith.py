import pygame
from stats import stats
from icons import img
from buttons import buttons
from fontz import fontz
from globals import game
from lcrender import left_column


def blacksmith():
    # upgrade prices sword, armor, bow, arrows.
    sup_list = [150, 200, 250, 300, 300, 350, 350, 400, 500, 600, 600]  # Sword upgrade price
    sword_list = [float(1.5), 2, 3, 3, float(4.5), float(5.5), 6, 8, 8, float(8.5), 10]
    s = 0
    aup_list = [150, 200, 250, 300, 300, 350, 350, 400, 500, 600, 600]  # Armor upgrade price
    armor_list = [5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 20]
    a = 0
    bup_list = [250, 250, 250, 300, 350, 350, 350, 450, 450, 600, 600]  # Bow upgrade price
    bow_list = [float(1.5), 2, 3, 3, float(4.5), float(5.5), 6, 8, 8, float(8.5), 10]
    b = 0
    wup_list = [150, 200, 200, 250, 250, 250, 300, 350, 350, 400, 400]  # Arrow upgrade price
    arrow_list = [1, 1, 2, 2, 4, 5, 5, 5, 5, 5, 5]
    w = 0
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.blacksmith_ui, (0, 0))
        sword_level_text = fontz.font_20.render("" + str(stats.sword_level), True, game.white, 1)
        armor_level_text = fontz.font_20.render("" + str(stats.armor_level), True, game.white, 1)
        bow_level_text = fontz.font_20.render("" + str(stats.bow_level), True, game.white, 1)
        arrow_level_text = fontz.font_20.render("" + str(stats.arrow_level), True, game.white, 1)
        suv = fontz.font_20.render("+ " + str(sword_list[s]), True, game.white, 1)  # Sword upgrade value
        auv = fontz.font_20.render("+ " + str(armor_list[a]), True, game.white, 1)  # Armor upgrade value
        buv = fontz.font_20.render("+ " + str(bow_list[b]), True, game.white, 1)  # Bow upgrade value
        awv = fontz.font_20.render("+ " + str(arrow_list[w]), True, game.white, 1)  # Arrow upgrade value
        su_price = fontz.font_20.render("Price: " + str(sup_list[s]), True, game.white, 1)  # Sword upgrade price
        au_price = fontz.font_20.render("Price: " + str(aup_list[a]), True, game.white, 1)  # Armor upgrade price
        bu_price = fontz.font_20.render("Price: " + str(bup_list[b]), True, game.white, 1)  # Bow upgrade price
        aw_price = fontz.font_20.render("Price: " + str(wup_list[w]), True, game.white, 1)  # Arrow upgrade price
        game.screen.blit(sword_level_text, (230, 450))
        game.screen.blit(armor_level_text, (385, 450))
        game.screen.blit(bow_level_text, (547, 450))
        game.screen.blit(arrow_level_text, (705, 450))
        if stats.sword_level <= 9:
            game.screen.blit(suv, (190, 565))
        if stats.armor_level <= 9:
            game.screen.blit(auv, (350, 565))
        if stats.bow_level <= 9:
            game.screen.blit(buv, (510, 565))
        if stats.arrow_level <= 9:
            game.screen.blit(awv, (670, 565))
        if stats.sword_level < 10:
            game.screen.blit(su_price, (160, 540))
        elif stats.sword_level == 10:
            game.screen.blit((fontz.old_font_20.render("Level 10/10", True, game.white)), (153, 540))
        if stats.armor_level < 10:
            game.screen.blit(au_price, (320, 540))
        elif stats.armor_level == 10:
            game.screen.blit((fontz.old_font_20.render("Level 10/10", True, game.white)), (310, 540))
        if stats.bow_level < 10:
            game.screen.blit(bu_price, (480, 540))
        elif stats.bow_level == 10:
            game.screen.blit((fontz.old_font_20.render("Level 10/10", True, game.white)), (466, 540))
        if stats.arrow_level < 10:
            game.screen.blit(aw_price, (640, 540))
        elif stats.arrow_level == 10:
            game.screen.blit((fontz.old_font_20.render("Level 10/10", True, game.white)), (623, 540))
        mx, my = pygame.mouse.get_pos()
        if buttons.sword_info.collidepoint(mx, my):
            game.screen.blit(img.blacksmith_icon_01, (mx, my - 200))
        elif buttons.armor_info.collidepoint(mx, my):
            game.screen.blit(img.blacksmith_icon_02, (mx, my - 200))
        elif buttons.bow_info.collidepoint(mx, my):
            game.screen.blit(img.blacksmith_icon_03, (mx, my - 200))
        elif buttons.arrow_info.collidepoint(mx, my):
            game.screen.blit(img.blacksmith_icon_04, (mx - 239, my - 200))

        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.back_button_left.collidepoint(mx, my):
                        return
                    if buttons.upgrade_sword_button.collidepoint(mx, my):
                        if stats.gold > sup_list[s] and stats.sword_level != 10:
                            stats.sword_level += 1
                            stats.decrease_gold(sup_list[s])
                            stats.sword_attack += sword_list[s]
                            s += 1
                    if buttons.upgrade_armor_button.collidepoint(mx, my):
                        if stats.gold > aup_list[a] and stats.armor_level != 10:
                            stats.armor_level += 1
                            stats.boost_max_armor(a)
                            stats.decrease_gold(sup_list[a])
                            a += 1
                            stats.max_armor += armor_list[a]
                    if buttons.upgrade_bow_button.collidepoint(mx, my):
                        if stats.gold > bup_list[b] and stats.bow_level != 10:
                            stats.bow_level += 1
                            stats.boost_bow_attack(b)
                            stats.decrease_gold(bup_list[b])
                            b += 1
                            stats.bow_attack += bow_list[b]
                    if buttons.upgrade_arrows_button.collidepoint(mx, my):
                        if stats.gold > wup_list[w] and stats.arrow_level != 10:
                            stats.arrow_level += 1
                            stats.arrow_attack += w
                            stats.decrease_gold(bup_list[w])
                            w += 1
                            stats.arrow_attack += arrow_list[s]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()
