import pygame
from globals import game

class GridView:
    """
        Generic class for any grid (=e.g. Dungeon)
        Generates cells (=e.g. DungeonDoors) on given coordinates
        Checks which cell is clicked and calls it's own click()
        Draws all the cells
    """

    def create_cells(self, grid_x, grid_y, cell_width, cell_height, rows, cols, CellClass):
        """
            Create all cell objects with proper coordinates
            grid_x
            grid_y - Upper left corner of the grid

            cell_height
            cell_width - dimensions of the single cell

            rows
            cols - how many cells are there

            CellClass - what class to use to create cells (e.g. DungeonDoor)
                      - must be subclass of GridViewCell

            all cells are stored in self.cells
        """

        self.cells = []

        for row in range(rows):
            for column in range(cols):
                cell = CellClass(
                    x=grid_x + column * cell_width,
                    y=grid_y + row * cell_height,
                    width=cell_width,
                    height=cell_height
                )

                self.cells.append(cell)

    def click(self, x, y):
        """
            Finds cell that was clicked,
            and calls the cell's own click() method
        """
        for cell in self.cells:
            if cell.collide(x, y):
                cell.click()
                return

    def draw(self):
        """
            Draws all cells
        """
        for cell in self.cells:
            cell.draw()

    def right_click(self, x, y):
        """
            Finds cell that was clicked,
            and calls the cell's own click() method
        """
        for cell in self.cells:
            if cell.collide(x, y):
                cell.right_click()
                return


class GridViewCell:
    """
        One cell of a grid (=e.g. DungeonDoor)
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        
        # We use this rect to compute collision
        # (And draw it when we need to check it)
        self.rect = pygame.Rect(x, y, width, height)

    def collide(self, x, y):
        return self.rect.collidepoint(x, y)

    def draw(self):
        # Uncomment to check proper coordinates
        # pygame.draw.rect(game.screen, (255, 0, 0), self.rect, 1)

        # get icon that should be rendered
        # (this is method of the particular sub-class, e.g. DungeonDoor)
        icon = self.get_icon()

        if icon is None:
            return

        # render it. We assume that the sub-class has set icon_x and icon_y
        game.screen.blit(icon, (self.icon_x, self.icon_y))
