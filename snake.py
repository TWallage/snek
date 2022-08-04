import pygame as pg
from grid import Grid
from cell_content import Cell_content
from food import Food

class Snake:
    """
    Controls the snake on the game board
    """
    # direction constants
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    frame_count = 0
    frame_length = 7

    def __init__(self, game_board: Grid, x: int = None, y: int = None, length=1) -> None:
        """
        x and y are cell positions on the game board that the snake will start, 
        if None then the center of the game board is used
        """
        self.board = game_board
        if x is None:
            self.x = self.board.num_cols//2
        else:
            self.x = x

        if y is None:
            self.y = self.board.num_rows//2
        else:
            self.y = y

        self.length = length
        self.direction = self.RIGHT
        self.snake_cells = [self.board.get_cell(self.x + (-i*self.direction[0]),
                                                self.y + (-i*self.direction[1]))
                            for i in range(self.length)]

        # set first snake cell contents to Snake_head
        self.snake_cells[0].set_content(Snake_head(self.direction))
        for cell in self.snake_cells[1:]:
            cell.set_content(Snake_body(self.direction))

    def update(self) -> None:
        """ Update snake """
        self.frame_count += 1
        if self.frame_count < self.frame_length:
            return
        else:
            self.frame_count = 0
        self.move_snake()

    def change_direction(self, new_direction)->None:
        if (self.direction[0] + new_direction[0]) == 0:
            return
        if (self.direction[1] + new_direction[1]) == 0:
            return
        else: self.direction = new_direction

    def move_snake(self) -> None:
        """ Move snake """
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        new_x, new_y = self.board.wrap_coords(new_x, new_y)

        self.check_next_cell(new_x, new_y)

        self.snake_cells[-1].set_content(None)
        self.snake_cells = [self.board.get_cell(
            new_x, new_y)] + self.snake_cells[:-1]
        self.snake_cells[0].set_content(Snake_head(self.direction))
        if self.length > 1:
            self.snake_cells[1].set_content(Snake_body(self.direction))
        self.x = new_x
        self.y = new_y

    def check_next_cell(self, new_x: int, new_y: int) -> None:
        next_cell = self.board.get_cell(new_x, new_y)
        if next_cell.content is None:
            return
        if isinstance(next_cell.content, Snake_body):
            if next_cell is self.snake_cells[-1]:
                return
            else:
                from game import game_over
                pg.event.post(pg.event.Event(game_over))
                return
        if isinstance(next_cell.content, Food):
            next_cell.set_content(None)
            self.add_cell()
            self.board.regen_food()
            return
    
    def add_cell(self)->None:
        if len(self.snake_cells) == 1:
            self.snake_cells.append(self.board.get_cell(self.x - (self.direction[0]),
                                                self.y - (self.direction[1])))
            self.snake_cells[1].set_content(Snake_body(self.direction))
        else:
            self.snake_cells.append(self.snake_cells[-1])
        
        self.length = self.length + 1
        

            


class Snake_head(Cell_content):
    """
    Snake head
    """

    def __init__(self, direction) -> None:
        self.direction = direction
        self.image = pg.image.load('Snake_head.png').convert()

    def update(self, direction=None) -> None:
        if not direction is None and direction != self.direction:
            self.direction = direction

    def draw(self, screen: pg.Surface, screen_x: int, screen_y: int, size: int):
        screen.blit(self.image, (screen_x, screen_y))


class Snake_body(Cell_content):
    """
    Snake body
    """

    def __init__(self, direction) -> None:
        self.direction = direction

    def update(self, direction=None) -> None:
        if not direction is None and direction != self.direction:
            self.direction = direction

    def draw(self, screen: pg.Surface, screen_x: int, screen_y: int, size: int):
        pg.draw.rect(screen, (100, 150, 40), (screen_x, screen_y, size, size))
        pg.draw.rect(screen,
                     (10, 100, 0),
                     (screen_x, screen_y, size, size),
                     width=1
                     )
