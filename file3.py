import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("background.jpg")
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

ship_width, ship_height = 150,100
ship_surface = pygame.image.load('ship3.png').convert_alpha()
ship_surface = pygame.transform.scale(ship_surface, (ship_width, ship_height))
ship_x = WIDTH//2
ship_y = HEIGHT
ship_rect = ship_surface.get_rect(midbottom=(ship_x, ship_y))
ship_speed = 20

bullets = []
bullet_size = 10

meteor_surface = pygame.image.load('meteor2.png').convert_alpha()
meteor_surface = pygame.transform.scale(meteor_surface, (50, 50))

meteors = []

score = 0

shooting_sound = pygame.mixer.Sound('shot-sound.wav')
hit_sound = pygame.mixer.Sound('explosion-sound.wav')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_rect.centerx, ship_rect.centery, bullet_size, bullet_size)
                bullets.append(bullet)

    if random.randint(1,30) == 1:
        x = random.randint(0, WIDTH-50)
        y = -50
        meteor_rect = meteor_surface.get_rect(midbottom=(x, y))
        meteors.append(meteor_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship_rect.x += ship_speed
    if ship_rect.x < 0:
        ship_rect.x = 0
    if ship_rect.x > WIDTH-ship_width:
        ship_rect.x = WIDTH-ship_width

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for meteor in meteors[:]:
        meteor.y += 4
        if meteor.y > HEIGHT:
            meteors.remove(meteor)

        for bullet in bullets[:]:
            if bullet.colliderect(meteor):
                bullets.remove(bullet)
                meteors.remove(meteor)
                score += 1
                break


    screen.blit(bg_surface, (0,0))
    screen.blit(ship_surface, ship_rect)
    for bullet in bullets[:]:
        pygame.draw.rect(screen, (255,255,0), bullet)
    for meteor in meteors[:]:
        screen.blit(meteor_surface, meteor)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()