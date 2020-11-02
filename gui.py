import pygame

screen = pygame.display.set_mode([1920,1080])
screen.fill([255, 255, 255])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()