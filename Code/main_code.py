#more files to keep clutter low in main file
import pygame
import random
import data_f
import data_structures
import mutual
from mutual import * 
from board_tokens import *
from data_structures import *
def texto(text, font): #button text
    textS = font.render(text, True, data_f.black)
    return textS, textS.get_rect()
def gamestate():
    callboard()
    separator()
    drawtoken()
def get_colrows(mouse):
    cr=()
    for i in range(len(data_structures.bdata)):
        for j in range(len(data_structures.bdata[0])):
            if mouse[0]>data_structures.bdata[i][j][1][0] and mouse[0]<data_structures.bdata[i][j][1][0]+data_f.boardwidthtiles and mouse[1]>data_structures.bdata[i][j][1][1] and mouse[1]<data_structures.bdata[i][j][1][1]+data_f.boardheighttiles:
                # print(mouse)
                col=j
                row=i
                cr=(col,row)
                return cr
    return -1

def game():
    loadtokens()
    tile=()
    clickarg=[]  #accept the player's input 
    clock=pygame.time.Clock() 
    running=True
    n=0
    # the variables n and defturn are almost similarr. need to think of a way to simplify
    valid=False
    while running:
        for event in pygame.event.get(): #to quit the game
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN: #if mouse clicked 
                mouse=pygame.mouse.get_pos() #gets x and y coordinate of position of mouse click in tuple
                print('mouse',mouse)
                if get_colrows(mouse)!=-1: #checks if either board is clicked or the knight needs to be confirmed with ifrah
                    tile=get_colrows(mouse)
                    clickarg.append(tile)
                    # extra variable tile maybe unnecessary
                else:
                    print('click on the knight!')
                if len(clickarg)==1: #clickarg will either have 1 or no value in the form of tile
                    if is_empty(data_structures.dice_roll)==False:
                        if top(data_structures.dice_roll)!='you got 3 sixes, your turn will be passed':
                            if check_valid(clickarg[0])==True:
                                # may need to implement check wvalid everywhere
                                print('clickarg',clickarg)
                                move(clickarg[0],top(data_structures.dice_roll))
                                pop(data_structures.dice_roll)
                                print('dice',data_structures.dice_roll)
                                if is_empty(data_structures.dice_roll)==True:
                                    print('your turn has ended')
                                    valid=True

                            else:
                                print('Wrong Move!',b[clickarg[0][0]][clickarg[0][1]])
                        else:
                            print('your turn will be passed')
                    else:
                        print('roll dice')
                clickarg=[]
            if valid==True and is_empty(data_structures.dice_roll)==True:
                print('playerturn',n)
                if n==3:
                    n=0
                    data_structures.defturn=turn(n)
                    if data_structures.defturn == 'plar':
                        print("Player RED's turn")
                    valid = False
                else:
                    n+=1
                    data_structures.defturn=turn(n)
                    if data_structures.defturn == 'plab':
                        print("Player BLUE's turn")
                    elif data_structures.defturn == 'plag':
                        print("Player GREEN's turn")
                    elif data_structures.defturn == 'play':
                        print("Player YELLOW's turn")
                    valid=False
                    
        screen.fill(data_f.screencolor)
        gamestate()
        # need to revise button function
        dicebutton, display =button('Roll Dice',50,50,100,50,data_f.boardred, 'dice')
        if dicebutton and display:
            if len(data_structures.dice_roll)==1 and top(data_structures.dice_roll)!=6:
                print('invalid')
            else: 
                dice()
            print(data_structures.dice_roll)
            six_count=0
            if top(data_structures.dice_roll)==6:
                six_count=1
            while top(data_structures.dice_roll)==6 and six_count!=3:
                dice()
                if top(data_structures.dice_roll)==6:
                    six_count+=1
                print('dice stack',data_structures.dice_roll)
            if six_count==3:
                while is_empty(data_structures.dice_roll)==False:
                   pop(data_structures.dice_roll) 
                data_structures.dice_roll.append('you got 3 sixes, your turn will be passed')
                
        pygame.display.update()
        clock.tick(60)
def button(text,x,y,w,h,color,screentype,function=None):
    # the variable named function not needed and revise the button function
    mouse=pygame.mouse.get_pos()
    press=pygame.mouse.get_pressed()
    pygame.draw.rect(screen,color,(x,y,w,h))
    display = False

    if mouse[0]>x and mouse[0]<x+w and mouse[1]>y and mouse[1]<y+h:
        pygame.draw.rect(screen,color,(x-12.5,y-12.5,w+25,h+25))
        if press[0]==1 and function==None and screentype == 'dice':
            gtext= pygame.font.Font(data_f.textfont,data_f.textfsize)
            start_text, start_textbox= texto(text, gtext)
            start_textbox.center = ((x+(w/2)),(y+(h/2)))
            screen.blit(start_text, start_textbox)    
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
    # mainmenu needs to be fixed
    # if mainmenu()==True:
    game()
    # else:
    pygame.quit()
if __name__=='__main__':
    m()