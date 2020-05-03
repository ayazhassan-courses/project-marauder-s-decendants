import pygame
import random
import data_f
def texto(text, font):
    textS = font.render(text, True,data_f.black)
    return textS, textS.get_rect()
def color(block):
    if block=='r':
        c=data_f.boardred
    elif block=='w':
        c=data_f.white
    elif block=='b':
        c=data_f.boardblue
    elif block=='g':
        c=data_f.boardgreen
    elif block=='y':
        c=data_f.boardyellow
    elif block=='p':
        c=data_f.boardpath
    else:
        c=data_f.black
    return c
# def fade():
#     f=pygame.Surface(data_f.screenwidth,data_f.screenheight)
#     f.fill(data_f.black)
#     for i in range(300):
#         fade.set_alpha(i)
#         re
def callboard(screen,b):
    maincolors=['r','b','y','g']
    width=data_f.boardwidthtiles
    height=data_f.boardheighttiles
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]=='s':
                r=pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width)
                if b[i+1][j] in maincolors:
                    pygame.draw.rect(screen,color(b[i+1][j]),r)
                    screen.blit(pygame.image.load(data_f.safepoint),((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty))
                elif b[i][j+1] in maincolors:
                    pygame.draw.rect(screen,color(b[i][j+1]),r)
                    screen.blit(pygame.image.load(data_f.safepoint),((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty))
            else:
                r=pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width)
                pygame.draw.rect(screen,color(b[i][j]),r)
def separator(screen,b):
    width=data_f.boardwidthtiles
    height=data_f.boardheighttiles
    for i in range(len(b[0])+1):
        h=i*height
        w=i*width
        pygame.draw.line(screen,data_f.screencolor,(data_f.boardstartx+w,data_f.boardstarty),(data_f.boardstartx+w,data_f.boardstarty+data_f.boardheight),2)
        pygame.draw.line(screen,data_f.screencolor,(data_f.boardstartx,h+data_f.boardstarty),(data_f.boardstartx+data_f.boardwidth,h+data_f.boardstarty),2)
def startgame():
    pygame.init()
    screen=pygame.display.set_mode((data_f.screenwidth,data_f.screenheight))
    pygame.display.set_caption(data_f.title)
    Icon=pygame.image.load(data_f.logo)
    pygame.display.set_icon(Icon)
    return screen
def game(screen,b):
    clock=pygame.time.Clock() 
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            # if event.type==pygame.K_ESCAPE:
            #     running=False
        # mainmenu(screen)
        screen.fill(data_f.screencolor)
        callboard(screen,b)
        separator(screen,b)
        dicebutton=button('Roll Dice',50,50,100,50,data_f.boardred,True,screen)
        if dicebutton==True:
            dice(screen)
        pygame.display.update()
        clock.tick(60)
def makeboard():
    board=[]
    file = open('board.txt', 'r')
    f=file.read()
    r=f.splitlines()
    file.close()
    for i in r:
        board.append(i.split(','))
    return board
def button(text,x,y,w,h,color,function,screen):
    mouse=pygame.mouse.get_pos()
    press=pygame.mouse.get_pressed()
    pygame.draw.rect(screen,color,(x,y,w,h))
    
    if mouse[0]>x and mouse[0]<x+w and mouse[1]>y and mouse[1]<y+h:
        pygame.draw.rect(screen,color,(x-12.5,y-12.5,w+25,h+25))
        if press[0]==1 and function!=None:
            return function
    gtext= pygame.font.Font(data_f.textfont,data_f.textfsize)
    start_text, start_textbox= texto(text, gtext)
    start_textbox.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(start_text, start_textbox) 
def mainmenu(screen):
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        screen.fill(data_f.screencolor)
        screen.blit(pygame.image.load(data_f.titleimage),((data_f.screenwidth/2)-250,(data_f.screenheight/2)-250))
        title = pygame.font.Font(data_f.titlefont,data_f.titlefsize)
        title_text, title_textbox = texto(data_f.title, title)
        title_textbox.center = ((data_f.screenwidth/2),(data_f.screenheight/2))
        screen.blit(title_text, title_textbox)
        # pygame.Rect(450,600,50,50)
        p=button('Play',(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50,data_f.boardgreen,True,screen)
        if p==True:
            return True
        q=button('Quit',(data_f.screenwidth/2)+50,(data_f.screenheight/2)+50,150,50,data_f.boardred,True,screen)
        if q==True:
            return False
        pygame.display.update()
def dice(screen):
    # rolling=True
    # while rolling:
    count=0
    num=random.randint(1,6)
    while count!=1:
        pygame.draw.rect(screen,data_f.white,((data_f.diceposx),(data_f.diceposy),data_f.dicewidth,data_f.diceheight))
        if num==1:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
            # rolling==False
        if num==2:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            # rolling==False
        if num==3:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            # rolling==False
        if num==4:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            # rolling==False
        if num==5:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            # rolling==False
        if num==6:

            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            # rolling==False
        count+=1
    pygame.display.update()
def m():
    screen=startgame()
    if mainmenu(screen)==True:

        game(screen,makeboard())
    else:
        pygame.quit()
if __name__=='__main__':
    m()