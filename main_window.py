import pygame
import random


WIDTH = 1200
HEIGHT = 600
FPS = 30
SAND = ('#F0FF00')
ORANGE = ('#b7410e')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Еvolution of snakes")
clock = pygame.time.Clock()

# init field
screen.fill((0, 0, 0))
pygame.draw.line(screen, ORANGE, (20, 20), (20, HEIGHT - 20), 4)
pygame.draw.line(screen, ORANGE, (20, 20), (WIDTH - 20, 20), 4)
pygame.draw.line(screen, ORANGE, (WIDTH - 20, 20), (WIDTH - 20, HEIGHT - 20), 4)
pygame.draw.line(screen, ORANGE, (20, HEIGHT - 20), (WIDTH - 20, HEIGHT - 20), 4)

for i in range(40,HEIGHT-20,20):
    pygame.draw.line(screen, SAND, (20, i), (WIDTH - 20, i), 1)
for i in range(40,WIDTH-20,20):
    pygame.draw.line(screen, SAND, (i, 20), (i, HEIGHT - 20), 1)


running = True
while running:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)


pygame.quit()