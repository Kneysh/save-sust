import pygame
import time
from random import randint
from screens.menu import Start_Menu, Pause_Menu, Game_Over_Menu
from utils.functions import load_image, text_object
from utils import colors


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("sust.png")
        self.rect = self.image.get_rect(midbottom=(400,590))
        self.mask = pygame.mask.from_surface(self.image)
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

        self.mask = pygame.mask.from_surface(self.image)


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

        # music and sfx
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bgm.mp3")
        self.crashSound = pygame.mixer.Sound("assets/sounds/crash.wav")

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

        self.gameOver = True

    def display_score(self):
        self.score += (1 / 60)
        scoreSurf, scoreRect = text_object("Score: " + str(int(self.score)), "Orbitron", 20, colors.textColor)
        scoreRect.topleft = (10, 5)

        self.screen.blit(scoreSurf, scoreRect)

    def spawn_obstacles(self):
        for obs in ["missile", "missile", "bomb", "missile"]:
            self.obstacleGroup.add(Obstacles(obs))

    def collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacleGroup, True, pygame.sprite.collide_mask):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.crashSound)
            time.sleep(1)
            self.obstacleGroup.empty()
            return True
        return False

    def quit_game(self):
        pygame.quit()
        quit()

    def reset(self):
        self.obstacleGroup.empty()
        self.spawn_obstacles()
        self.score = 0
        self.backgroundY = self.displayHeight - 1536
        self.player.empty()
        self.player.add(Player())

    def menu_screen(self, name):
        self.screen.blit(self.background, (0, 0))
        while True:
            if name == "start":
                menu = Start_Menu()
            elif name == "over":
                menu = Game_Over_Menu()
                menu.final_score(str(int(self.score)), self.screen)
            menu.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_p and name == "start") or (event.key == pygame.K_r and name == "over"):
                        self.reset()
                        return False
                    if event.key == pygame.K_q:
                        self.quit_game()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if name == "start" and menu.playBtn.inButton():
                        return False
                    elif name == "over" and menu.restartBtn.inButton():
                        self.reset()
                        return False
                    if menu.quitBtn.inButton():
                        self.quit_game()
            
            pygame.display.update()
            self.clock.tick(15)

    def pause(self):
        pygame.mixer.music.pause()

        while True:
            menu = Pause_Menu()
            menu.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_c:
                        pygame.mixer.music.unpause()
                        return
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.continueBtn.inButton():
                        pygame.mixer.music.unpause()
                        return
                    if menu.quitBtn.inButton():
                        self.quit_game()

            pygame.display.update()
            self.clock.tick(15)


    def run(self):
        # start screen
        self.gameOver = self.menu_screen(name="start")
        pygame.mixer.music.play(-1)

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                        self.pause()

            # moving background
            self.backgroundRect = self.background.get_rect(topleft = (0, self.backgroundY))
            self.screen.blit(self.background, self.backgroundRect)
            self.backgroundY += self.backgroundMove

            if self.backgroundY > 0:
                self.backgroundY = self.displayHeight - 1536



            # player
            self.player.draw(self.screen)
            self.player.update()

            # obstacles
            self.obstacleGroup.draw(self.screen)
            self.obstacleGroup.update()

            # check collision
            if self.collision():
                # game-over screen
                self.gameOver = self.menu_screen(name="over")
                pygame.mixer.music.play(-1)


            # score-card
            self.display_score()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game().run()
