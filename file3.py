import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("background.jpg")
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(bg_surface, (0,0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()