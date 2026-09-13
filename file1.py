import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

stars = []

for i in range(100):
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    stars.append((x,y))

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    for star in stars:
        pygame.draw.circle(screen, (255,255,255), (star[0], star[1]), 10)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()