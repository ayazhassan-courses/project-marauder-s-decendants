import pygame
import random
import data_f
import data_structures
from mutual import *
from board_tokens import *
from data_structures import *
def texto(text, font):
    textS = font.render(text, True, data_f.black)
    return textS, textS.get_rect()
def gamestate():
    callboard()
    separator()
    drawtoken()
def game():
    loadtokens()
    tile=()
    clickarg=[]
    clock=pygame.time.Clock() 
    running=True
    n=0
    defturn='plar'
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                press=pygame.mouse.get_pressed()
                print(mouse)
                # if press[0]==1:
                for i in range(len(data_structures.bdata)):
                    for j in range(len(data_structures.bdata[0])):
                        if mouse[0]>data_structures.bdata[i][j][1][0] and mouse[0]<data_structures.bdata[i][j][1][0]+data_f.boardwidthtiles and mouse[1]>data_structures.bdata[i][j][1][1] and mouse[1]<data_structures.bdata[i][j][1][1]+data_f.boardheighttiles:
                            # print(mouse)
                            col=j
                            row=i
                            print(col,row)
                            if tile==(col,row):
                                tile=()
                                clickarg=[]
                            # tile=(col,row)
                            # clickarg.append(tile)
                            if len(clickarg)==1:
                                print(clickarg)
                                while is_empty(data_structures.dice_roll)==False:
                                    # move(clickarg[0],top(data_structures.dice_roll))
                                    pop(data_structures.dice_roll)
                                clickarg=[]
                                if n>3:
                                    n=0
                                else:
                                    n+=1
                                defturn=turn(n)
                    
        screen.fill(data_f.screencolor)
        gamestate()
        dicebutton, display =button('Roll Dice',50,50,100,50,data_f.boardred, 'dice')
        if dicebutton and display:
            dice()
            print(data_structures.dice_roll)
            count=0
            if top(data_structures.dice_roll)==6:
                count=1
            while top(data_structures.dice_roll)==6 and count!=3:
                dice()
                count+=1
                print(data_structures.dice_roll)
            if count==3:
                while is_empty(data_structures.dice_roll)==False:
                   pop(data_structures.dice_roll) 
            # else:
                # mouse=pygame.mouse.get_pos()
                # press=pygame.mouse.get_pressed()
                # print(mouse)
                # if press[0]==1:
                #     for i in range(len(data_structures.bdata)):
                #         for j in range(len(data_structures.bdata[0])):
                #             if mouse[0]>data_structures.bdata[i][j][1][0] and mouse[0]<data_structures.bdata[i][j][1][0]+data_f.boardwidthtiles and mouse[1]>data_structures.bdata[i][j][1][1] and mouse[1]<data_structures.bdata[i][j][1][1]+data_f.boardheighttiles:
                #                 # print(mouse)
                #                 col=j
                #                 row=i
                #                 print(col,row)
                #                 if tile==(col,row):
                #                     tile=()
                #                     clickarg=[]
                #                 tile=(col,row)
                #                 clickarg.append(tile)
                #                 if len(clickarg)==2:
                #                     print(clickarg)
                #                     move(clickarg[0],clickarg[1])
                #                     clickarg=[]
                
        pygame.display.update()
        clock.tick(60)
def button(text,x,y,w,h,color,screentype,function=None):
    mouse=pygame.mouse.get_pos()
    press=pygame.mouse.get_pressed()
    pygame.draw.rect(screen,color,(x,y,w,h))
    display = False

    if mouse[0]>x and mouse[0]<x+w and mouse[1]>y and mouse[1]<y+h:
        pygame.draw.rect(screen,color,(x-12.5,y-12.5,w+25,h+25))
        if press[0]==1 and function==None and screentype == 'dice':
            display = True
            return True, display
        elif press[0]==1 and function==None and screentype == 'menu':
            return True, False
    gtext= pygame.font.Font(data_f.textfont,data_f.textfsize)
    start_text, start_textbox= texto(text, gtext)
    start_textbox.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(start_text, start_textbox) 
    return False, display

def mainmenu():
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
        p, p2=button('Play',(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50,data_f.boardgreen,screen, 'menu')
        if p==True and p2 == False:
            return True
        q, q2=button('Quit',(data_f.screenwidth/2)+50,(data_f.screenheight/2)+50,150,50,data_f.boardred,screen, 'menu')
        if q==True and q2 == False:
            return False
        pygame.display.update()

def m():
    screen=startgame()
    # if mainmenu()==True:
    game()
    # else:
        # pygame.quit()
if __name__=='__main__':
    m()