import pygame
from lcrender import left_column
from icons import img
from buttons import buttons
from grid_view import GridViewCell, GridView
from fontz import fontz as ft
from globals import game
import main_quests_functions
QUEST_X = 200
QUEST_Y = 290
QUEST_WIDTH = 580
QUEST_HEIGHT = 58
QUEST_NUM_X = 1
QUEST_NUM_Y = 6

class QuestNameList:
    def __init__(self):
        self.the_kneeling_one = ft.font_20.render("The Kneeling One.", True, game.white)
        self.dragon_treasure = ft.font_20.render("The Dragon Treasure", True, game.white)

quest_list = QuestNameList()


class QuestSlot(GridViewCell):
    def __init__(self, x, y, width, height):

        # Call __init__ of parent class
        super().__init__(x, y, width, height)

        self.icon_x = x + 15
        self.icon_y = y + 18

        # This will be the number of this slot in inventory
        # It will be set later in InventoryGrid
        self.index = None

    def get_icon(self):                  # Icons
        item = self.get_item()

        if item is None:
            return None

        return {
            "The Kneeling One": quest_list.the_kneeling_one,
            "Dragon Treasure": quest_list.dragon_treasure,

        }[item.name]

    def click(self):                              # Functions
        item = self.get_item()

        if item is None:
            return

        {
            "The Kneeling One": main_quests_functions.the_kneeling_one.loop,
            "Dragon Treasure": main_quests_functions.dragon_treasure.loop,

        }[item.name]()

    def get_item(self):
        """
            Get Inventory Item corresponding to this
            particular Slot
        """
        try:
            return main_quest.items[self.index]
        except IndexError:
            return None

class QuestsGrid(GridView):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.create_cells(
            grid_x=QUEST_X,
            grid_y=QUEST_Y,
            cell_width=QUEST_WIDTH,
            cell_height=QUEST_HEIGHT,
            cols=QUEST_NUM_X,
            rows=QUEST_NUM_Y,
            CellClass=QuestSlot
        )

        self.slots = self.cells

        for index, slot in enumerate(self.slots):
            slot.index = index

class QuestItem:
    def __init__(self, name):
        self.name = name

class MainQuest:
    def __init__(self):
        self.items = [

        ]

    def add_item(self, item_name):
        """
            Add an item by name
        """
        self.items.append(QuestItem(item_name))

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

main_quest = MainQuest()

def my_quests():
    quest_grid = QuestsGrid(QUEST_X, QUEST_Y)
    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.my_quests_ui, (0, 0))
        left_column.draw()
        quest_grid.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                quest_grid.click(mx, my)
                if buttons.back_button_left.collidepoint(mx, my):
                    return