import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((500, 500))

p1 = pygame.Vector2(100, 100)
p2 = pygame.Vector2(200, 300)

dist = p2 - p1
print(dist, dist.normalize(), 100 / dist.length(), 200 / dist.length())


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.line(screen, constants.RED, p1, p2)
    pygame.display.update()
pygame.quit()
