import pygame
def texto(text, font):
    textS = font.render(text, True,(0,0,0))
    return textS, textS.get_rect()
def mainmenu(screen):
    menu=True
    while menu:
        screen.fill((247,206,215))
        largeText = pygame.font.Font('Death Star.otf',85)
        TextSurf, TextRect = texto("Ludo", largeText)
        TextRect.center = ((400),(300))
        screen.blit(TextSurf, TextRect)
        pygame.Rect(450,600,50,50)
        pygame.draw.rect()
        pygame.display.update()
def color(block):
    if block=='r':
        c=(223,101,129)
    elif block=='w':
        c=(255,255,255)
    elif block=='l':
        c=(106,110,219)
    elif block=='g':
        c=(106,222,171)
    elif block=='y':
        c=(255,233,162)
    elif block=='p':
        c=(229,233,240)
    else:
        c=(0,0,0)
    return c
def callboard(screen,b):
    width=round(800/len(b[0]))
    height=round(800/len(b))
    for i in range(len(b)):
        for j in range(len(b[0])):
            r=pygame.Rect(i*height,j*width,height,width)
            pygame.draw.rect(screen,color(b[i][j]),r)
def separator(screen,b):
    width=round(800/len(b[0]))
    height=round(800/len(b))
    for i in range(len(b[0])):
        h=i*height
        w=i*width
        pygame.draw.line(screen,(0,0,0),(0,w),(800,w),1)
        pygame.draw.line(screen,(0,0,0),(h,0),(h,800),1)
def startgame():
    pygame.init()
    screen=pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Ludo')
    Icon=pygame.image.load('dice.PNG')
    pygame.display.set_icon(Icon)
    return screen
def game(screen,b):
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            # if event.type==pygame.K_ESCAPE:
            #     running=False
        # mainmenu(screen)
        callboard(screen,b)
        separator(screen,b)
        pygame.display.update()
def makeboard():
    board=[]
    file = open('board.txt', 'r')
    f=file.read()
    r=f.splitlines()
    file.close()
    for i in r:
        board.append(i.split(','))
    return board
def m():
    b=makeboard()
    screen=startgame()
    game(screen,b)
if __name__=='__main__':
    m()