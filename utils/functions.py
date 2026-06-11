import pygame

IMG_LOC = "assets/images/"
FONT_LOC = "assets/fonts/"

# image loading
def load_image(path):
    img = pygame.image.load(IMG_LOC + path).convert_alpha()
    return img

# text render
def text_object(text, font, size, color):
    font = pygame.font.Font((FONT_LOC + font + ".ttf"), size)
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()

# drawing block
def draw_block(surface, x_pos, y_pos, width, height, color, borderRadius=0):
    pygame.draw.rect(surface, color, [x_pos, y_pos, width, height], border_radius=borderRadius)

