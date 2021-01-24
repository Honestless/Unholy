import pygame
from buttons import buttons
from random import choice
from lcrender import left_column
from globals import game, white
from fontz import fontz
from grid_view import GridView, GridViewCell
from icons import img
from dungeon_events import ActivityTypes, NoActivity
from battlesc import dungeonlevel
back_button_left = pygame.Rect(0, 595, 130, 55)
clock = pygame.time.Clock()
dungeon_level_text = fontz.font_40.render("You found gold!", True, white, 1)
DUNGEON_X = 140    # 167
DUNGEON_Y = 335   # 350
DUNGEON_NUM_X = 6
DUNGEON_NUM_Y = 4
DOOR_WIDTH = 110
DOOR_HEIGHT = 80


class Dungeon(GridView):
    def __init__(self):
        self.create_cells(
            grid_x=DUNGEON_X,
            grid_y=DUNGEON_Y,
            cell_width=DOOR_WIDTH,
            cell_height=DOOR_HEIGHT,
            rows=DUNGEON_NUM_Y,
            cols=DUNGEON_NUM_X,
            CellClass=DungeonDoor
        )

        # Just alias - we want to call the cells doors
        self.doors = self.cells

        for door in self.doors:
            door.icon = img.door_icon


class DungeonDoor(GridViewCell):
    def __init__(self, x, y, width, height):

        # Call __init__ of parent class
        super().__init__(x, y, width, height)

        self.icon_x = x + 27
        self.icon_y = y + 15

        self.activity = None
        self.has_player = False

    def get_icon(self):
        if self.has_player:
            return img.player_icon

        if self.activity is None:
            return img.door_icon
        elif self.activity.icon is not None:
            return self.activity.icon

    def click(self):
        if abs(self.icon_x - player.x) <= DOOR_WIDTH and abs(self.icon_y - player.y) <= DOOR_WIDTH:
            if self.activity is None:
                self.activity = choice(ActivityTypes)()
                return
        if abs(self.icon_x - player.x) <= DOOR_WIDTH and abs(self.icon_y - player.y) <= DOOR_WIDTH:
            if isinstance(self.activity, NoActivity):
                player.door.has_player = False
                self.has_player = True
                player.door = self
                player.x = self.icon_x
                player.y = self.icon_y
            self.activity = self.activity.activate()


class Player:
    def __init__(self):
        self.image = img.player_icon
        self.x = 167
        self.y = 350
        self.door = None

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

player = Player()

def dungeon_level_01():
    global player

    player = Player()
    dungeon = Dungeon()
    dungeon.doors[0].has_player = True
    dungeon.doors[0].activity = NoActivity()
    player.door = dungeon.doors[0]

    running = True
    while running:
        game.screen.fill((0, 0, 0))
        game.screen.blit(img.dl1_ui, (0, 0))
#        screen.blit(dg_level_text, (550, 8))
        dungeonlevel.draw()
        dungeon.draw()
        left_column.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    dungeon.click(mx, my)
                    if buttons.back_button_left.collidepoint(mx, my):
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        clock.tick(60)
        pygame.display.update()
