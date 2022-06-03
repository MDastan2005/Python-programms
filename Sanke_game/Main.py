import pygame
import random
import arguments as arg
import time


def random_cor():
    ans1 = random.randint(1, arg.ROWS - 1)
    ans2 = random.randint(1, arg.COLUMNS - 1)
    return ans1, ans2


def draw_table():
    for i in range(1, arg.ROWS):
        for j in range(1, arg.COLUMNS):
            if snake[i][j]:
                if (i, j) == snake_head:
                    color = arg.GREEN
                else:
                    color = arg.LIGHT_GREEN
            elif (i, j) == apple_cor:
                color = arg.RED
            elif (i + j) % 2 == 0:
                color = arg.BROWN
            else:
                color = arg.BROWN2
            x = i * arg.BLOCK_SIZE
            y = j * arg.BLOCK_SIZE
            pygame.draw.rect(screen, color, (x, y, arg.BLOCK_SIZE, arg.BLOCK_SIZE))


def snake_slew(pressed_key):
    global snake_direct
    if pressed_key == pygame.K_UP:
        if snake_direct != 4:
            snake_direct = 3
        return
    elif pressed_key == pygame.K_DOWN:
        if snake_direct != 3:
            snake_direct = 4
        return
    elif pressed_key == pygame.K_RIGHT:
        if snake_direct != 1:
            snake_direct = 2
        return
    elif pressed_key == pygame.K_LEFT:
        if snake_direct != 2:
            snake_direct = 1
        return


def you_lose():
    screen.fill(arg.BLACK)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                exit(0)


def check(x, y):
    return (x >= 1 and y >= 1 and y < arg.ROWS and x < arg.COLUMNS)


def snake_move():
    if not snake_direct:
        return
    global snake_head, snake_tail, apple_gived, apple_cor, snake_len
    x, y = snake_head
    x1, y1 = snake_tail
    snake_head = (x + dx[snake_direct], y + dy[snake_direct])
    x2, y2 = snake_head
    if (not check(x2, y2)) or snake[x2][y2]:
        you_lose()
    snake_pred[x2][y2] = (x, y)
    snake[x + dx[snake_direct]][y + dy[snake_direct]] = 1
    if snake_head == apple_cor:
        apple_gived = 0
        apple_cor = 0
        snake_len += 1
        snake_pred[x2][y2] = (x, y)
        print(snake_len)
        return
    snake[x1][y1] = 0
    snake_pred[x1][y1] = (0, 0)
    while (x, y) != (x1, y1):
        x2, y2 = x, y
        x, y = snake_pred[x][y]
    snake_tail = (x2, y2)


def set_apple():
    global apple_cor, apple_gived
    apple_gived = 1
    apple_cor = random_cor()
    while True:
        x, y = apple_cor
        if not snake[x][y]:
            break
        apple_cor = random_cor()


frame_speed = 1
screen = pygame.display.set_mode(arg.WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Standard Snake')
snake = [[0] * arg.COLUMNS for i in range(arg.ROWS)]
x, y = arg.ROWS // 2, arg.COLUMNS // 2
snake[x][y] = 1
snake_pred = [[(0, 0)] * arg.COLUMNS for i in range(arg.ROWS)]
snake_direct = 0
snake_head = (x, y)
snake_tail = (x, y)
snake_len = 1
apple_cor = (0, 0)
apple_gived = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
#1 = left, 2 = right, 3 = up, 4 = down
start_time = time.time()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            snake_slew(event.key)
    if not apple_gived:
        set_apple()
    stop_time = pygame.time.get_ticks() + 250
    snake_move()
    while (pygame.time.get_ticks() < stop_time):
        continue
    screen.fill(arg.BLUE)
    draw_table()
    pygame.display.flip()
    if time.time() - start_time >= 5:
        start_time += 5
        frame_speed += 0.5
    clock.tick(frame_speed)
