from icons import img
from grid_view import GridView, GridViewCell
from stats import stats
INV_X = 150 - 12
INV_Y = 510 - 12
INV_NUM_X = 6
INV_NUM_Y = 2
INV_WIDTH = 76
INV_HEIGHT = 75

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

class Slot(GridViewCell):
    def __init__(self, x, y, width, height):

        # Call __init__ of parent class
        super().__init__(x, y, width, height)

        self.icon_x = x + 12
        self.icon_y = y + 12

        # This will be the number of this slot in inventory
        # It will be set later in InventoryGrid
        self.index = None

    def get_icon(self):                  # >>>> Tady se da ty icony
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

        }[item.name]

    def click(self):
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

        }[item.name]()

        if item is not None:
            inventory.remove_particular_item(item)

    def get_item(self):
        """
            Get Inventory Item corresponding to this
            particular Slot
        """
        try:
            return inventory.items[self.index]
        except IndexError:
            return None


class InventoryGrid(GridView):
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
            CellClass=Slot
        )

        self.slots = self.cells

        for index, slot in enumerate(self.slots):
            slot.index = index


class InventoryItem:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self):
        self.inventory_full = False
        self.items = [

        ]

    def max_items(self):
        self.max = 6
        self.min = 5
        if len(self.items) >= self.max:
            self.inventory_full = True
        if len(self.items) <= self.min:
            self.inventory_full = False

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

inventory = Inventory()
