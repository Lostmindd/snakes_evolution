import pygame

field = []
screen = None



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

    field_size_y = 0
    field_size_x = 0
    for i in range(40, HEIGHT - 20, 20):
        pygame.draw.line(screen, SAND, (20, i), (WIDTH - 20, i), 1)
        field_size_y += 1
    for i in range(40, WIDTH - 20, 20):
        pygame.draw.line(screen, SAND, (i, 20), (i, HEIGHT - 20), 1)
        field_size_x += 1

    #init field matrix
    for i in range(field_size_y):
        list_x = [0 for i in range(0, field_size_x)]
        field.append(list_x)

def draw_apple(x,y):
    global screen
    pygame.draw.circle(screen, '#f80000', (30+x*20, 30+y*20), 7)

def draw_snake_segment(x,y):
    global screen
    pygame.draw.rect(screen, '#00e600', (23+x*20, 23+y*20, 15, 15))
