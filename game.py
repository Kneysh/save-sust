import pygame
import time
from random import randint, randrange, choice
from screens import start, pause, over
from utils.functions import load_image, text_object
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
    def __init__(self, obs:str):
        super().__init__()
        
        if obs == "missile":
            self.image = load_image("missile.png")
            self.top = -(randint(400, 600))
            self.rect = self.image.get_rect(midtop=(randint(50, 750), self.top))
            self.speed = randint(5, 9)
        elif obs == "bomb":
            self.image = load_image("bomb.png")
            self.top = -500
            self.rect = self.image.get_rect(midtop=(randint(50, 750), self.top))
            self.speed = 9


    def update(self):
        self.rect.top += self.speed
        if self.rect.top > 600:
            self.rect.midbottom = (randint(50, 750), -10)



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
        self.obstacleGroup = pygame.sprite.Group()
        self.spawn_obstacles()

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        self.x_change = 0
        self.y_change = 0
        self.playerSpeed = 5

        self.score = 0

        self.gameOver = False

    def game_over(self):
        pass

    def display_score(self):
        scoreSurf, scoreRect = text_object("Score: " + str(int(self.score)), "Orbitron", 20, colors.textColor)
        scoreRect.topleft = (10, 10)

        self.screen.blit(scoreSurf, scoreRect)

    def calc_score(self):
        pass

    def spawn_obstacles(self):
        for obs in ["missile", "missile", "bomb", "missile"]:
            self.obstacleGroup.add(Obstacles(obs))

    def collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacleGroup, True):
            self.obstacleGroup.empty()
            return True
        return False
        

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

            # check collision
            self.gameOver = self.collision()

            # obstacles
            self.obstacleGroup.draw(self.screen)
            self.obstacleGroup.update()


            # score-card
            self.display_score()

            self.score += (1 / 60)
            pygame.display.update()
            self.clock.tick(60)

        # return
        # pygame.quit()
        # quit()


if __name__ == "__main__":
    Game().run()