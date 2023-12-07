import pygame

pygame.init()

WINDOWN_WIDTH, WINDOW_HEIGHT = 800, 600

screen = pygame.display.set_mode((WINDOWN_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("my pong game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 0))
    pygame.display.update()
pygame.quit()
