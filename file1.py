import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping game")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("BG.png")
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

player_surface = pygame.image.load("girl3.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface, (50, 100))
player_speed = 20
player_start_x = WIDTH // 2 - 25
player_start_y = HEIGHT - 100
player_rect = player_surface.get_rect(topleft = (player_start_x, player_start_y))

gravity = 1
jump_power = -30
velocity_y = 0
on_ground = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_power
                on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > WIDTH-50:
        player_rect.x = WIDTH - 50

    velocity_y += gravity
    player_rect.y += velocity_y

    if player_rect.y >= HEIGHT - 100:
        player_rect.y = HEIGHT - 100
        velocity_y = 0
        on_ground = True

    screen.blit(bg_surface, (0,0))
    screen.blit(player_surface, player_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()