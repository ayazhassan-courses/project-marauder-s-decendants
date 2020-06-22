import pygame
import data_f
import data_structures
from data_structures import *
from mutual import *
import random
# rename variables
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
                t1=b[i][j][:4]
                if '-' in b[i][j]:
                    plaspot=[]
                    plaspot.append(t1) #first token is saved in plaspot
                    for character in range(len(b[i][j])):
                            if b[i][j][character]=='-': #if more than one token is present, they will be identified and stored in plaspot too
                                plaspot.append(b[i][j][character+1:character+6]) 
                    count=0
                    for p in plaspot:
                        if p[:4] in token:
                            count+=3
                            screen.blit(token[p[:4]],pygame.Rect((j*width)+data_f.boardstartx+count,(i*height)+data_f.boardstarty,height,width)) #play with this to handle multiple token on one spot
                else:
                    if t1 in token:
                        screen.blit(token[t1],pygame.Rect((j*width)+data_f.boardstartx,(i*height)+data_f.boardstarty,height,width))
def dice():
    clock=pygame.time.Clock() 
    count=0
    while count!=5:
        num=random.randint(1,6)
        # num=6
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
        pygame.time.delay(75)
        pygame.display.update()
    push(data_structures.dice_roll, num)
    pygame.time.delay(400)
    clock.tick(30)   
def check_valid(start):
    plaspot=[]
    selectedtoken=b[start[0]][start[1]]
    if '-' in selectedtoken:
        plaspot.append((selectedtoken[:5],0)) #first token is saved in plaspot
        for character in range(len(selectedtoken)):
            if selectedtoken[character]=='-': #if more than one token is present, they will be identified and stored in plaspot too
                plaspot.append((selectedtoken[character+1:character+6],character))
        # print('check valid plaspot',plaspot)
        for ch in plaspot: 
            if ch[0][:4]==data_structures.defturn:
                return True
        return False
    else:
        if selectedtoken[:4]==data_structures.defturn:
            return True
        else:
            return False
def findplayer():
    for i in data_structures.Players:
        if i['playcolor']==data_structures.defturn:
            return i
def seetokensinfield(pla,colrow):
    for i in pla['tokens_in_field']:
        if i[1]==colrow:
            return True    
def field_to_track(token,dice,start):
    # print('dice',dice)
    if dice!=6 and seetokensinfield(findplayer(),start)==True:
        return 'you need a six'
    for i in data_structures.Players:
        if i['playcolor']==data_structures.defturn:
                # print('player',i['playcolor'])
                for t in range(len(i['tokens_in_field'])):
                    # print(i['tokens_in_field'],token[0])
                    if i['tokens_in_field'][t][0]==token[0]:
                        pos=t
                        tokinfo=i['tokens_in_field'][t]
                        # print('tokinfo',tokinfo)
                        for s in data_structures.stops:
                            if len(s[1])>1 and s[1][0]==token[0][0]:
                                # print('stop')
                                track[s[0]].append(tokinfo) #tokinfo contains what token it is and its original position
                                temp=track[s[0]] #temp has all the information of the tile. temp[0] has the coordinates of the tile. s[0] is the tile number which is a stop
                                # print('temp',temp)
                                destination=b[temp[0][0]][temp[0][1]]
                                i['tokens_on_track'].append((i['tokens_in_field'].pop(pos),temp[0],s[0])) 
                                # print('when it moves field to track, tokens in track becomes',i['tokens_on_track'])
                                return (destination,temp[0],temp)
    return ('not in field')
def in_track_move(token,dice): #need to make changes
    for i in data_structures.Players:
        # find the token which was selected in the dict
        # print(i['home'])
        if i['home']!=[]:
            for h in i['home']:
                if h[0]==token[0]:
                    h=towardshome(token,dice,h[1])
                    # print('home token',h)
                    return h
        if i['playcolor']==data_structures.defturn:
                # print('player',i['playcolor'])
                # if u found the player dict, than search for it in token on track
                for t in range(len(i['tokens_on_track'])):
                    # if the color and number match then store the info of the token in tokinfo
                    # circlist updates the tile number
                    if i['tokens_on_track'][t][0][0]==token[0]:
                            tokinfo=i['tokens_on_track'][t]
                            # print('tokinfo',tokinfo)
                            circlst=tokinfo[2]
                            oldtile=tokinfo[2]
                            for d in range(dice):
                                    # print('the number',d,'the dice',dice)
                                    circlst+=1
                                    # print('updating circlst',circlst)
                                    if circlst>=48:
                                        circlst=0
                                    if i['tokens_on_track'][t][0][2]+d+1==46 and i['ousted']==True: 
                                        h=towardshome(token,dice-d-1,track[circlst][0])
                                        # print('home token',h)
                                        return h
                            temp=track[circlst]
                            # print('track[oldtile]',track[oldtile])
                            # print('track[circlst]',track[circlst])
                            tilestraversed=tokinfo[0][2]+dice
                            track[oldtile].remove(tokinfo[0])
                            track[circlst].append((tokinfo[0][0],tokinfo[0][1],tilestraversed))
                            # print('temp hopeful',temp) 
                            destination=b[temp[0][0]][temp[0][1]]
                            i['tokens_on_track'][t]=((i['tokens_on_track'][t][0][0],i['tokens_on_track'][t][0][1],i['tokens_on_track'][t][0][2]+dice),temp[0],circlst)
                            return (destination,temp[0],temp)
                
def towardshome(token,dice,loc):
    destination=()
    temp=()
    hompos=[]
    uncertain=[]
    tbr = ()
    locx=loc[0]
    locy=loc[1]
    for_outhome=()
    for i in data_structures.homelanes:
        # print('check')
        if i[0]==token[0][0]:
            for j in data_structures.Players:
                if j['playcolor'][3] == token[0][0]:
                    pl = j
            if j['home']!=[]:
                for h in i['home']:
                    if h[0]==token[0]:
                        uncertain=h[0]
                        # print('home token',h)
            else:
                for j in range(len(pl['tokens_on_track'])):
                    if pl['tokens_on_track'][j][0][0] == token[0]:
                        tbr = j
                        hompos = pl['tokens_on_track'][j][2]
                        # print(pl['tokens_on_track'], 'is token on track that has to be emptied later')
            homestart=i[1][0]
            homefin=i[1][1]
            if homestart[0]==homefin[0]:
                if homestart[1]<homefin[1]:
                    if locy+dice==homefin[1]+1:
                        pl['tokens_won']+=1
                        for i in range(len(pl['home'])):
                            if pl['home'][i][0] == token[0]:
                                for_outhome = pl['home'][i]
                                pl['home'].pop(i)
                        pl['outofhome'].append(for_outhome)
                        print('token ', token[0], 'went home!')
                        return 'token won'
                        # it will go home
                    elif locy+dice>homefin[1]+1:
                        # greater number than home 
                        return 'not possible'
                    else:
                        temp=(locx,locy+dice)
                        if token not in pl['home']:
                            pl['home'].append((token[0],temp))
                            pl['tokens_on_track'].pop(tbr)
                            for to in range(1, len(track[hompos])):
                                if track[hompos][to][0] == track[0]:
                                    track[hompos].pop(to)

                else:
                    if locy-dice==homefin[1]-1:
                        pl['tokens_won']+=1
                        for i in range(len(pl['home'])):
                            if pl['home'][i][0] == token[0]:
                                for_outhome = pl['home'][i]
                                pl['home'].pop(i)
                        pl['outofhome'].append(for_outhome)
                        print('token ', token[0], 'went home!')
                        return 'token won'
                        # it will go home
                    elif locy-dice<homefin[1]+1:
                        # greater number than home 
                        return 'not possible'
                    else:
                        temp=(locx,locy-dice)
                        if token not in pl['home']:
                            pl['home'].append((token[0],temp))
                            pl['tokens_on_track'].pop(tbr)
                            for to in range(1, len(track[hompos])):
                                if track[hompos][to][0] == track[0]:
                                    track[hompos].pop(to)
            else:
                if homestart[0]<homefin[0]:
                    if locx+dice==homefin[0]+1:
                        pl['tokens_won']+=1

                        for i in range(len(pl['home'])):
                            if pl['home'][i][0] == token[0]:
                                for_outhome = pl['home'][i]
                                pl['home'].pop(i)
                        pl['outofhome'].append(for_outhome)
                        print('token ', token[0], 'went home!')
                        return 'token won'

                    elif locx+dice>homefin[0]+1:
                        # greater number than home 
                        return 'not possible'
                    else:
                        temp=(locx+dice,locy)
                        if token not in pl['home']:
                            pl['home'].append((token[0],temp))
                            pl['tokens_on_track'].pop(tbr)
                            for to in range(1, len(track[hompos])):
                                if track[hompos][to][0] == track[0]:
                                    track[hompos].pop(to)
                else:
                    if locx-dice==homefin[0]-1:
                        pl['tokens_won']+=1
                        for i in range(len(pl['home'])):
                            if pl['home'][i][0] == token[0]:
                                for_outhome = pl['home'][i]
                                pl['home'].pop(i)
                        pl['outofhome'].append(for_outhome)
                        print('token ', token[0], 'went home!')
                        return 'token won'
                        # it will go home
                    elif locx-dice<homefin[0]+1:
                        # greater number than home 
                        return 'not possible'
                    else:
                        temp=(locx-dice,locy)
                        if token not in pl['home']:
                                pl['home'].append((token[0], temp))
                                pl['tokens_on_track'].pop(tbr)
                                for to in range(1, len(track[hompos])):
                                    if track[hompos][to][0] == track[0]:
                                        track[hompos].pop(to)
            destination=b[temp[0]][temp[1]]
            # print(destination, 'is destination for home')
            info=pl['home'] 
            return (destination,temp,info)

def move(start,dicee):
    tokinfo=()
    token=() #first argument is the colour and the number of the token, second is the position in the selectedtoken 
    pos=()
    plaspot=[]
    selectedtoken=b[start[0]][start[1]]
    # print('selectedtoken',selectedtoken)
    destination=[]
    if len(selectedtoken)<2:
        print('invalid')
        pass
    if '-' in selectedtoken: #there is a chance of multiple tokens
        plaspot.append((selectedtoken[:5],-1)) #first token is saved in plaspot
        for character in range(len(selectedtoken)):
            if selectedtoken[character]=='-': #if more than one token is present, they will be identified and stored in plaspot too
                plaspot.append((selectedtoken[character+1:character+6],character))
        # plaspot is a nested tuple containing multiple tokens on a tile
        for ch in plaspot: #nested tuple 
            # count is for to keep track if the selected place has the token of the player
            # so it will run a loop. if it finds the player's token, then it will save it in the variable token and it will break
            # else if the count is equal to the length of the tuple plaspot, it will pass
            # need to make this part a function
            count=0
            if ch[0][:4]==data_structures.defturn: #to be checked
                token=(ch[0][3:5],ch[1])
                # print('one of the multiple tokens',token)
                break
            else:
                count+=1
        if count==len(plaspot):
            pass
    else: #only one token 
        if selectedtoken[:4]==data_structures.defturn:
            # print('valid selection')
            token=(selectedtoken[3:5],'')
            # print('token',token)
        else:
            pass
            # print(token)
    destination=field_to_track(token,dicee,start)
    if destination=='you need a six':
        print('you need a six')
        return False
    if destination=='not in field': 
        print('not in field') #nothing returned here
        destination=in_track_move(token,dicee)
        # print(' we are checking for destination', destination)
        if destination=='end the game':
            data_structures.end=True
            winner=data_structures.defturn
            pass
        if destination=='not possible':
            print('this is not possible, number greater than available tiles')
            return 'not possible' ###########
        if destination=='token won':
            newtoken='pla'+token[0]
            string5 = b[start[0]][start[1]]
            lst = string5.split('-')
            for i in lst:
                if i[:5] == newtoken:
                    if len(i) >5:
                        lst.remove(i)
                        if lst == []:
                            lst.append(i[5:])
                        else:
                            lst[-1] = lst[-1]+(i[5:])
                    else:
                        lst.remove(i)
            new_str = ''
            if len(lst) == 1:
                b[start[0]][start[1]] = lst[0]
            else:
                for i in lst:
                    new_str = new_str + '-' + i
                if new_str[0] == '-':
                    new_str = new_str[1:]
                b[start[0]][start[1]] = new_str 
            # print('what was left',b[start[0]][start[1]])
            return 'token won'
    if destination!=[]: #swapping of token
        col=destination[0][-1] #detecting error here 
        if 's' in destination[0]: #star position
            col='s'+col
            # print('col',col)
            # print('wat is going in',destination[0])
        newtoken='pla'+token[0]
        string5 = b[start[0]][start[1]]
        lst = string5.split('-')
        for i in lst:
            if i[:5] == newtoken:
                if len(i) >5:
                    lst.remove(i)
                    if lst == []:
                        lst.append(i[5:])
                    else:
                        lst[-1] = lst[-1]+(i[5:])
                else:
                    lst.remove(i)
        new_str = ''
        if len(lst) == 1:
            b[start[0]][start[1]] = lst[0]
        else:
            for i in lst:
                new_str = new_str + '-' + i
            if new_str[0] == '-':
                new_str = new_str[1:]
            b[start[0]][start[1]] = new_str 
        # print('what was left',b[start[0]][start[1]])
        if len(destination[0])>4:
            ous=oust(destination[0],destination[2],token)
            if ous==False:
                b[destination[1][0]][destination[1][1]]='pla'+token[0]+'-'+destination[0]
                # print('changed destination',b[destination[1][0]][destination[1][1]])
            else:
                b[destination[1][0]][destination[1][1]]='pla'+token[0]+col
                # print('changed destination',b[destination[1][0]][destination[1][1]])
                return 'rollagain'
        else:
            b[destination[1][0]][destination[1][1]]='pla'+token[0]+destination[0]
            # print('changed destination',b[destination[1][0]][destination[1][1]])
       
        


