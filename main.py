import pygame
import random
import game_field
import Snake

WIDTH = 1200
HEIGHT = 600
FPS = 2
SNAKES_NUMBER = 30
APPLES_NUMBER = 40





pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Еvolution of snakes")
clock = pygame.time.Clock()


# draw field
game_field.init_game_field(WIDTH, HEIGHT, screen)


snake_list = []
for i in range(1):
    snake = Snake.Snake()
    snake_list.append(snake)

for i in range(APPLES_NUMBER):
    game_field.create_random_apple()





running = True
while running:
    pygame.display.flip()

    head_coord = game_field.snakes_coord[0][-1]
    game_field.move_snake(0,[head_coord[0],head_coord[1]-1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)


pygame.quit()