import pygame

pygame.init()

# define game windows width hight
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = pygame.image.load("lesson-5/Boardwalk.png").convert_alpha()

ball = pygame.image.load("lesson-5/ball.png").convert_alpha()
ball = pygame.transform.scale(ball, [48, 48])
ball_rect = ball.get_rect()
ball_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# paddle
paddle = pygame.Surface((100, 15))
paddle.fill((0, 255, 0))
paddle_rect = paddle.get_rect()
paddle_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)

speed = [2, 2]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    ball_rect = ball_rect.move(speed)
    screen.blit(ball, ball_rect)
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        speed[1] = -speed[1]

    # handle the movement
    mouse_x = pygame.mouse.get_pos()[0]
    if mouse_x - 40 > 0:
        paddle_rect.center = (mouse_x, WINDOW_HEIGHT - 50)

    # handle keyboard move padding
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_a]:
        paddle_rect.move_ip([-5, 0])
    screen.blit(paddle, paddle_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
