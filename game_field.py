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
FIELD_WIDTH = 0
FIELD_HEIGHT = 0




SNAKE_COLORS = ["#48D1CC", "#0000FF", "#32CD32", "#00FF00", "#66CDAA", "#FF0000", "#008000", "#FFD700", "#1E90FF", "#FF00FF",
                "#D2691E", "#FF0000", "#00FFFF", "#FFBF00", "#BDB76B", "#ED4830", "#1FAEE9", "#FFA474", "#8B00FF", "#800000",
                "#9370D8", "#8E4585", "#FC2847", "#FF6E4A", "#E97451", "#2F4F4F", "#DA70D6", "#4682B4", "#808000", "#66CDAA"]



def init_game_field(WIDTH, HEIGHT, screen_init):
    global screen, FIELD_WIDTH, FIELD_HEIGHT
    screen = screen_init
    FIELD_WIDTH = WIDTH
    FIELD_HEIGHT = HEIGHT

    #draw field
    SAND = ('#F0FF00')
    ORANGE = ('#b7410e')

    # прорисовка игрового поля (прямоугольника)
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, ORANGE, (20, 20), (20, HEIGHT - 20), 4)
    pygame.draw.line(screen, ORANGE, (20, 20), (WIDTH - 420, 20), 4)
    pygame.draw.line(screen, ORANGE, (WIDTH - 420, 20), (WIDTH - 420, HEIGHT - 20), 4)
    pygame.draw.line(screen, ORANGE, (20, HEIGHT - 20), (WIDTH - 420, HEIGHT - 20), 4)

    # прорисовка игрового поля (координатной сетки)
    global field_size_y, field_size_x
    field_size_y = 1
    field_size_x = 1
    for i in range(40, HEIGHT - 20, 20):
        pygame.draw.line(screen, ORANGE, (20, i), (WIDTH - 420, i), 1)
        field_size_x += 1
    for i in range(40, WIDTH - 420, 20):
        pygame.draw.line(screen, ORANGE, (i, 20), (i, HEIGHT - 20), 1)
        field_size_y += 1

    field_size.append(field_size_x)
    field_size.append(field_size_y)

    # прорисовка прямоугольника для счета
    clear_score()

    # инициация матрицы поля
    for i in range(field_size_x):
        list_y = [EMPTY for i in range(0, field_size_y)]
        field.append(list_y)


def clear_score():
    pygame.draw.rect(screen, '#FFF3F1', (FIELD_WIDTH - 420, 19, 400, FIELD_HEIGHT - 36))
    pygame.draw.rect(screen, '#b7410e', (FIELD_WIDTH -420, 19, 400, FIELD_HEIGHT - 36), 4)

def draw_apple(x,y):
    global screen
    pygame.draw.circle(screen, '#f80000', (30+y*20, 30+x*20), 7)

def create_apple(x,y):
    draw_apple(x, y)
    field[x][y] = APPLE

def draw_snake_segment(x,y, id):
    global screen
    pygame.draw.rect(screen, SNAKE_COLORS[id], (23+y*20, 23+x*20, 15, 15))

def create_snake_segment(x,y, id):
    draw_snake_segment(x,y, id)
    field[x][y] = id

def draw_snake_head(x,y, id):
    global screen
    pygame.draw.rect(screen, SNAKE_COLORS[id], (23+y*20, 23+x*20, 15, 15))

def create_snake_head(x,y, id):
    draw_snake_head(x,y, id)
    field[x][y] = id

def draw_empty(x,y):
    global screen
    pygame.draw.rect(screen, '#ffffff', (23+y*20, 23+x*20, 15, 15))


def create_snake(id):
    # random.seed(421)
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
    draw_snake_segment(old_head_coord[0], old_head_coord[1], id)
    create_snake_head(move_coord[0], move_coord[1], id)
    snakes_coord[id].append(move_coord)



def get_cell_content(x,y):
    return field[x][y]

def refsresh_field ():
    for x in range(field_size[0]):
        for y in range(field_size[1]):
            field[x][y] = 100
            draw_empty(x,y)
            snakes_coord.clear()


def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_score(snake_list, snake_names, generation):
    clear_score()

    snake_list.sort(key=lambda snake: snake.weight, reverse=True)
    draw_text(screen, 'Поколение: ' + str(generation), 32, FIELD_WIDTH -220, 30, '#000000')
    i = 0
    for snake in snake_list:
        draw_text(screen, snake_names[snake.snake_id] + ": " + str(snake.weight), 22, FIELD_WIDTH - 220, 70 + i, SNAKE_COLORS[snake.snake_id])
        i+=26


