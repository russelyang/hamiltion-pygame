import pygame
import random

pygame.init()

# define game windows width hight
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = pygame.image.load("lesson-6/boardwalk.png").convert_alpha()

ball = pygame.image.load("lesson-6/ball.png").convert_alpha()
ball = pygame.transform.scale(ball, [48, 48])
ball_rect = ball.get_rect()
ball_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
speed = [5, 5]

# paddle
paddle = pygame.Surface((100, 15))
paddle.fill(GREEN)
paddle_rect = paddle.get_rect()
PADDLE_HIGHT = WINDOW_HEIGHT - 50
paddle_rect.center = (WINDOW_WIDTH // 2, PADDLE_HIGHT)
pygame.mouse.set_visible(False)

score = 0
print(pygame.font.get_fonts())
font = pygame.font.SysFont("kefa", 24)

clock = pygame.time.Clock()
last_colide = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # background
    screen.blit(bg, (0, 0))
    # ball
    ball_rect = ball_rect.move(speed)
    screen.blit(ball, ball_rect)
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        speed[1] = -speed[1]

    # score
    score_str = font.render("score: " + str(score), True, (255, 0, 0))
    score_str_rect = score_str.get_rect()
    screen.blit(score_str, score_str_rect)

    # padding
    mouse_pos = pygame.mouse.get_pos()
    paddle_rect.center = (mouse_pos[0], PADDLE_HIGHT)
    if paddle_rect.left < 0:
        paddle_rect.left = 0
    if paddle_rect.right > WINDOW_WIDTH:
        paddle_rect.right = WINDOW_WIDTH

    # detect colide
    if (
        paddle_rect.colliderect(ball_rect)
        and pygame.time.get_ticks() - last_colide > 150
    ):
        speed[0] = random.choice([1, -1]) * speed[0]
        speed[1] = -speed[1]
        score += 1
        last_colide = pygame.time.get_ticks()
    screen.blit(paddle, paddle_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
