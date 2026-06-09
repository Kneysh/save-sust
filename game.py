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
        self.rect = self.image.get_rect(midbottom=(400,590))
        self.imageWidth = 100
        self.imageHeight = 100

        self.x_change = 0
        self.y_change = 0
        self.playerSpeed = 5
    
    def instructions(self):
        keys = pygame.key.get_pressed()
        self.x_change = 0
        self.y_change = 0

        if keys[pygame.K_RIGHT] and self.rect.right <= 800:
            self.x_change = (self.playerSpeed)
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.x_change = -(self.playerSpeed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= 600:
            self.y_change = (self.playerSpeed)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.y_change = -(self.playerSpeed)
    
    def move(self):
        self.rect.left += self.x_change
        self.rect.top += self.y_change

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.left <= 0:
            self.rect.left = 0
    
    def update(self):
        self.instructions()
        self.move()


# obstacles class
class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()




# main game
class Game():
    def __init__(self):
        pygame.init()

        # display
        self.displayWidth = 800
        self.displayHeight = 600

        pygame.display.set_caption("Save Sust")
        self.screen = pygame.display.set_mode((800, 600))

        # frame-per-second
        self.clock = pygame.time.Clock()

        # background image
        self.background = load_image("background.png")
        # self.backgroundRect = self.background.get_rect()
        self.backgroundMove = 3
        self.backgroundY = self.displayHeight - 1536


        # groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        self.x_change = 0
        self.y_change = 0
        self.playerSpeed = 5

        self.gameOver = False

    def run(self):

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

            # moving background
            self.backgroundRect = self.background.get_rect(topleft = (0, self.backgroundY))
            self.screen.blit(self.background, self.backgroundRect)
            self.backgroundY += self.backgroundMove

            if self.backgroundY > 0:
                self.backgroundY = self.displayHeight - 1536



            # player
            self.player.draw(self.screen)
            self.player.update()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()


if __name__ == "__main__":
    Game().run()