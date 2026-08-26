import pygame
import random
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

fruit1_surface = pygame.image.load('fruit1.png').convert_alpha()
fruit1_surface = pygame.transform.scale(fruit1_surface, (50, 50))

fruits = []
spawn_timer = 0

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_rect.x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_rect.x += basket_speed

    if basket_rect.x < 0:
        basket_rect.x = 0
    if basket_rect.x > WIDTH-basket_width:
        basket_rect.x = WIDTH-basket_width

    if spawn_timer <= 0:
        spawn_timer = random.randint(20, 100)
    spawn_timer -= 1
    if spawn_timer <= 0:
        x = random.randint(0, WIDTH-50)
        y = -50
        fruit_rect = fruit1_surface.get_rect(topleft = (x,y))
        fruits.append(fruit_rect)

    for fruit in fruits[:]:
        fruit.y += 5
        if fruit.top > HEIGHT:
            fruits.remove(fruit)
        if basket_rect.colliderect(fruit):
            fruits.remove(fruit)
            score += 1

    screen.blit(bg_surface, (0,0))
    screen.blit(basket_surface, basket_rect)
    for fruit in fruits[:]:
        screen.blit(fruit1_surface, fruit)
    score_font = pygame.font.SysFont('Arial', 36)
    score_text = score_font.render("score:"+ str(score), True, (255,0,0))
    screen.blit(score_text, (20,20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
