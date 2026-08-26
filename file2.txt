import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruits Catcher")
clock = pygame.time.Clock()

bg_surface = pygame.image.load('BG.png')
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

basket_width = 150
basket_height = 50
basket_surface =pygame.image.load('basket3.png').convert_alpha()
basket_surface = pygame.transform.scale(basket_surface, (basket_width,basket_height))
basket_speed = 20
basket_x = WIDTH//2
basket_y = HEIGHT
basket_rect = basket_surface.get_rect(midbottom= (basket_x,basket_y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_surface, (0,0))
    screen.blit(basket_surface, basket_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
