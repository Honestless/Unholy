import pygame
from globals import game
from icons import img
from buttons import buttons
from grid_view import GridView, GridViewCell
from stats import stats
from inventory import inventory
from lcrender import left_column
from fontz import fontz as ft

INV_X = 139
INV_Y = 347
INV_NUM_X = 8
INV_NUM_Y = 4
INV_WIDTH = 73
INV_HEIGHT = 73

def use_bread():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(4)
    else:
        return
def use_cheese():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(6)
    else:
        return
def use_apple():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(2)
    else:
        return
def use_candy():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(8)
    else:
        return
def use_big_potion():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(50)
    else:
        return
def use_small_potion():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(25)
    else:
        return
def use_phial():
    if stats.armor <= stats.max_armor - 1:
        stats.boost_armor(50)
    else:
        return
def use_draught():
    print("You used draught of luck.")
def use_small_pk():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(10)
    else:
        return
def use_big_pk():
    if stats.health <= stats.max_health - 1:
        stats.boost_health(20)
    else:
        return
def use_lucky_leaf():
    print("You used a lucky leaf.")
def use_syringe():
    if stats.health <= stats.max_health - 1 and stats.armor <= stats.max_armor - 1:
        stats.boost_health(50)
        stats.boost_armor(50)
    else:
        return

def use_dragon_necklace():
    pass

class MainInvSlot(GridViewCell):
    def __init__(self, x, y, width, height):

        # Call __init__ of parent class
        super().__init__(x, y, width, height)

        self.icon_x = x + 12
        self.icon_y = y + 12

        # This will be the number of this slot in inventory
        # It will be set later in InventoryGrid
        self.index = None

    def get_icon(self):                  # Icons
        item = self.get_item()

        if item is None:
            return None

        return {
            "bread": img.bread_icon,
            "cheese": img.cheese_icon,
            "apple": img.apple_icon,
            "candy": img.candy_icon,
            "bigpotion": img.big_potion_icon,
            "smallpotion": img.small_potion_icon,
            "draught": img.draught_of_luck_icon,
            "phial": img.phial_of_protection_icon,
            "smallpk": img.small_painkiller_icon,
            "bigpk": img.big_painkiller_icon,
            "luckyleaf": img.lucky_leaf_icon,
            "syringe": img.syringe_icon,
            "Dragon Necklace": img.dragon_necklace,

        }[item.name]

    def click(self):                              # Functions
        item = self.get_item()

        if item is None:
            return

        {
            "bread": use_bread,
            "cheese": use_cheese,
            "apple": use_apple,
            "candy": use_candy,
            "bigpotion": use_big_potion,
            "smallpotion": use_small_potion,
            "draught": use_draught,
            "phial": use_phial,
            "smallpk": use_small_pk,
            "bigpk": use_big_pk,
            "luckyleaf": use_lucky_leaf,
            "syringe": use_syringe,
            "Dragon Necklace": use_dragon_necklace,

        }[item.name]()

        if item is not None:
            maininventory.remove_particular_item(item)

    def right_click(self):                          # Send item to battle inventory.
        if inventory.inventory_full is not True:
            item = self.get_item()

            if item is None:
                return
            if item is not None:
                maininventory.move_item(item)

    def get_item(self):
        """
            Get Inventory Item corresponding to this
            particular Slot
        """
        try:
            return maininventory.items[self.index]
        except IndexError:
            return None

class MainInventoryGrid(GridView):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.create_cells(
            grid_x=INV_X,
            grid_y=INV_Y,
            cell_width=INV_WIDTH,
            cell_height=INV_HEIGHT,
            cols=INV_NUM_X,
            rows=INV_NUM_Y,
            CellClass=MainInvSlot
        )

        self.slots = self.cells

        for index, slot in enumerate(self.slots):
            slot.index = index

class InventoryItem:
    def __init__(self, name):
        self.name = name

class MainInventory:
    def __init__(self):
        self.full = False
        self.max_item_number = 32
        self.items = [

        ]

    def max_items(self):
        if len(self.items) >= 32:
            self.full = True

    def add_item(self, item_name):
        """
            Add an item by name
        """
        self.items.append(InventoryItem(item_name))

    def remove_item(self, item_name):
        """
            Remove item by name
        """
        found_items = filter(lambda item: item.name == item_name, self.items)
        item_to_remove = next(found_items)
        self.items.remove(item_to_remove)

    def remove_particular_item(self, item):
        """
            Remove particular InventoryItem
        """
        self.items.remove(item)

    def move_item(self, item):
        """
            Move particular item
        """
        self.remove_particular_item(item)
        inventory.items.append(item)

maininventory = MainInventory()

def character_menu():
    inventory_grid = MainInventoryGrid(INV_X, INV_Y)
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.character_ui, (0, 0,))
        game.screen.blit(ft.font_20.render(str(stats.health) + "/" + str(stats.max_health), True, game.white), (230, 125))
        game.screen.blit(ft.font_20.render(str(stats.armor) + "/" + str(stats.max_armor), True, game.white), (230, 195))
        game.screen.blit(ft.font_20.render(str(stats.attack), True, game.white), (470, 95))
        game.screen.blit(ft.font_20.render(str(stats.defence), True, game.white), (470, 165))
        game.screen.blit(ft.font_20.render(str(stats.strength), True, game.white), (470, 235))
        game.screen.blit(ft.font_20.render(str(stats.agility), True, game.white), (700, 95))
        game.screen.blit(ft.font_20.render(str(stats.perception), True, game.white), (700, 165))
        game.screen.blit(ft.font_20.render(str(stats.deception), True, game.white), (700, 235))
        inventory_grid.draw()
        left_column.draw()
        mx, my = pygame.mouse.get_pos()
        if buttons.char_button_01.collidepoint(mx, my):
            game.screen.blit(img.char_icon_01, (mx, my))
        if buttons.char_button_02.collidepoint(mx, my):
            game.screen.blit(img.char_icon_02, (mx, my))
        if buttons.char_button_03.collidepoint(mx, my):
            game.screen.blit(img.char_icon_03, (mx, my))
        if buttons.char_button_04.collidepoint(mx, my):
            game.screen.blit(img.char_icon_04, (mx, my))
        if buttons.char_button_05.collidepoint(mx, my):
            game.screen.blit(img.char_icon_05, (mx, my))
        if buttons.char_button_06.collidepoint(mx, my):
            game.screen.blit(img.char_icon_06, (mx - 240, my))
        if buttons.char_button_07.collidepoint(mx, my):
            game.screen.blit(img.char_icon_07, (mx - 240, my))
        if buttons.char_button_08.collidepoint(mx, my):
            game.screen.blit(img.char_icon_08, (mx - 240, my))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    inventory_grid.click(mx, my)  # CLICK
                    if buttons.back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.MOUSEBUTTONUP and inventory.inventory_full is not True:
                if event.button == 3:
                    inventory_grid.right_click(mx, my)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        inventory.max_items()

        pygame.display.update()