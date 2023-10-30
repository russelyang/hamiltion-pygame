# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()

backdrop = pygame.transform.scale(
    pygame.image.load(os.path.join("lesson-3", "Boardwalk.png")).convert(), ((960, 720))
)
backdrop_rect = backdrop.get_rect()
backdrop_rect.center = (480, 360)

running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() / 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    screen.blit(backdrop, backdrop_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
