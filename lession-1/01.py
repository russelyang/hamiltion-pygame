import pygame

# initilize the game
pygame.init()

# define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# set display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("hello world")

# fill with black
display_surface.fill((0, 0, 0))

# boolean, a built in call bool
# main game loop
running = True  # False

while running:
    for event in pygame.event.get():
        # print(event)
        if bool(event.type == pygame.QUIT):
            running = False
    pygame.display.flip()

# clean up and quit
pygame.quit()
