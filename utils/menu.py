from utils import colors
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
        self.message.pos = (400, 300)
        
        self.btnOne = Button(pos=(150, 550))
        self.btnTwo = Button(pos=(550, 550))
        self.btnTwo.text = "Let Die"
        self.btnTwo.textColor = colors.baseColor
        self.btnTwo.activeColor = colors.red
        self.btnTwo.inactiveColor = colors.textColor

    def render(self, surface):
        self.info.render(surface)
        self.message.render(surface)
        self.btnOne.render(surface)
        self.btnTwo.render(surface)


class Start_Menu(Menu):
    def __init__(self):
        super().__init__(message="SAVE SUST", info="Press 'S' to save or 'L' to let die")

        self.message.color = colors.green
        self.message.size = 100

        self.btnOne.text = "Save"
   

class Game_Over_Menu(Menu):
    def __init__(self):
        super().__init__(message="SUST DESTROYED", info="Press 'R' to retry or 'L' to let die")


        self.message.color = colors.red
        self.message.size = 80
        self.message.pos = (400, 200)

        self.btnOne.text = "Retry"



    def final_time(self, surface, totalTime, highestTime, totalCoins):
        self.finalTime = Message()
        self.finalTime.text = f"Survived: {totalTime} s\nHighest: {highestTime} s\nWallet: $ {totalCoins}"
        self.finalTime.font = "Orbitron"
        self.finalTime.size = 30
        self.finalTime.color = colors.textColor
        self.finalTime.pos = (400, 400)

        self.finalTime.render(surface)

        
class Pause_Menu(Menu):
    def __init__(self):
        super().__init__(message="PAUSED", info="Press 'K' or 'Spacebar' to continue or 'L' to let die")

        self.message.color = colors.yellow
        self.message.size = 100

        self.btnOne.text = "Keep Saving"
        self.btnOne.width = 130
            

