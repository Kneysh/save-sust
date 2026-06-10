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
        super().__init__(message="SAVE SUST", info="Press 'S' to save or 'L' to let die")

        self.message.color = "Green"
        self.message.size = 100

        self.btnOne.text = "Save"

        self.btnTwo.text = "Let Die"
        self.btnTwo.activeColor = "Red"
        self.btnTwo.inactiveColor = (200, 0, 0)
   

class Game_Over_Menu(Menu):
    def __init__(self):
        super().__init__(message="SUST DESTROYED", info="Press 'R' to retry or 'L' to let die")


        self.message.color = "Red"
        self.message.size = 80

        self.btnOne.text = "Retry"

        self.btnTwo.text = "Let Die"
        self.btnTwo.activeColor = "Red"
        self.btnTwo.inactiveColor = (200, 0, 0)

    def final_time(self, totalTime, highestTime, surface):
        self.finalTime = Message()
        self.finalTime.text = f"Survived: {totalTime} s\nHighest: {highestTime} s"
        self.finalTime.font = "Orbitron"
        self.finalTime.size = 30
        self.finalTime.color = colors.textColor
        self.finalTime.pos = (400, 350)

        self.finalTime.render(surface)

        
class Pause_Menu(Menu):
    def __init__(self):
        super().__init__(message="PAUSED", info="Press 'K' or 'Spacebar' to continue or 'L' to let die")

        self.message.color = "Yellow"
        self.message.size = 100

        self.btnOne.text = "Keep Saving"
        self.btnOne.width = 130

        self.btnTwo.text = "Let Die"
        self.btnTwo.activeColor = "Red"
        self.btnTwo.inactiveColor = (200, 0, 0)

            

