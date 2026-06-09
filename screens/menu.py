import pygame
from utils import colors
from utils.functions import text_object, draw_block
from utils.buttons import Button
from utils.title import Title


class Menu():
    def __init__(self, title):
        self.title = Title()
        self.title.text = title
        self.title.pos = (400, 200)
        
        self.btnOne = Button(text="One", pos=(150, 450))
        self.btnTwo = Button(text="Two", pos=(550, 450))


class Start_Menu(Menu):
    def __init__(self):
        super().__init__(title="SAVE SUST")
        self.playBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.title.color = "Green"
        self.title.size = 100

        self.playBtn.text = "Play"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)

    def render(self, surface):
        self.title.render(surface)
        self.playBtn.render(surface)
        self.quitBtn.render(surface)

class Game_Over_Menu(Menu):
    def __init__(self):
        super().__init__(title="GAME OVER")
        self.restartBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.title.color = "Red"
        self.title.size = 100

        self.restartBtn.text = "Restart"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)

    def render(self, surface):
        self.title.render(surface)
        self.restartBtn.render(surface)
        self.quitBtn.render(surface)
        
class Pause_Menu(Menu):
    def __init__(self):
        super().__init__(title="PAUSED")
        self.resumeBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.title.color = "Yellow"
        self.title.size = 100

        self.resumeBtn.text = "Resume"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)

    def render(self, surface):
        self.title.render(surface)
        self.resumeBtn.render(surface)
        self.quitBtn.render(surface)
            

