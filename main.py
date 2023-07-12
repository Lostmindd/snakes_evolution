import pygame
import random
import game_field


WIDTH = 1200
HEIGHT = 600
FPS = 30


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Еvolution of snakes")
clock = pygame.time.Clock()


# draw field
game_field.init_game_field(WIDTH, HEIGHT, screen)
game_field.draw_snake_segment(1,3)





running = True
while running:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)


pygame.quit()