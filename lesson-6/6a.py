import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()


running = True
VOL = 1
RADIUS = 20
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    player = pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS)

    user_inputs = pygame.key.get_pressed()
    if user_inputs[pygame.K_UP] and y - RADIUS - 2 > 0:
        y -= VOL
    if user_inputs[pygame.K_DOWN] and y + RADIUS < WINDOW_HEIGHT:
        y += VOL
    if user_inputs[pygame.K_LEFT] and x - RADIUS > 0:
        x -= VOL
    if user_inputs[pygame.K_RIGHT] and x + RADIUS < WINDOW_WIDTH:
        x += VOL

    pygame.display.update()
    clock.tick(60)

pygame.quit()
