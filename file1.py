import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooting game")
clock = pygame.time.Clock()

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

rocket = pygame.image.load("ship3.png").convert_alpha()
rocket = pygame.transform.scale(rocket, (80, 60))
rocket_rect = rocket.get_rect(center=(WIDTH//2-40, HEIGHT - 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()