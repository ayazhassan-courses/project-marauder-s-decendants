import pygame
def text_objects(text, font):
    textSurface = font.render(text, True,(0,0,0))
    return textSurface, textSurface.get_rect()
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ludo')
Icon=pygame.image.load('dice.PNG')
pygame.display.set_icon(Icon)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((247,206,215))
    largeText = pygame.font.Font('Death Star.otf',115)
    TextSurf, TextRect = text_objects("Ludo", largeText)
    TextRect.center = ((400),(300))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
