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
                if '-' in b[i][j]:
                    t2=b[i][j][5:9]
                    if t1 in token:
                        screen.blit(token[t1],pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width))
                t1=b[i][j][:4]
                if t1 in token:
                    screen.blit(token[t1],pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width))
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
        pygame.display.update()
    data_structures.dice_roll.append(num)
    pygame.time.delay(500)   
def check_valid(start):
    selectedtoken=b[start[0]][start[1]]
    if selectedtoken[:4]==data_structures.defturn:
        return True
    else:
        False
    
def field_to_track(token):
    for i in data_structures.Players:
        if i.get('playcolor')==data_structures.defturn:
                print('player',i['playcolor'])
            # if i['tokens_in_field']!=[]:
                for t in range(len(i['tokens_in_field'])):
                    # print(i['tokens_in_field'][t])
                    if i['tokens_in_field'][t][0]==token[0]:
                        pos=t
                        tokinfo=i['tokens_in_field'][t]
                        print('tokinfo',tokinfo)
                        for s in data_structures.stops:
                            if len(s[1])>1 and s[1][0]==token[0][0]:
                                print('stop')
                                track[s[0]].append(tokinfo)
                                temp=track[s[0]]
                                print('temp',temp)
                                destination=b[temp[0][0]][temp[0][1]]
                                i['tokens_on_track'].append((i['tokens_in_field'].pop(pos),temp[0],s[0]))
                                return (destination,temp[0])
    return ('not in field')
def in_track_move(token,dice):
    for i in data_structures.Players:
        if i.get('playcolor')==data_structures.defturn:
                print('player',i['playcolor'])
                for t in range(len(i['tokens_on_track'])):
                    # print(i['tokens_on_track'][t])
                    if i['tokens_on_track'][t][0]==token[0]:
                        tokinfo=i['tokens_on_track'][t]
                        print('tokinfo',tokinfo)
                        circlst=t[2]+dice
                        if tokinfo[2]!=47:
                            track[circlst].append(tokinfo)
                        else:
                            circlst=0
                            track[0].append(tokinfo)
                        temp=track[t[2]+dice]
                        print('temp',temp)
                        destination=b[temp[0][0]][temp[0][1]]
                        i['tokens_on_track'][t]=(i['tokens_on_track'][t][0],temp[0],circlst)
                        return (destination,temp[0])

def move(start,dice):
    tokinfo=()
    token=()
    pos=()
    selectedtoken=b[start[0]][start[1]]
    print('selectedtoken',selectedtoken)
    destination=[]
    if len(selectedtoken)<2:
        print('invalid')
        pass
    if '-' in selectedtoken:
        plaspot((selectedtoken[:5],0))
        for character in range(len(selectedtoken)):
            if selectedtoken[character]=='-':
                plaspot.append((selectedtoken[character+1:character+5],character))
        else:
            for ch in plaspot:
                count=0
                if ch[0]==data_structures.defturn:
                    token=(ch[0][3:5],ch[1])
                    break
                else:
                    count+=1
            if count==len(plaspot):
                pass
    else:
        if selectedtoken[:4]==data_structures.defturn:
            print('valid selection')
            token=(selectedtoken[3:5],'')
            print('token',token)
        else:
            pass
            # print(token)
    destination=field_to_track(token)
    if destination=='not in field':
        destination=in_track_move(token,dice)
    if destination!=[]:
        col=destination[0][-1]
        if 's' in destination[0]:
            col='s'+col
            print('col',col)
        if len(destination)>4:
            if destination[:4]==selectedtoken[:5]:
                b[destination[1][0]][destination[1][1]]=destination[:5]+'-'+selectedtoken[:5]+col
                print('destination',b[destination[1][0]][destination[1][1]])
        else:
            b[destination[1][0]][destination[1][1]]=selectedtoken[:5]+col
        if '-' in selectedtoken:
            b[start[0]][start[1]]=selectedtoken[:token[1]]+selectedtoken[token[1]+5:]
        else:
            b[start[0]][start[1]]=selectedtoken[5:]
    # 


