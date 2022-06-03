import pygame
WINDOW_SIZE = [400, 400]
BLOCK_SIZE = 100
BROWN = (160, 82, 45)
CONST_LEN = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def readKey():
    global table, table_cor, cnt, who_move
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                table_cor = [[(0, 0)] * 3 for i in range(3)]
                cnt = 0
                for i in range(3):
                    for j in range(3):
                        x = i * BLOCK_SIZE + i + CONST_LEN
                        y = j * BLOCK_SIZE + j + CONST_LEN
                        table_cor[i][j] = (x, y)
                who_move = 1
                return


def draw_table():
    for i in range(3):
        for j in range(3):
            x = i * BLOCK_SIZE + i + CONST_LEN
            y = j * BLOCK_SIZE + j + CONST_LEN
            pygame.draw.rect(screen, BROWN, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            if table[i][j] == 1:
                pygame.draw.line(screen, WHITE, [x + 10, y + 10], [x + BLOCK_SIZE - 10, y + BLOCK_SIZE - 10], 5)
                pygame.draw.line(screen, WHITE, [x + 10, y + BLOCK_SIZE - 10], [x + BLOCK_SIZE - 10, y + 10], 5)
            if table[i][j] == 2:
                pygame.draw.circle(screen, WHITE, ((x + x + BLOCK_SIZE) // 2, (y + y + BLOCK_SIZE) // 2), 40, 5)


def cor_block(x, y):
    for i in range(3):
        for j in range(3):
            a, b = table_cor[i][j]
            c, d = (a + BLOCK_SIZE, b + BLOCK_SIZE)
            if a <= x <= c and b <= y <= d:
                return i, j
    return -1, -1


def process_click(posx, posy):
    global who_move, cnt
    x, y = cor_block(posx, posy)
    if (x == -1 and y == -1) or table[x][y] != 0:
        return
    cnt += 1
    if who_move == 1:
        table[x][y] = 1
        who_move = 2
    else:
        table[x][y] = 2
        who_move = 1


def print_winner(who):
    screen.fill(BLACK)
    if who == 1:
        pygame.draw.line(screen, WHITE, [50, 50], [350, 350], 10)
        pygame.draw.line(screen, WHITE, [50, 350], [350, 50], 10)
        pygame.display.flip()
        readKey()
    else:
        pygame.draw.circle(screen, WHITE, (200, 200), 175, 10)
        pygame.display.flip()
        readKey()


def print_draw():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [20, 100], [200, 280], 10)
    pygame.draw.line(screen, WHITE, [20, 280], [200, 100], 10)
    pygame.draw.circle(screen, WHITE, (300, 200), 100, 10)
    pygame.display.flip()
    readKey()


def is_game_ended():
    for i in range(3):
        if table[i][0] != 0 and table[i][0] == table[i][1] and table[i][0] == table[i][2]:
            print_winner(table[i][0])
        elif table[0][i] != 0 and table[0][i] == table[1][i] and table[0][i] == table[2][i]:
            print_winner(table[0][i])
    if table[1][1] != 0 and ((table[1][1] == table[2][2] and table[1][1] == table[0][0]) or (table[0][2] == table[1][1] and table[1][1] == table[2][0])):
        print_winner(table[1][1])
    if cnt == 9:
        print_draw()


screen = pygame.display.set_mode(WINDOW_SIZE)
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
table_cor = [[(0, 0)] * 3 for i in range(3)]
cnt = 0
for i in range(3):
    for j in range(3):
        x = i * BLOCK_SIZE + i + CONST_LEN
        y = j * BLOCK_SIZE + j + CONST_LEN
        table_cor[i][j] = (x, y)
who_move = 1
# 1 = cross , 2 = zero


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            process_click(x, y)
            is_game_ended()
    screen.fill(BLACK)
    draw_table()
    pygame.display.flip()
