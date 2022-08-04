from abc import ABC, abstractmethod
import pygame as pg

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