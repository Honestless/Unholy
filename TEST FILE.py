import pygame


screen = pygame.display.set_mode((800, 600))
bla = pygame.Rect(50, 50, 50, 50)
running = True
while running:
    screen.fill((255, 255, 255))
    for square in range(10, 20):
        pygame.draw.rect(screen, (100, 220, 157), bla, 0)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()