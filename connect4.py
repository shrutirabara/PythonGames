import numpy as np
import pygame
import sys
import math
import json

"""
declare global variables for:
board color (blue - 0, 0, 255),
empty spot color (black - 0, 0, 0),
player 1 chip color (red - 255, 0, 0),
player 2 chip color (yellow - 255, 255, 0)
number of rows (6)
number of columns (7)

You may use any colors you wish, but
the common colors are listed with their
rgb values. You may also change the size
of the board to experiment.
"""
BOARD_COLOR = (0, 0, 255)
SPOT_COLOR = (0, 0, 0)
P1_COLOR = (255, 0, 0)
P2_COLOR = (255, 255, 0)

ROWS = 6
COLUMNS = 7

def loc_works(board, column):
    '''
    Returns True or False based on a check to see if 
    the selected column on the board is full, or if 
    it is playable.

    Parameters
    ----------
    board : ndarray
    column : int

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    ROWS
    '''
    return board[ROWS - 2][column] == 0

def next_row(board, column):
    '''
    Returns the index of the next available row within the column.

    Parameters
    ----------
    board = ndarray
    column = int

    Returns
    -------
    row = int
    '''
    for row in range(ROWS):
        if board[row][column] == 0:
            return row

def print_board(board):
    '''
    Print a vertically flipped version of the board to the console.

    Parameters
    ----------
    board = ndarray

    Implements (See also)
    ---------------------
    numpy.flip(array, axis)
    '''
    print(np.flip(board, 0))

def make_board():
    '''
    Returns a numpy array with a shape of (ROWS, COLUMNS)

    Returns
    -------
    board = ndarray

    Implements (See also)
    ---------------------
    ROWS
    COLUMNS
    numpy.zeros(shape)
    '''
    board = np.zeros((ROWS, COLUMNS))
    return board

def win_check(board, chip):
    '''
    Checks for combos of 4 along vertical, horizontal, and 
    negatively and positively sloped diagonal lines.

    Parameters
    ----------
    board = ndarray
    chip = int

    Returns
    -------
    True : bool
    '''
    for column in range(COLUMNS - 3):
        for row in range(ROWS):
            if board[row][column] == chip \
            and board[row][column + 1] == chip \
            and board[row][column + 2] == chip \
            and board[row][column + 3] == chip:
                return True

    for column in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][column] == chip \
            and board[row + 1][column] == chip \
            and board[row + 2][column] == chip \
            and board[row + 3][column] == chip:
                return True

    for column in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if board[row][column] == chip \
            and board[row + 1][column + 1] == chip \
            and board[row + 2][column + 2] == chip \
            and board[row + 3][column + 3] == chip:
                return True

    for column in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if board[row][column] == chip \
            and board[row - 1][column + 1] == chip \
            and board[row - 2][column + 2] == chip \
            and board[row - 3][column + 3] == chip:
                return True

def play_c4():
    '''
    Initializes and maintains the primary game loop. 
    Renders the board in a new window via pygame,
    tracks events such as exit, mouse movement, and 
    mouse clicks.

    Implements (See also)
    ---------------------
    global variables --
        COLUMNS : int
        ROWS : int
        BOARD_COLOR : tuple of 3 ints
        SPOT_COLOR : tuple of 3 ints
        P1_COLOR : tuple of 3 ints
        P2_COLOR : tuple of 3 ints

    self-made functions --
        make_board()
        print_board(board)
        loc_works(board, column)
        next_row(board, column)
        win_check(board, chip)

    internal functions --
        draw_board(board)
        place_chip(board, row, column, chip)

    module functions --
        math.floor(int)
        sys.exit()
        pygame
            .init()
            .display
                .set_mode(size)
                .update()
                .blit(source, destination)
            .draw
                .rect(surface, color, rect)
                .circle(surface, color, center, radius)
            .font
                .Sysfont(name, size)
                .render
            .event.get()
            .QUIT
            .MOUSEMOTION
            .MOUSECLICK
            .time.wait(milliseconds)
    '''

    def draw_board(board):
        '''
        Use pygame to draw the board in a new window.

        Parameters
        ----------
        board : ndarray

        Returns
        -------
        None

        Implements (See also)
        ---------------------
        COLUMNS : int
        ROWS : int
        BOARD_COLOR
        SPOT_COLOR
        P1_COLOR
        P2_COLOR

        pygame
            .draw
                .rect(surface, color, rect)
                .circle(surface, color, center, radius)
            .display.update()
        
        '''
        for column in range(COLUMNS):
            for row in range(ROWS):
                pygame.draw.rect(   
                    screen, 
                    BOARD_COLOR, 
                    (
                        column * screen_size, 
                        row * screen_size + screen_size,
                        screen_size, 
                        screen_size
                    )
                )
                pygame.draw.circle( 
                    screen, 
                    SPOT_COLOR, 
                    (
                        int(column * screen_size + screen_size/2), 
                        int(row * screen_size + screen_size + screen_size/2)
                    ), 
                    circle_radius
                )

        for column in range(COLUMNS):
            for row in range(ROWS):      
                if board[row][column] == 1:
                    pygame.draw.circle( 
                        screen,
                        P1_COLOR,
                        (
                            int(column * screen_size + screen_size / 2),
                            screen_height - int(row * screen_size + screen_size / 2)
                        ), 
                        circle_radius
                    )
                elif board[row][column] == 2: 
                    pygame.draw.circle( 
                        screen, 
                        P2_COLOR, 
                        (
                            int(column * screen_size + screen_size / 2), 
                            screen_height - int(row * screen_size + screen_size / 2)
                        ), 
                        circle_radius
                    )
        pygame.display.update()

    def place_chip(board, row, column, chip):
        '''
        Assigns the current player's chip to the selected spot
        on the board.

        Parameters
        ----------
        board = ndarray
        row = int
        column = int
        chip = int
        '''
        board[row][column] = chip

    with open("scores.json", "r") as f:
        scores = json.load(f)
    player1_wins = 0
    player2_wins = 0

    c4_board = make_board()
    print_board(c4_board)
    game_over = False
    turn = 0

    pygame.init()

    screen_size = 100
    circle_radius = int(screen_size / 2 - 5) 
    screen_width = COLUMNS * screen_size
    screen_height = ROWS * screen_size
    size = (screen_width, screen_height)
    screen = pygame.display.set_mode(size)

    draw_board(c4_board)
    game_font = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(   
                    screen, 
                    SPOT_COLOR, 
                    (
                        0, 
                        0 , 
                        screen_width, 
                        screen_size
                    )
                )
                x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(
                        screen, 
                        P1_COLOR, 
                        (
                            x, 
                            int(screen_size / 2)
                        ), 
                        circle_radius
                    )
                else:
                    pygame.draw.circle(
                        screen, 
                        P2_COLOR, 
                        (
                            x, 
                            int(screen_size / 2)
                        ), 
                        circle_radius
                    )

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(
                    screen, 
                    SPOT_COLOR, 
                    (
                        0, 
                        0, 
                        screen_width, 
                        screen_size
                    )
                )

                if turn == 0:
                    x = event.pos[0]
                    column = int(math.floor(x / screen_size))

                    if loc_works(c4_board, column):
                        row = next_row(c4_board, column)
                        place_chip(c4_board, row, column, 1)

                        if win_check(c4_board, 1):
                            label = game_font.render("P1 wins!", 1, P1_COLOR)
                            screen.blit(label, (40, 10))
                            player1_wins += 1
                            game_over = True

                else:
                    x = event.pos[0]
                    column = int(math.floor(x/screen_size))

                    if loc_works(c4_board, column):
                        row = next_row(c4_board, column)
                        place_chip(c4_board, row, column, 2)

                        if win_check(c4_board, 2):
                            label = game_font.render("P2 wins!", 2, P2_COLOR)
                            screen.blit(label, (40, 10))
                            player2_wins += 1
                            game_over = True

                

                print_board(c4_board)
                draw_board(c4_board)

                turn += 1
                turn = turn % 2

                if game_over:
                    
                    pygame.quit()

    
    scores["player1"]["wins"] += player1_wins
    scores["player2"]["wins"] += player2_wins

    with open("scores.json", "w") as f:
        json.dump(scores, f)
