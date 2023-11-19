import pygame

pygame.init()

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 480

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball = pygame.image.load("lesson-4/ball.png")
ball_rect = ball.get_rect()
print(ball_rect)
ball = pygame.transform.scale(ball, [32, 32])
ball_rect = ball.get_rect()
ball_rect.topleft = (0, 0)


# sound = pygame.mixer.Sound("lesson-4/sound.wav")
# sound.play(-1)

speed = [1, 1]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if ball_rect.right > WINDOW_WIDTH or ball_rect.left < 0:
        speed[0] = -speed[0]
    if ball_rect.bottom > WINDOW_HEIGHT or ball_rect.top < 0:
        speed[1] = -speed[1]
    ball_rect = ball_rect.move(speed)
    screen.blit(ball, ball_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
