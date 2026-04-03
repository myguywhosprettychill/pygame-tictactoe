import pygame
import random
import time

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

turn = "computer"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

screen.fill('White')

images = [pygame.transform.scale(pygame.image.load("blank.png").convert_alpha(), (160, 160)),
          pygame.transform.scale(pygame.image.load("x.png").convert_alpha(), (160, 160)),
          pygame.transform.scale(pygame.image.load("o.png").convert_alpha(), (160, 160))]

surface1 = images[0]
rect1 = surface1.get_rect()
rect1.topleft = ((WIDTH-440)/3,(HEIGHT-430)/3)
surface2 = images[0]
rect2 = surface2.get_rect()
rect2.topleft = ((WIDTH-370)/3*2,(HEIGHT-430)/3)
surface3 = images[0]
rect3 = surface3.get_rect()
rect3.topleft = (WIDTH-330,(HEIGHT-430)/3)
surface4 = images[0]
rect4 = surface4.get_rect()
rect4.topleft = ((WIDTH-410)/3,(HEIGHT-380)/3*2)
surface5 = images[0]
rect5 = surface5.get_rect()
rect5.topleft = ((WIDTH-320)/3*2,(HEIGHT-380)/3*2)
surface6 = images[0]
rect6 = surface6.get_rect()
rect6.topleft = (WIDTH-310,(HEIGHT-380)/3*2)
surface7 = images[0]
rect7 = surface7.get_rect()
rect7.topleft = ((WIDTH-440)/3,HEIGHT-350)
surface8 = images[0]
rect8 = surface8.get_rect()
rect8.topleft = ((WIDTH-370)/3*2,HEIGHT-350)
surface9 = images[0]
rect9 = surface9.get_rect()
rect9.topleft = (WIDTH-330,HEIGHT-350)

hor_surf = pygame.Surface((500, 10))
ver_surf = pygame.Surface((10, 500))

surfaces = [surface1, surface2, surface3, surface4, surface5, surface6, surface7, surface8, surface9]
rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]

def pick_square():
    global board
    global turn
    global surfaces
    global images
    loop = True
    print('looping comp...')
    while loop:
        square_num = random.randint(0, 8)
        if board[square_num] == "":
            board[square_num] = 'o'
            surfaces[square_num] = images[2]
            loop = False
    print(board)
    turn = "player"

def player_square(picked_square):
    global board
    global surfaces
    global turn
    global images
    print('picking square...')
    print(picked_square)
    if board[picked_square] == '':
        board[picked_square] = 'x'
        surfaces[picked_square] = images[1]
        turn = "computer"

def check_win(player):
    global board
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == "player":
                if rect1.collidepoint(event.pos):
                    player_square(0)
                elif rect2.collidepoint(event.pos):
                    player_square(1)
                elif rect3.collidepoint(event.pos):
                    player_square(2)
                elif rect4.collidepoint(event.pos):
                    player_square(3)
                elif rect5.collidepoint(event.pos):
                    player_square(4)
                elif rect6.collidepoint(event.pos):
                    player_square(5)
                elif rect7.collidepoint(event.pos):
                    player_square(6)
                elif rect8.collidepoint(event.pos):
                    player_square(7)
                elif rect9.collidepoint(event.pos):
                    player_square(8)

    if turn == "computer":
        pick_square()

    for i in range(9):
        screen.blit(surfaces[i], rects[i])

    screen.blit(hor_surf,((WIDTH-350)/3,(HEIGHT-360)/3*2))
    screen.blit(hor_surf,((WIDTH-350)/3,HEIGHT-340))
    
    screen.blit(ver_surf,((WIDTH-360)/3*2,(HEIGHT-350)/3))
    screen.blit(ver_surf,(WIDTH-330,(HEIGHT-350)/3))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    