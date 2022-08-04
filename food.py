import pygame as pg
from cell_content import Cell_content

class Food(Cell_content):
    def __init__(self, direction=None) -> None:
        self.direction = direction
    def update(self, new_direction=None) -> None:
        self.direction = new_direction
    def draw(self, screen: pg.Surface, screen_x: int, screen_y: int, size: int) -> None:
        pg.draw.circle(screen,
         (150, 10, 0),
          center = (screen_x+(size//2), screen_y+(size//2)),
          radius = size//2)
        pg.draw.circle(screen,
         (10,10,10),
          center = (screen_x+(size//2), screen_y+(size//2)),
          radius = size//2,
          width=2)