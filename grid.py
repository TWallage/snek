import pygame as pg
import numpy as np

class Cell:
    """
    Individual Cell
    """

    def __init__(self, pos, size=40, contains=None) -> None:
        self.content = None
        self.size = size
        self.x, self.y = pos
        # x and y are the cells position in the grid, not screen coords#
        self.screen_x = self.size*self.x
        self.screen_y = self.size*self.y

    def __repr__(self) -> str:
        return str(self.content)

    def draw(self, screen: pg.Surface) -> None:
        if self.content is None:
            pg.draw.rect(screen,
                         (150, 150, 150),
                         (self.screen_x, self.screen_y, self.size, self.size),
                         width=1
                         )
        else:
            pg.draw.rect(screen,
                         (100, 150, 40),
                         (self.screen_x, self.screen_y, self.size, self.size),
                         )
            pg.draw.rect(screen,
                         (10, 100, 0),
                         (self.screen_x, self.screen_y, self.size, self.size),
                         width=2
                         )
            

class Grid:
    """
    Grid made up of Cells for snek game board
    """
    CELL_SIZE = 40

    def __init__(self, s_width: int, s_height: int) -> None:
        self.num_cols = s_width//self.CELL_SIZE
        self.num_rows = s_height//self.CELL_SIZE
        self.grid = [Cell((x, y), size=self.CELL_SIZE)for x in range(self.num_cols)
                     for y in range(self.num_rows)]

    def add_snake(self, x=None, y=None):
        if x is None:
            x = np.random.randint(0, self.num_cols)
        if y is None:
            y = np.random.randint(0, self.num_rows)
        self.grid[self._get_cell_index(x,y)].content = "Snake"

    def __repr__(self) -> str:
        return_val = ""
        for i, cell in enumerate(self.grid):
            if i != 0 and i % self.num_cols == 0:
                return_val += "\n"
            return_val += repr(cell) + " "
        return return_val

    def draw(self, screen: pg.Surface) -> None:
        """
        Draws grid to screen
        """
        for cell in self.grid:
            cell.draw(screen)

    def _get_cell_index(self, x, y) -> int:
        index = x + self.num_cols*y
        if index < len(self.grid):
            return index
        else:
            return 0

    def get_cell(self, x, y) -> Cell:
        return self.grid[self._get_cell_index(x, y)]
