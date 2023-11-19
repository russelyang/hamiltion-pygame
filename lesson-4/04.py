import pygame

pygame.init()

# define game windows width hight
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ball = pygame.image.load("ball.png").convert_alpha()
ball = pygame.transform.scale(ball, [48, 48])
ball_rect = ball.get_rect()
ball_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
speed = [2, 2]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    ball_rect = ball_rect.move(speed)
    screen.blit(ball, ball_rect)
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        speed[1] = -speed[1]

    pygame.display.update()
    clock.tick(60)
pygame.quit()
