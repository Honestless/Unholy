import pygame
from globals import game
from fontz import fontz
from icons import img
from stats import stats
from buttons import buttons
from lcrender import left_column
from character_menu import maininventory
def market():
    running = True
    bread_price, cheese_price, apples_price, candy_price = 15, 20, 10, 25
    bhp_price, shp_price, dol_price, pop_price = 100, 60, 100, 100
    small_pk_price, big_pk_price, LL_PRICE, syringe_price = 25, 60, 150, 150
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.market_ui, (0, 0,))
        bread_buy = fontz.old_font_15.render(str(bread_price) + " gold", True, game.white, 1)
        cheese_buy = fontz.old_font_15.render(str(cheese_price) + " gold", True, game.white, 1)
        apples_buy = fontz.old_font_15.render(str(apples_price) + " gold", True, game.white, 1)
        candy_buy = fontz.old_font_15.render(str(candy_price) + " gold", True, game.white, 1)
        big_potion_buy = fontz.old_font_15.render(str(bhp_price) + " gold", True, game.white, 1)
        small_potion_buy = fontz.old_font_15.render(str(shp_price) + " gold", True, game.white, 1)
        draught_buy = fontz.old_font_15.render(str(dol_price) + " gold", True, game.white, 1)
        phial_buy = fontz.old_font_15.render(str(pop_price) + " gold", True, game.white, 1)
        s_pk_buy = fontz.old_font_15.render(str(small_pk_price) + " gold", True, game.white, 1)
        big_pk_buy = fontz.old_font_15.render(str(big_pk_price) + " gold", True, game.white, 1)
        luck_leaf_buy = fontz.old_font_15.render(str(LL_PRICE) + " gold", True, game.white, 1)
        syringe_buy = fontz.old_font_15.render(str(syringe_price) + " gold", True, game.white, 1)
        game.screen.blit(bread_buy, (265, 415))
        game.screen.blit(cheese_buy, (265, 485))
        game.screen.blit(apples_buy, (265, 553))
        game.screen.blit(candy_buy, (265, 622))
        game.screen.blit(big_potion_buy, (493, 415))
        game.screen.blit(small_potion_buy, (493, 485))
        game.screen.blit(draught_buy, (493, 553))
        game.screen.blit(phial_buy, (493, 622))
        game.screen.blit(s_pk_buy, (720, 415))
        game.screen.blit(big_pk_buy, (720, 485))
        game.screen.blit(luck_leaf_buy, (720, 553))
        game.screen.blit(syringe_buy, (720, 622))
        mx, my = pygame.mouse.get_pos()
        if buttons.market_button_01.collidepoint(mx, my):
            game.screen.blit(img.bread_icon_float, (mx, my - 200))
        if buttons.market_button_02.collidepoint(mx, my):
            game.screen.blit(img.cheese_icon_float, (mx, my - 200))
        if buttons.market_button_03.collidepoint(mx, my):
            game.screen.blit(img.apples_icon_float, (mx, my - 200))
        if buttons.market_button_04.collidepoint(mx, my):
            game.screen.blit(img.candy_icon_float, (mx, my - 200))
        if buttons.market_button_05.collidepoint(mx, my):
            game.screen.blit(img.big_hp_icon_float, (mx, my - 200))
        if buttons.market_button_06.collidepoint(mx, my):
            game.screen.blit(img.small_hp_icon_float, (mx, my - 200))
        if buttons.market_button_07.collidepoint(mx, my):
            game.screen.blit(img.draught_icon_float, (mx, my - 200))
        if buttons.market_button_08.collidepoint(mx, my):
            game.screen.blit(img.phial_icon_float, (mx, my - 200))
        if buttons.market_button_09.collidepoint(mx, my):
            game.screen.blit(img.smallpk_icon_float, (mx - 230, my - 200))
        if buttons.market_button_10.collidepoint(mx, my):
            game.screen.blit(img.bigpk_icon_float, (mx - 230, my - 200))
        if buttons.market_button_11.collidepoint(mx, my):
            game.screen.blit(img.leaf_icon_float, (mx - 230, my - 200))
        if buttons.market_button_12.collidepoint(mx, my):
            game.screen.blit(img.syringe_icon_float, (mx - 230, my - 200))
        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if buttons.back_button_left.collidepoint(mx, my):
                        return
                    if buttons.market_button_01.collidepoint(mx, my) and maininventory.full is False:
                        if bread_price <= stats.gold:
                            maininventory.add_item("bread")
                            stats.decrease_gold(bread_price)
                    if buttons.market_button_02.collidepoint(mx, my) and maininventory.full is False:
                        if cheese_price <= stats.gold:
                            maininventory.add_item("cheese")
                            stats.decrease_gold(cheese_price)
                    if buttons.market_button_03.collidepoint(mx, my) and maininventory.full is False:
                        if apples_price <= stats.gold:
                            maininventory.add_item("apple")
                            stats.decrease_gold(apples_price)
                    if buttons.market_button_04.collidepoint(mx, my) and maininventory.full is False:
                        if candy_price <= stats.gold:
                            maininventory.add_item("candy")
                            stats.decrease_gold(candy_price)
                    if buttons.market_button_05.collidepoint(mx, my) and maininventory.full is False:
                        if bhp_price <= stats.gold:
                            maininventory.add_item("bigpotion")
                            stats.decrease_gold(bhp_price)
                    if buttons.market_button_06.collidepoint(mx, my) and maininventory.full is False:
                        if shp_price <= stats.gold:
                            maininventory.add_item("smallpotion")
                            stats.decrease_gold(shp_price)
                    if buttons.market_button_07.collidepoint(mx, my) and maininventory.full is False:
                        if dol_price <= stats.gold:
                            maininventory.add_item("draught")
                            stats.decrease_gold(dol_price)
                    if buttons.market_button_08.collidepoint(mx, my) and maininventory.full is False:
                        if pop_price <= stats.gold:
                            maininventory.add_item("phial")
                            stats.decrease_gold(pop_price)
                    if buttons.market_button_09.collidepoint(mx, my) and maininventory.full is False:
                        if small_pk_price <= stats.gold:
                            maininventory.add_item("smallpk")
                            stats.decrease_gold(small_pk_price)
                    if buttons.market_button_10.collidepoint(mx, my) and maininventory.full is False:
                        if big_pk_price < stats.gold:
                            maininventory.add_item("bigpk")
                            stats.decrease_gold(big_pk_price)
                    if buttons.market_button_11.collidepoint(mx, my) and maininventory.full is False:
                        if LL_PRICE <= stats.gold:
                            maininventory.add_item("luckyleaf")
                            stats.decrease_gold(LL_PRICE)
                    if buttons.market_button_12.collidepoint(mx, my) and maininventory.full is False:
                        if syringe_price <= stats.gold:
                            maininventory.add_item("syringe")
                            stats.decrease_gold(syringe_price)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        maininventory.max_items()
        pygame.display.update()
