import pygame
import time
from random import randint, choice
from utils.menu import Start_Menu, Pause_Menu, Game_Over_Menu
from utils.functions import load_image, text_object
from utils.highest_time import Highest_Time
from utils import colors


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, displayWidth, displayHeight):
        super().__init__()
        self.displayWidth, self.displayHeight = displayWidth, displayHeight

        self.image = load_image("sust.png")
        self.initPos = ((self.displayWidth / 2), (self.displayHeight - 50))
        self.rect = self.image.get_rect(midbottom=self.initPos)
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

        if keys[pygame.K_RIGHT] and self.rect.right <= self.displayWidth:
            self.x_change = (self.playerSpeed)
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.x_change = 0 - (self.playerSpeed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= self.displayHeight:
            self.y_change = (self.playerSpeed)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.y_change = 0 - (self.playerSpeed)
    
    def move(self):
        self.rect.left += self.x_change
        self.rect.top += self.y_change

        if self.rect.bottom >= self.displayHeight - 35:
            self.rect.bottom = self.displayHeight - 35
        if self.rect.right >= self.displayWidth:
            self.rect.right = self.displayWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.left <= 0:
            self.rect.left = 0
    
    def update(self):
        self.instructions()
        self.move()


# obstacles class
class Obstacles(pygame.sprite.Sprite):
    def __init__(self, obs:str, displayWidth:int, displayHeight:int):
        super().__init__()
        self.displayWidth, self.displayHeight = displayWidth, displayHeight
        self.rangeX = (50, (displayWidth - 50)) 
        
        if obs == "missile":
            self.image = load_image("missile.png")
            self.top = 0 - (randint(400, 600))
            self.rect = self.image.get_rect(midtop=(randint(*self.rangeX), self.top))
            self.speed = randint(5, 9)
        elif obs == "bomb":
            self.image = load_image("bomb.png")
            self.top = -500
            self.rect = self.image.get_rect(midtop=(randint(*self.rangeX), self.top))
            self.speed = 9

        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect.top += self.speed
        if self.rect.top > self.displayHeight:
            self.rect.midbottom = (randint(*self.rangeX), -10)


# prizes class
class Prizes(pygame.sprite.Sprite):
    def __init__(self, prize:str, displayWidth:int, displayHeight:int):
        super().__init__()
        self.displayWidth, self.displayHeight = displayWidth, displayHeight
        self.rangeX = (50, (displayWidth - 50))
        self.speed = 5

        if prize == "money":
            self.image = load_image("money.png")
        elif prize == "goldCoin":
            self.image = load_image("gold_coin.png")
        elif prize == "silverCoin":
            self.image = load_image("silver_coin.png")
        
        self.rect = self.image.get_rect(midtop=(randint(*self.rangeX), -300))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > self.displayHeight:
            self.kill()



# main game
class Game():
    def __init__(self):
        pygame.init()

        # display
        self.displayWidth = 800
        self.displayHeight = 800
        
        pygame.display.set_caption("Save Sust")
        self.screen = pygame.display.set_mode((self.displayWidth, self.displayHeight))

        self.icon = load_image("icon.png")
        pygame.display.set_icon(self.icon)

        # music and sfx
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bgm.mp3")
        self.crashSound = pygame.mixer.Sound("assets/sounds/crash.wav")
        self.collectCoins = pygame.mixer.Sound("assets/sounds/collect_points.mp3")

        # frame-per-second
        self.clock = pygame.time.Clock()

        # background image
        self.background = load_image("background.png")
        # self.backgroundRect = self.background.get_rect()
        self.backgroundMove = 3
        self.backgroundHeight = 1536
        self.backgroundY = self.displayHeight - self.backgroundHeight


        # groups
        self.prizeGroup = pygame.sprite.Group()

        self.obstacleGroup = pygame.sprite.Group()
        self.spawn_obstacles()

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.displayWidth, self.displayHeight))

        self.x_change = 0
        self.y_change = 0
        self.playerSpeed = 5

        # timer
        self.prizeTimer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.prizeTimer, 5000)

        # scores
        self.highestTime = Highest_Time().load_highest()
        self.totalTime = 0

        self.gameOver = True

    def display_score(self):
        self.totalTime += (1 / 60)
        scoreSurf, scoreRect = text_object(f"Survived: {int(self.totalTime)} s", "Orbitron", 20, colors.textColor)
        # scoreRect.topleft = (10, 5)
        scoreRect.bottomleft = (10, (self.displayHeight - 5))

        scoreBoxHeight = 35
        scoreBox = pygame.Rect(0, (self.displayHeight -scoreBoxHeight), self.displayWidth, scoreBoxHeight)
        pygame.draw.rect(self.screen, colors.baseColor, scoreBox)

        self.screen.blit(scoreSurf, scoreRect)

    def spawn_obstacles(self):
        for obs in ["missile", "missile", "bomb", "missile"]:
            self.obstacleGroup.add(Obstacles(obs, self.displayWidth, self.displayHeight))

    def collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacleGroup, True, pygame.sprite.collide_mask):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.crashSound)
            time.sleep(1)
            self.obstacleGroup.empty()
            self.prizeGroup.empty()
            return True
        return False
    
    def collection(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.prizeGroup, True, pygame.sprite.collide_mask):
            pygame.mixer.Sound.play(self.collectCoins)
            return True
        return False

    def quit_game(self):
        pygame.quit()
        quit()

    def reset(self):
        self.obstacleGroup.empty()
        self.spawn_obstacles()
        self.totalTime = 0
        self.backgroundY = self.displayHeight - self.backgroundHeight
        self.player.empty()
        self.player.add(Player(self.displayWidth, self.displayHeight))

    def menu_screen(self, name):
        self.screen.blit(self.background, (0, 0))
        while True:
            if name == "start":
                menu = Start_Menu()
            elif name == "over":
                menu = Game_Over_Menu()
                if self.totalTime > self.highestTime:
                    self.highestTime = int(self.totalTime)
                    Highest_Time().save_highest(self.highestTime)
                menu.final_time(str(int(self.totalTime)), str(self.highestTime), self.screen)
            menu.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_s and name == "start") or (event.key == pygame.K_r and name == "over"):
                        self.reset()
                        return False
                    if event.key == pygame.K_l:
                        self.quit_game()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.btnOne.in_button():
                        self.reset()
                        return False
                    if menu.btnTwo.in_button():
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
                    if event.key == pygame.K_SPACE or event.key == pygame.K_k:
                        pygame.mixer.music.unpause()
                        return
                    if event.key == pygame.K_l:
                        self.quit_game()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.btnOne.in_button():
                        pygame.mixer.music.unpause()
                        return
                    if menu.btnTwo.in_button():
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
                    if event.key == pygame.K_SPACE or event.key == pygame.K_k:
                        self.pause()

                if event.type == self.prizeTimer:
                    self.prizeGroup.add(Prizes(choice(["silverCoin", "goldCoin", "money", "goldCoin", "silverCoin"]), self.displayWidth, self.displayHeight))

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

            # prizes
            self.prizeGroup.draw(self.screen)
            self.prizeGroup.update()

            self.collection()

            # score-card
            self.display_score()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game().run()

