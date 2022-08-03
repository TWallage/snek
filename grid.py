import pygame as pg
import numpy as np

from abc import ABC, abstractmethod

class Cell_content(ABC):
    """
    Abstact class decribing cell content
    """
    direction = None
    @abstractmethod
    def __init__(self, direction = None) -> None:
        """
        initialize cell content
        """
        ...
    @abstractmethod
    def update(self, new_direction = None) -> None:
        """
        update cell content
        """
        ...
    @abstractmethod
    def draw(self, screen:pg.Surface, screen_x:int, screen_y:int, size:int)->None:
        """
        draw content of cell to screen
        """
        ...

class Cell:
    """
    Individual Cell
    """

    def __init__(self, pos, size=40, contains:Cell_content=None) -> None:
        self.content = contains
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
            self.content.draw(screen, self.screen_x, self.screen_y, self.size)
    
    def set_content(self, new_content:Cell_content)->None:
        self.content = new_content

class Grid:
    """
    Grid made up of Cells for snek game board
    """
    CELL_SIZE = 40

    def __init__(self, s_width: int, s_height: int) -> None:
        self.num_cols = s_width//self.CELL_SIZE
        self.num_rows = s_height//self.CELL_SIZE
        self.grid = [Cell((x, y), size=self.CELL_SIZE)for y in range(self.num_rows)
                     for x in range(self.num_cols)]
    
    @property
    def shape(self):
        return (self.num_cols, self.num_rows)

    def __repr__(self) -> str:
        return_val = ""
        for i, cell in enumerate(self.grid):
            if i != 0 and i % self.num_cols == 0:
                return_val += "\n"
            return_val += repr(cell) + " "
        return return_val
    """
    def add_snake(self, x=None, y=None):
        if x is None:
            x = np.random.randint(0, self.num_cols)
        if y is None:
            y = np.random.randint(0, self.num_rows)
        self.grid[self.get_cell_index(x,y)].content = "Snake"
    """
    def draw(self, screen: pg.Surface) -> None:
        """
        Draws grid to screen
        """
        for cell in self.grid:
            cell.draw(screen)

    def get_cell_index(self, x:int, y:int) -> int:
        if not self.check_bounds(x,y):
            raise IndexError("(x,y) outside grid")
        index = x + self.num_cols*y
        if index < len(self.grid):
            return index
        else:
            return 0

    def get_cell(self, x:int, y:int) -> Cell:
        return self.grid[self.get_cell_index(x, y)]
    
    def check_bounds(self, x:int, y:int) -> bool:
        return 0 <= x < self.num_cols and 0 <= y < self.num_rows

    def wrap_coords(self, x:int, y:int):
        if x < 0:
            x = self.num_cols-1
        if x >= self.num_cols:
            x = 0
        if y < 0:
            y = self.num_rows-1
        if y >= self.num_rows:
            y = 0
        
        return (x,y)
