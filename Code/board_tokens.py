import pygame
import data_f
import data_structures
from mutual import *
import random

#for board and token related code
token={}
def colors(block): #adding color to board
    if block[0]=='r':
        c=data_f.boardred
    elif block[0]=='b':
        c=data_f.boardblue
    elif block[0]=='g':
        c=data_f.boardgreen
    elif block[0]=='y':
        c=data_f.boardyellow
    elif block[0]=='p':
        c=data_f.boardpath
    else:
        c=data_f.white
    return c
def callboard(): #visually draws board
    width=data_f.boardwidthtiles
    height=data_f.boardheighttiles
    for i in range(len(b)):
        for j in range(len(b[0])):
            r=pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width)            
            if len(b[i][j])>=2:
                c=b[i][j][-1]
                pygame.draw.rect(screen,colors(c),r)
                if 's' in b[i][j]:
                    screen.blit(pygame.image.load(data_f.safepoint),((j*width)+data_f.boardstartx+(width/6),(i*height)+data_f.boardstarty+(height/4)))
            else:
                c=b[i][j]
                pygame.draw.rect(screen,colors(c),r)
                # data_structures.bdata.append((b[i][j],(i*width)+data_f.boardstartx,(j*height)+data_f.boardstarty))
    # for i in data_structures.Players:
    #     lstofplayers=i[0].get('tokens_in_field')
    #     color=i[1]
    #     drawtoken(screen,color,x,y)
def separator():
    width=data_f.boardwidthtiles
    height=data_f.boardheighttiles
    for i in range(len(b[0])+1):
        h=i*height
        w=i*width
        pygame.draw.line(screen,data_f.screencolor,(data_f.boardstartx+w,data_f.boardstarty),(data_f.boardstartx+w,data_f.boardstarty+data_f.boardheight),2)
        pygame.draw.line(screen,data_f.screencolor,(data_f.boardstartx,h+data_f.boardstarty),(data_f.boardstartx+data_f.boardwidth,h+data_f.boardstarty),2)
def loadtokens(): #loading token images into dictionary called token
    t=['plar','plab','plag','play'] #pla (= player) + r/b/g/y (for color)
    for i in t:
        if i=='plar':
            token[i]=pygame.transform.scale(pygame.image.load(data_f.red_token),(data_f.boardwidthtiles,data_f.boardheighttiles))
    
        if i=='plab':
            token[i]=pygame.transform.scale(pygame.image.load(data_f.blue_token),(data_f.boardwidthtiles,data_f.boardheighttiles))

        if i=='plag':
            token[i]=pygame.transform.scale(pygame.image.load(data_f.green_token),(data_f.boardwidthtiles,data_f.boardheighttiles))

        if i=='play':
            token[i]=pygame.transform.scale(pygame.image.load(data_f.yellow_token),(data_f.boardwidthtiles,data_f.boardheighttiles))
def drawtoken(): #reads board and draws token where 'plar' etc are
    width=data_f.boardwidthtiles
    height=data_f.boardheighttiles
    for i in range(len(b)):
        for j in range(len(b[0])):
            if len(b[i][j])>2:
                t=b[i][j][:4]
                if t in token:
                    screen.blit(token[t],pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width))
def dice():
    count=0
    while count!=10:
        num=random.randint(1,6)
        pygame.draw.rect(screen,data_f.white,((data_f.diceposx),(data_f.diceposy),data_f.dicewidth,data_f.diceheight))
        if num==1:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
        if num==2:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
        if num==3:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
        if num==4:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
        if num==5:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+(data_f.dicewidth//2),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
        if num==6:
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)+(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)+(data_f.diceheight//4)),8)
            pygame.draw.circle(screen,data_f.black,(data_f.diceposx+((data_f.dicewidth//2)-(data_f.dicewidth//4)),data_f.diceposy+(data_f.diceheight//2)-(data_f.diceheight//4)),8)
        count+=1
        pygame.time.delay(100)
    data_structures.dice_roll.append(num)
    pygame.time.delay(5000)
def check_valid(start): #??
    selectedtoken=b[start[0]][start[1]]
    if selectedtoken[:4]==data_structures.defturn:
        return True
    else:
        False
def move(start,die):
    tokinfo=()
    selectedtoken=b[start[0]][start[1]]
    # print(selectedtoken)
    print(selectedtoken[:4],data_structures.defturn)
    if selectedtoken[:4]==data_structures.defturn:
        if len(selectedtoken)>2:
            token=selectedtoken[3:5]
            # print(token)
            for i in data_structures.Players:
                if i.get('playcolor')==data_structures.defturn:
                    if i['tokens_on_track']==[]:
                        for t in range(len(i['tokens_in_field'])):
                            # print(i['tokens_in_field'][t])
                            if i['tokens_in_field'][t][0]==token:
                                pos=t
                                tokinfo=i['tokens_in_field'][t]
            
                                
                                # print(tokinfo)
                                for s in data_structures.stops:
                                    if len(s[1])>1 and s[1][0]==selectedtoken[3]:
                                        track[s[0]].append(tokinfo)
                                        temp=track[s[0]]
                                        destination=b[temp[0][0]][temp[0][1]]
                                        print(destination)
                                        # print(b[t[1][0]][t[1][0]])
                                        col=destination[-1]
                                        if 's' in destination:
                                            col+='s'+col
                                        b[temp[0][0]][temp[0][1]]=selectedtoken[:4]+col
                                        b[start[0]][start[1]]=selectedtoken[5:]
                                        break
                        i['tokens_on_track'].append(i['tokens_in_field'].pop(pos))
                        print(i['tokens_on_track'])
                        print(i['tokens_in_field'])
                                
                                    

                    break
            
        else:
            pass
    else:
        print('invalid move')


