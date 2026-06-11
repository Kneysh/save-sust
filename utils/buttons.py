import pygame
from utils import colors
from utils.functions import text_object, draw_block


class Button():
    def __init__(self, width=100, height=50, activeColor=colors.baseColor, inactiveColor=colors.blue, bgImg=None, pos=(0,0), text="Button", textSize=20, textFont="Roboto", textColor=colors.textColor, borderRadius=15):
        self.width = width
        self.height = height
        self.activeColor = activeColor
        self.inactiveColor = inactiveColor
        self.bgImg = bgImg
        self.pos = pos
        self.text = text
        self.textSize = textSize
        self.textFont = textFont
        self.textColor = textColor
        self.borderRadius = borderRadius

        if self.bgImg:
            self.imgRect = self.bgImg.get_rect(center = ((self.pos[0] + (self.width / 2)), (self.pos[1] + (self.height / 2))))


    def in_button(self):
        mouse = pygame.mouse.get_pos()
        return ((self.pos[0] + self.width) >= mouse[0] >= self.pos[0]) and ((self.pos[1] + self.height) >= mouse[1] >= self.pos[1])
    
    def render(self, surface):
        if self.bgImg:
            surface.blit(self.bgImg, self.imgRect)
        else:
            draw_block(surface, self.pos[0], self.pos[1], self.width, self.height, self.activeColor if self.in_button() else self.inactiveColor, self.borderRadius)
        
        self.textSurf, self.textRect =  text_object(self.text, self.textFont, self.textSize, self.textColor)
        self.textRect.center = ((self.pos[0] + (self.width / 2)), (self.pos[1] + (self.height / 2)))
        surface.blit(self.textSurf, self.textRect)

    
    def is_clicked(self):
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0]:
                return self.in_button()
            else:
                return False




