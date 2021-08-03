import pygame, sys
import numpy as np

pygame.init()

# Const variables
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLUMN = 3
#RGB    
RED = (255,0,0)
BACKGROUND_COLOR = (20, 74, 254)
LINE_COLOR = (23, 105, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(BACKGROUND_COLOR)

# board
board = np.zeros((BOARD_ROWS,BOARD_COLUMN))

def draw_lines():
    # 1 horizontal 
        # Screen, line color, time position of line (), ending position of line (), width
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
    # 2 horizontal 
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)

    # 1 vertical 
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200, 600), LINE_WIDTH)
    # 2 vertical 
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# marking a square
def mark_square(row, col, player):
    board[row][col] = player


# check if square is available, it will return true
def available_square(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False

# returns true if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMN):
            if board[row][col] == 0:
                return False
    return True


draw_lines()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()