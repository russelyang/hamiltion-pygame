import pygame
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))

waypoints = [(100, 100), (400, 200), (400, 100), (200, 300), (0, 0)]

dot = pygame.Surface((32, 32), pygame.SRCALPHA)
dot.fill(pygame.Color("green"))
dot_rect = dot.get_rect()

orignal_dot = dot

dot_pos = pygame.Vector2(waypoints[0])
dot_rect.center = dot_pos
dot_speed = 1

waypoint_index = 1
target = pygame.Vector2(waypoints[waypoint_index])
clock = pygame.time.Clock()


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 0, 0), False, waypoints)
    movement = target - dot_rect.center

    angle = math.degrees(math.atan2(-movement[1], movement[0]))

    dot, dot_rect = rot_center(orignal_dot, angle, dot_pos.x, dot_pos.y)

    dist = movement.length()

    if dist >= dot_speed:
        dot_pos += movement.normalize() * dot_speed
    else:
        if waypoint_index < len(waypoints) - 1:
            waypoint_index += 1
            target = pygame.Vector2(waypoints[waypoint_index])
        if dist != 0:
            dot_pos += movement.normalize() * dist
    dot_rect.center = dot_pos

    screen.blit(dot, dot_rect)
    pygame.display.update()

pygame.quit()
