import pygame,sys

pygame.init()

screen = pygame.display.set_mode((1280, 720))
box = pygame.Rect(10, 50, 50, 50)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    # Checking Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        box.x += 1
    if keys[pygame.K_LEFT]:
        box.x -= 1
    if keys[pygame.K_UP]:
        box.y -= 1
    if keys[pygame.K_DOWN]:
        box.y += 1


    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 150, 255), box)
    pygame.display.flip()
