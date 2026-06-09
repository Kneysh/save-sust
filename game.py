import pygame
import time
from random import randint, randrange, choice
from screens import start, pause, over
from utils.functions import load_image
from utils import colors


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("sust.png")



# obstacles class
class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()




# main game
class Game():
    def __init__(self):
        pygame.init()

        # display
        pygame.display.set_caption("Save Sust")
        self.screen = pygame.display.set_mode((800, 600))

        # frame-per-second
        self.clock = pygame.time.Clock()

        self.gameOver = False

    def run(self):

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

            self.screen.fill("White")
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()


if __name__ == "__main__":
    Game().run()