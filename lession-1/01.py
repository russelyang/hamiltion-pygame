import pygame

# initilize the game
pygame.init()

# define constants
WINDOW_WIDTH = 600  # constant
WINDOW_HEIGHT = 300

RED = (255, 0, 0)


# RGB A
# set display surface
display_surface = pygame.display.set_mode((600, 300))
pygame.display.set_caption("hello world")
display_surface.fill(RED, (0, 0, 200, 200))

# boolean, a built in call bool
# main game loop
running = True  # False

while running:
    for event in pygame.event.get():
        print(event)
        if bool(event.type == pygame.QUIT):
            running = False
    pygame.display.flip()

# clean up and quit
pygame.quit()
