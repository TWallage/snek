import pygame as pg
from grid import Grid

class Game:
    """
    Class for handling the game
    """
    # Define Constants
    FPS = 60
    SCREEN_SIZE = WIDTH, HEIGHT = (640,480)
    BG_COLOUR = (200,200, 220)

    def __init__(self) -> None:
        """
        Initiallizes pygame and create window surface
        """
        pg.init()
        self.screen = pg.display.set_mode(self.SCREEN_SIZE)
        pg.display.set_caption('Snek')
        self.screen.fill(self.BG_COLOUR)
        pg.display.update()
        self.clock = pg.time.Clock()
    
    def start(self) -> None:
        """
        Starts game loop
        """
        print(pg.get_init())
        
        game_board = Grid(self.WIDTH, self.HEIGHT)
        game_board.add_snake()
        print(repr(game_board))
        game_board.draw(self.screen)
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            game_board.add_snake()
            game_board.draw(self.screen)
            pg.display.update()
            self.clock.tick(self.FPS)
            print(self.clock.get_fps())
        pg.quit()
        
