import random

import pygame

field = []
screen = None
field_size = []
EMPTY = 100
APPLE = 101


def init_game_field(WIDTH, HEIGHT, screen_init):
    global screen
    screen = screen_init

    #draw field
    SAND = ('#F0FF00')
    ORANGE = ('#b7410e')
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, ORANGE, (20, 20), (20, HEIGHT - 20), 4)
    pygame.draw.line(screen, ORANGE, (20, 20), (WIDTH - 20, 20), 4)
    pygame.draw.line(screen, ORANGE, (WIDTH - 20, 20), (WIDTH - 20, HEIGHT - 20), 4)
    pygame.draw.line(screen, ORANGE, (20, HEIGHT - 20), (WIDTH - 20, HEIGHT - 20), 4)

    global field_size_y, field_size_x
    field_size_y = 0
    field_size_x = 0
    for i in range(40, HEIGHT - 20, 20):
        pygame.draw.line(screen, SAND, (20, i), (WIDTH - 20, i), 1)
        field_size_x += 1
    for i in range(40, WIDTH - 20, 20):
        pygame.draw.line(screen, SAND, (i, 20), (i, HEIGHT - 20), 1)
        field_size_y += 1

    field_size.append(field_size_x)
    field_size.append(field_size_y)

    #init field matrix
    for i in range(field_size_x):
        list_y = [EMPTY for i in range(0, field_size_y)]
        field.append(list_y)

def draw_apple(x,y):
    global screen
    pygame.draw.circle(screen, '#f80000', (30+y*20, 30+x*20), 7)

def draw_snake_segment(x,y):
    global screen
    pygame.draw.rect(screen, '#00a550', (23+y*20, 23+x*20, 15, 15))

def draw_snake_head(x,y):
    global screen
    pygame.draw.rect(screen, '#00db6a', (23+y*20, 23+x*20, 15, 15))

def create_snake(id):
    global field_size
    snake_head_position = [random.randint(0,field_size[0]-1), random.randint(1,field_size[1]-3)]
    snake_tail_position = [snake_head_position[0], snake_head_position[1]+1]
    while field[snake_head_position[0]][snake_head_position[1]] != EMPTY \
            or field[snake_tail_position[0]][snake_tail_position[1]]!= EMPTY \
            or field[snake_head_position[0]][snake_head_position[1]-1]!= EMPTY \
            or field[snake_tail_position[0]][snake_tail_position[1]+1]!= EMPTY:
        snake_head_position = [random.randint(0, field_size[0]-1), random.randint(1, field_size[1] - 2)]
        snake_tail_position = [snake_head_position[0], snake_head_position[1] + 1]
    field[snake_head_position[0]][snake_head_position[1]] = id
    field[snake_tail_position[0]][snake_tail_position[1]] = id
    draw_snake_head(snake_head_position[0],snake_head_position[1])
    draw_snake_segment(snake_tail_position[0], snake_tail_position[1])
    return snake_head_position, snake_tail_position

