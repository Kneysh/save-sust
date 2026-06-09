from utils import colors
from utils.functions import text_object

class Message():
    def __init__(self, text="Message", font="BlackOpsOne", size=60, color=colors.baseColor, pos=(0,0)):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.pos = pos

    def render(self, surface):
        textSurf, textRect = text_object(self.text, self.font, self.size, self.color)
        textRect.center = self.pos
        surface.blit(textSurf, textRect)

