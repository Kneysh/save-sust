import pygame

pygame.init()

# display
pygame.display.set_caption("Save Sust")
screen = pygame.display.set_mode((800, 600))

# frame-per-second
clock = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


