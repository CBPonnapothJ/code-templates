import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooting game")

clock = pygame.time.Clock()

bg = pygame.image.load("background (1).jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

rocket_image = pygame.image.load("ship3 (3).png").convert_alpha()
rocket_image = pygame.transform.scale(rocket_image, (60, 40))
rocket_rect = rocket_image.get_rect(center=(WIDTH // 2, HEIGHT - 20))

meteor_image = pygame.image.load("meteor4 (2).png").convert_alpha()
meteor_image = pygame.transform.scale(meteor_image, (40, 40))

shooting_sound = pygame.mixer.Sound("shot-sound (3).wav")
hit_sound = pygame.mixer.Sound("explosion-sound (3).wav")

bullets = []
meteors = []

score = 0
font = pygame.font.Font(None, 48)
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(rocket_rect.centerx, rocket_rect.centery, 10, 20)
                bullets.append(bullet)

    if not game_over and random.randint(1, 30) == 1:
        x = random.randint(0, WIDTH - 20)
        meteor_rect = meteor_image.get_rect(topleft=(x, -50))
        meteors.append(meteor_rect)

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            rocket_rect.centerx -= 7
        if keys[pygame.K_RIGHT]:
            rocket_rect.centerx += 7
        if rocket_rect.left < 0:
            rocket_rect.left = 0
        if rocket_rect.right > WIDTH:
            rocket_rect.right = WIDTH

    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for meteor in meteors[:]:
        meteor.y += 4
        if meteor.y > HEIGHT:
            meteors.remove(meteor)

        if rocket_rect.colliderect(meteor):
            game_over = True

        for bullet in bullets[:]:
            if bullet.colliderect(meteor):
                bullets.remove(bullet)
                meteors.remove(meteor)
                score += 1
                break


    screen.blit(bg, (0, 0))
    screen.blit(rocket_image, rocket_rect)
    for meteor in meteors[:]:
        screen.blit(meteor_image, meteor)
    for bullet in bullets[:]:
        pygame.draw.rect(screen,(255,255,0), bullet)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()