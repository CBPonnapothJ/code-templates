import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooting game")
clock = pygame.time.Clock()

bg = pygame.image.load("background.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()