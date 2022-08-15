import pygame as pg
from grid import Grid
from snake import Snake

game_over = pg.USEREVENT + 0

class Game:
    """
    Class for handling the game
    """
    # Define Constants
    FPS = 60
    SCREEN_SIZE = WIDTH, HEIGHT = (32*40,24*40)
    BG_COLOUR = (200,200, 220)

    def __init__(self) -> None:
        """
        Initiallizes pygame and create window surface
        """
        # initialize pygame
        pg.init()
        # get screen surface
        self.screen = pg.display.set_mode(self.SCREEN_SIZE)
        pg.display.set_caption('Snek')
        # set background colour
        self.screen.fill(self.BG_COLOUR)
        # update display
        pg.display.update()
        # create clock
        self.clock = pg.time.Clock()
    
    def start(self) -> None:
        """
        Starts game loop
        """
        # check if pygame has be initialized
        print(pg.get_init())
        # create game board
        game_board = Grid(self.WIDTH, self.HEIGHT)
        # create snake
        self.snake = Snake(game_board,length=1)
        # debugging
        print(repr(game_board))
        game_board.draw(self.screen)

        food_cell = game_board.regen_food()
        # start game loop
        running = True
        while running:
            # check for events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == game_over:
                    print("Game over")
                    print(self.snake.length)
                    running = False
                if event.type == pg.KEYDOWN:
                    self.input_control(event)



            # draw game board
            game_board.draw(self.screen)
            # update snake
            self.snake.update()
            # update display
            pg.display.update()
            # FPS tick rate
            self.clock.tick(self.FPS)
            # print(self.clock.get_fps())
            # wipe the screen ready for next frame
            self.screen.fill(self.BG_COLOUR)

        pg.quit()
        
    def input_control(self, event:pg.event.Event):
        if event.key == pg.K_w or event.key == pg.K_UP:
            self.snake.change_direction(self.snake.UP)
        if event.key == pg.K_s or event.key == pg.K_DOWN:
            self.snake.change_direction(self.snake.DOWN)
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.snake.change_direction(self.snake.LEFT)
        if event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.snake.change_direction(self.snake.RIGHT)
