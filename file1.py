import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooting game")
clock = pygame.time.Clock()

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

rocket_image = pygame.image.load("ship3.png").convert_alpha()
rocket_image = pygame.transform.scale(rocket_image, (80, 60))
rocket_rect = rocket_image.get_rect(center=(WIDTH//2-40, HEIGHT - 20))

meteor_images = [pygame.image.load("meteor2.png").convert_alpha(),
                 pygame.image.load("meteor3.png").convert_alpha(),
                 pygame.image.load("meteor4.png").convert_alpha()
                 ]
meteor_positions = []
total_meteors = 10
for i in range(total_meteors):
    x = random.randint(0,2)
    meteor_rect = meteor_images[x].get_rect(topleft = (random.randint(0,WIDTH-50), random.randint(-300,-50)))
    speed = random.randint(3,5)
    meteor_positions.append([x,meteor_rect,speed])

shooting_sound = pygame.mixer.Sound("shot-sound.wav")
explore_sound = pygame.mixer.Sound("explosion-sound.wav")

bullets = []
font = pygame.font.Font(None, 48)
game_over = True
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(rocket_rect.centerx, rocket_rect.centery, 5, 10)
                bullets.append(bullet_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket_rect.x -= 10
    if keys[pygame.K_RIGHT]:
        rocket_rect.x += 10
    if rocket_rect.x < 0:
        rocket_rect.x = 0
    if rocket_rect.x > WIDTH-80:
        rocket_rect.x = WIDTH-80

    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for meteor in meteor_positions:
        meteor[1].y += meteor[2]
        if meteor[1].y > HEIGHT:
            meteor[1].x = random.randint(0,WIDTH-50)
            meteor[1].y = random.randint(-300,-50)
        for bullet in bullets:
            if meteor[1].colliderect(bullet):
                bullets.remove(bullet)
                meteor[1].x = random.randint(0, WIDTH - 50)
                meteor[1].y = random.randint(-300, -50)
                score += 1


    screen.blit(bg, (0,0))
    screen.blit(rocket_image, rocket_rect)
    for meteor in meteor_positions:
        screen.blit(meteor_images[meteor[0]], meteor[1])
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 255, 0), bullet)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()