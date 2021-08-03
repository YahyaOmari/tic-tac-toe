import pygame, sys

pygame.init()

# Const variables
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
#RGB    
RED = (255,0,0)
BACKGROUND_COLOR = (20, 74, 254)
LINE_COLOR = (23, 105, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(BACKGROUND_COLOR)


def draw_lines():
    # Screen, line color, time position of line (), ending position of line (), width
        # 1 horizontal 
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
        # 2 horizontal 
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)

        # 1 vertical 
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200, 600), LINE_WIDTH)
        # 2 vertical 
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()