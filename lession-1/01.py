import pygame

# initilize the game
pygame.init()

# define constants
WINDOW_WIDTH=600
WINDOW_HEIGHT=300

# set display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('hello world')
display_surface.fill((255,0,0), (0,0,200,200))

# main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# clean up and quit
pygame.quit()