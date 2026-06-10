import pygame
from utils import colors
from utils.functions import text_object, draw_block
from utils.buttons import Button
from utils.message import Message


class Menu():
    def __init__(self, message, info=None):
        self.info = Message()
        self.info.text = info
        self.info.font = "Orbitron"
        self.info.size = 25
        self.info.color = colors.textColor
        self.info.pos = (400, 50)


        self.message = Message()
        self.message.text = message
        self.message.pos = (400, 200)
        
        self.btnOne = Button(text="One", pos=(150, 450))
        self.btnTwo = Button(text="Two", pos=(550, 450))

    def render(self, surface):
        self.info.render(surface)
        self.message.render(surface)
        self.btnOne.render(surface)
        self.btnTwo.render(surface)


class Start_Menu(Menu):
    def __init__(self):
        super().__init__(message="SAVE SUST", info="Press 'P' to play or 'Q' to quit")
        self.playBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.message.color = "Green"
        self.message.size = 100

        self.playBtn.text = "Play"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)
   

class Game_Over_Menu(Menu):
    def __init__(self):
        super().__init__(message="GAME OVER", info="Press 'R' to restart or 'Q' to quit")
        self.restartBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.message.color = "Red"
        self.message.size = 100

        self.restartBtn.text = "Restart"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)

    def final_score(self, finalScore, surface):
        self.finalScore = Message()
        self.finalScore.text = "Final Score: " + finalScore
        self.finalScore.font = "Orbitron"
        self.finalScore.size = 30
        self.finalScore.color = colors.textColor
        self.finalScore.pos = (400, 350)

        self.finalScore.render(surface)

        
class Pause_Menu(Menu):
    def __init__(self):
        super().__init__(message="PAUSED", info="Press 'C' or 'Spacebar' to continue or 'Q' to quit")
        self.continueBtn = self.btnOne
        self.quitBtn = self.btnTwo

        self.message.color = "Yellow"
        self.message.size = 100

        self.continueBtn.text = "Continue"

        self.quitBtn.text = "Quit"
        self.quitBtn.activeColor = "Red"
        self.quitBtn.inactiveColor = (200, 0, 0)

            

