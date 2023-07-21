import random

import pygame

field = []
snakes_coord = []
screen = None
field_size = []
EMPTY = 100
APPLE = 101
LEFT = 7
DIRECTLY = 8
RIGHT = 9

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
    field_size_y = 1
    field_size_x = 1
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

def create_apple(x,y):
    draw_apple(x, y)
    field[x][y] = APPLE

def draw_snake_segment(x,y):
    global screen
    pygame.draw.rect(screen, '#00a550', (23+y*20, 23+x*20, 15, 15))

def create_snake_segment(x,y, id):
    draw_snake_segment(x,y)
    field[x][y] = id

def draw_snake_head(x,y):
    global screen
    pygame.draw.rect(screen, '#00db6a', (23+y*20, 23+x*20, 15, 15))

def create_snake_head(x,y, id):
    draw_snake_head(x,y)
    field[x][y] = id

def draw_empty(x,y):
    global screen
    pygame.draw.rect(screen, '#000000', (23+y*20, 23+x*20, 15, 15))


def create_snake(id):
    # random.seed(4)
    snake_head_position = [random.randint(1,field_size[0]-2), random.randint(1,field_size[1]-3)]
    snake_tail_position = [snake_head_position[0], snake_head_position[1]+1]
    while field[snake_head_position[0]][snake_head_position[1]] != EMPTY \
            or field[snake_tail_position[0]][snake_tail_position[1]]!= EMPTY \
            or field[snake_tail_position[0]-1][snake_tail_position[1]] != EMPTY \
            or field[snake_tail_position[0]+1][snake_tail_position[1]] != EMPTY \
            or field[snake_head_position[0] - 1][snake_head_position[1]] != EMPTY \
            or field[snake_head_position[0] + 1][snake_head_position[1]] != EMPTY \
            or field[snake_head_position[0]][snake_head_position[1]-1]!= EMPTY \
            or field[snake_tail_position[0]][snake_tail_position[1]+1]!= EMPTY:
        snake_head_position = [random.randint(1, field_size[0]-2), random.randint(1, field_size[1] - 3)]
        snake_tail_position = [snake_head_position[0], snake_head_position[1] + 1]
    snakes_coord.append([snake_tail_position, snake_head_position])
    create_snake_head(snake_head_position[0],snake_head_position[1], id)
    create_snake_segment(snake_tail_position[0], snake_tail_position[1], id)

def create_random_apple():
    global field_size
    apple_position = [random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1)]
    place_iterator = 1
    while field[apple_position[0]][apple_position[1]] != EMPTY:
        apple_position[1] = (apple_position[1]+place_iterator) % field_size[1]
        if place_iterator == field_size[1]:
            place_iterator = 0
            apple_position[0] = (apple_position[0] + 1) % field_size[0]
    create_apple(apple_position[0],apple_position[1])

def destroy_snake(id):
    for coord in snakes_coord[id]:
        draw_empty(coord[0], coord[1])
        create_apple(coord[0], coord[1])

def move_snake(id, move_coord):
    if field[move_coord[0]][move_coord[1]] != APPLE:
        # delete tail
        tail_coord = snakes_coord[id].pop(0)
        field[tail_coord[0]][tail_coord[1]] = EMPTY
        draw_empty(tail_coord[0], tail_coord[1])
    else:
        create_random_apple()

    # head movement
    old_head_coord = [snakes_coord[id][-1][0], snakes_coord[id][-1][1]]
    draw_snake_segment(old_head_coord[0], old_head_coord[1])
    create_snake_head(move_coord[0], move_coord[1], id)
    snakes_coord[id].append(move_coord)



def get_cell_content(x,y):
    return field[x][y]


