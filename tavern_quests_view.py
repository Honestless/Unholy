from grid_view import GridViewCell, GridView
from fontz import fontz as ft
from globals import game
import tavern_quests_functions
QUEST_X = 160
QUEST_Y = 400
QUEST_WIDTH = 600
QUEST_HEIGHT = 58
QUEST_NUM_X = 1
QUEST_NUM_Y = 4

class QuestNameList:
    def __init__(self):
        self.quest_name_01 = ft.font_20.render("The Desperate Woman", True, game.white)
        self.quest_name_02 = ft.font_20.render("Criminal Activity near Riverwood", True, game.white)

questlist = QuestNameList()


class RandomQuestSlot(GridViewCell):
    def __init__(self, x, y, width, height):

        # Call __init__ of parent class
        super().__init__(x, y, width, height)

        self.icon_x = x + 6
        self.icon_y = y + 18

        # This will be the number of this slot in inventory
        # It will be set later in InventoryGrid
        self.index = None

    def get_icon(self):                  # Icons
        item = self.get_item()

        if item is None:
            return None

        return {
            "The Desperate Woman": questlist.quest_name_01,
            "Criminal Activity": questlist.quest_name_02,

        }[item.name]

    def click(self):                              # Functions
        item = self.get_item()

        if item is None:
            return

        {
            "The Desperate Woman": tavern_quests_functions.sinje.loop,
            "Criminal Activity": tavern_quests_functions.criminal_activity.loop,

        }[item.name]()

    def get_item(self):
        """
            Get Inventory Item corresponding to this
            particular Slot
        """
        try:
            return tavern_quest.items[self.index]
        except IndexError:
            return None

class RandomQuestsGrid(GridView):
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
            CellClass=RandomQuestSlot
        )

        self.slots = self.cells

        for index, slot in enumerate(self.slots):
            slot.index = index

class QuestItem:
    def __init__(self, name):
        self.name = name

class TavernQuests:
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

tavern_quest = TavernQuests()

tavern_quest.add_item("The Desperate Woman")
tavern_quest.add_item("Criminal Activity")