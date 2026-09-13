import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fruit_radius = 50
fruit_x = random.randint(0, WIDTH - fruit_radius)
fruit_y = -15
fruit_speed = 5
fruit_color = (255, 0, 0)

basket_width = 100
basket_height = 50
basket_x = WIDTH//2-basket_width//2
basket_y = HEIGHT-basket_height
basket_color = (0, 255, 255)
basket = pygame.Rect(basket_x,basket_y, basket_width, basket_height)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fruit_y += fruit_speed
    if fruit_y > HEIGHT:
        fruit_y = random.randint(-300,-20)
        fruit_x = random.randint(0, WIDTH - fruit_radius)

    screen.fill((255,255,255))
    pygame.draw.circle(screen,fruit_color,(fruit_x,fruit_y), fruit_radius)
    pygame.draw.rect(screen,basket_color,basket)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()