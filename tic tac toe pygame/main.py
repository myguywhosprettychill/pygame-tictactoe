import pygame
import random

WIDTH = 800
HEIGHT = 800

board = ["", "", "",
         "", "", "",
         "", "", ""]

win_conditions = [
    (0, 1, 2),  # top row
    (3, 4, 5),  # middle row
    (6, 7, 8),  # bottom row
    (0, 3, 6),  # left column
    (1, 4, 7),  # middle column
    (2, 5, 8),  # right column
    (0, 4, 8),  # diagonal
    (2, 4, 6)   # diagonal
]

wins = 0

turn = "player"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

screen.fill('White')

images = [pygame.image.load("blank.png"),
          pygame.image.load("x.png"),
          pygame.image.load("o.png")]

surface1 = images[0]
rect1 = surface1.get_rect()
surface2 = images[0]
rect2 = surface2.get_rect()
surface3 = images[0]
rect3 = surface3.get_rect()
surface4 = images[0]
rect4 = surface4.get_rect()
surface5 = images[0]
rect5 = surface5.get_rect()
surface6 = images[0]
rect6 = surface6.get_rect()
surface7 = images[0]
rect7 = surface7.get_rect()
surface8 = images[0]
rect8 = surface8.get_rect()
surface9 = images[0]
rect9 = surface9.get_rect()

hor_surf = pygame.Surface((500, 20))

surfaces = [surface1, surface2, surface3, surface4, surface5, surface6, surface7, surface8, surface9]

def pick_square():
    global board
    global turn
    loop = True
    while loop:
        square_num = random.randint(0, 8)
        if board[square_num] != 'o':
            board[square_num] = "o"
            loop = False
    turn = "player"

def player_square(picked_square):
    global board
    turn = "computer"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if turn == "player":
            if rect1.collidepoint(event.pos):
                pick_square(surface1)
            elif rect2.collidepoint(event.pos):
                pick_square(surface2)
            elif rect3.collidepoint(event.pos):
                pick_square(surface3)
            elif rect4.collidepoint(event.pos):
                pick_square(surface4)
            elif rect5.collidepoint(event.pos):
                pick_square(surface5)
            elif rect6.collidepoint(event.pos):
                pick_square(surface6)
            elif rect7.collidepoint(event.pos):
                pick_square(surface7)
            elif rect8.collidepoint(event.pos):
                pick_square(surface8)
            elif rect9.collidepoint(event.pos):
                pick_square(surface9)

    screen.blit(surface1,((WIDTH-350)/3,(HEIGHT-350)/3), rect1)
    screen.blit(surface2,((WIDTH-350)/3*2,(HEIGHT-350)/3), rect2)
    screen.blit(surface3,(WIDTH-350,(HEIGHT-350)/3), rect3)
    screen.blit(surface4,((WIDTH-350)/3,(HEIGHT-350)/3*2), rect4)
    screen.blit(surface5,((WIDTH-350)/3*2,(HEIGHT-350)/3*2), rect5)
    screen.blit(surface6,(WIDTH-350,(HEIGHT-350)/3*2), rect6)
    screen.blit(surface7,((WIDTH-350)/3,HEIGHT-350), rect7)
    screen.blit(surface8,((WIDTH-350)/3*2,HEIGHT-350), rect8)
    screen.blit(surface9,(WIDTH-350,HEIGHT-350), rect9)

    screen.blit(hor_surf,((WIDTH-350)/3,(HEIGHT-350)/3*2))
    screen.blit(hor_surf,((WIDTH-350)/3,HEIGHT-350))

    pygame.display.update()
    clock.tick(60)
    