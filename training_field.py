import pygame
from globals import game
from lcrender import left_column
from icons import img
from buttons import buttons
from fontz import fontz as ft
from stats import stats


def training_field():
    ag_price = [50, 75, 100, 125, 150, 0]
    ag_upgrade = [1, 2, 2, 2, 2, 0]
    a = 0
    pr_price = [75, 100, 150, 175, 200, 0]
    pr_upgrade = [2, 2, 2, 3, 5, 0]
    b = 0
    dc_price = [100, 100, 100, 150, 200, 0]
    dc_upgrade = [2, 2, 2, 3, 5, 0]
    c = 0
    att_price = [150, 150, 150, 150, 200, 0]
    att_upgrade = [1, 1, 1, 2, 3, 0]
    d = 0
    def_price = [150, 150, 150, 150, 200, 0]
    def_upgrade = [1, 1, 2, 2, 3, 0]
    e = 0
    str_price = [150, 150, 150, 150, 200, 0]
    str_upgrade = [1, 1, 2, 2, 3, 0]
    f = 0
    running = True
    while running:
        # suv = fontz.font_20.render("+ " + str(sword_list[s]), True, game.white, 1)
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.training_ui, (0, 0,))
        # Price
        if stats.agility_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(ag_price[a]) + " gold", True, game.white, 1), (230, 385))
            game.screen.blit(ft.font_20.render("+ " + str(ag_upgrade[a]) + " agility", True, game.white, 1), (260, 415))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (260, 385))

        if stats.perception_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(pr_price[b]) + " gold", True, game.white, 1), (225, 480))
            game.screen.blit(ft.font_20.render("+ " + str(pr_upgrade[b]) + " perception", True, game.white, 1), (261, 510))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (260, 480))

        if stats.deception_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(dc_price[c]) + " gold", True, game.white, 1), (225, 575))
            game.screen.blit(ft.font_20.render("+ " + str(dc_upgrade[c]) + " deception", True, game.white, 1), (261, 605))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (260, 575))

        if stats.attack_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(att_price[d]) + " gold", True, game.white, 1), (505, 385))
            game.screen.blit(ft.font_20.render("+ " + str(att_upgrade[d]) + " attack", True, game.white, 1), (540, 415))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (535, 385))

        if stats.defence_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(def_price[e]) + " gold", True, game.white, 1), (505, 480))
            game.screen.blit(ft.font_20.render("+ " + str(def_upgrade[e]) + " defence", True, game.white, 1), (540, 510))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (535, 480))

        if stats.strength_level != 5:
            game.screen.blit(ft.font_20.render("Upgrade: " + str(str_price[f]) + " gold", True, game.white, 1), (505, 575))
            game.screen.blit(ft.font_20.render("+ " + str(str_upgrade[f]) + " strength", True, game.white, 1), (540, 610))
        else:
            game.screen.blit(ft.font_20.render("Level 5/5", True, game.white, 1), (535, 575))

        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.first_button.collidepoint(mx, my):
                        if stats.gold > ag_price[a] and stats.agility_level != 5:
                            stats.agility_level += 1
                            stats.boost_agility(ag_upgrade[a])
                            stats.decrease_gold(ag_price[a])
                            a += 1
                    if buttons.second_button.collidepoint(mx, my):
                        if stats.gold > pr_price[b] and stats.perception_level != 5:
                            stats.perception_level += 1
                            stats.boost_perception(pr_upgrade[b])
                            stats.decrease_gold(pr_upgrade[b])
                            b += 1
                    if buttons.third_button.collidepoint(mx, my):
                        if stats.gold > dc_price[c] and stats.deception_level != 5:
                            stats.deception_level += 1
                            stats.boost_deception(dc_upgrade[c])
                            stats.decrease_gold(dc_upgrade[c])
                            c += 1
                    if buttons.fourth_button.collidepoint(mx, my):
                        if stats.gold > att_price[d] and stats.attack_level != 5:
                            stats.attack_level += 1
                            stats.boost_attack(att_upgrade[d])
                            stats.decrease_gold(att_price[d])
                            d += 1
                    if buttons.fifth_button.collidepoint(mx, my):
                        if stats.gold > def_price[e] and stats.defence_level != 5:
                            stats.defence_level += 1
                            stats.boost_defence(def_upgrade[e])
                            stats.decrease_gold(def_price[e])
                            e += 1
                    if buttons.sixth_button.collidepoint(mx, my):
                        if stats.gold > str_price[f] and stats.strength_level != 5:
                            stats.strength_level += 1
                            stats.boost_strength(str_upgrade[f])
                            stats.decrease_gold(str_price[f])
                            f += 1
                    if buttons.back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.update()
