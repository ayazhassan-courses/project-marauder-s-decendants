import data_f
from mutual import *
def push(lst,s):
    lst.append(s)
def pop(lst):
    return lst.pop()
def top(lst):
    return lst[-1]
def is_empty(lst):
    return len(lst)==0

#creating the game track consisting of a list with 48 sub-lists aka tiles
#does not consist of the home column
bdata=[]
defturn='plar'
board=makeboard()
for i in range(len(board)): #storing token color and coordinates (x,y) in tuple
    t=[]
    for j in range(len(board[0])):
        t.append((board[i][j],(data_f.boardstartx+(i*data_f.boardwidthtiles),data_f.boardstarty+(j*data_f.boardheighttiles))))
    bdata.append(t)

end=False
winner=''
P1 = {
    'playcolor':'plar',
    'tokens_on_track' : [],
    'tokens_in_field' : [('r1',(1,1),0),('r2',(1,3),0),('r3',(3,1),0),('r4',(3,3),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 0,
    'last' : 46,
    'outofhome' : []
}

P2 = {
    'playcolor':'plab',
    'tokens_on_track' : [],
    'tokens_in_field' : [('b1',(1,9),0),('b2',(1,11),0),('b3',(3,9),0),('b4',(3,11),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 12,
    'last' : 10,
    'outofhome' : []
}

P3 = {
    'playcolor':'plag',
    'tokens_on_track' : [],
    'tokens_in_field' : [('g1',(9,9),0),('g2',(9,11),0),('g3',(11,9),0),('g4',(11,11),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 24,
    'last' : 22,
    'outofhome' : []
}

P4 = {
    'playcolor':'play',
    'tokens_on_track' : [],
    'tokens_in_field' : [('y1',(9,1),0),('y2',(9,3),0),('y3',(11,1),0),('y4',(11,3),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 36,
    'last' : 34,
    'outofhome' : []
}

#dice rolls stack
dice_roll = []
dice_roll2 = []
#tile indexes for stops
stops = [(0,'rh'),(7,'b'),(12,'bh'),(19,'g'),(24,'gh'),(31,'y'),(36,'yh'),(43,'r')]
homelanes=[('r',[(6,1),(6,5)]),('b',[(1,6),(5,6)]),('g',[(6,11),(6,7)]),('y',[(11,6),(7,6)])]
winningtile=(6,6)
Players = [P1,P2,P3,P4]

'''
move function:

check number of tokens available to move

if there is only one token on track
move it automatically

If there are more, ask which token to move

for moving:

check if it exceeds track length (diff for each player). If it does, check ousted, number of spaces available for validity of move

if exceeds track list, implement circular queue trick

if not:
update the track
update the player dictionary

oust someone already there unless stop
'''

def removetoken(remtok,trackpos):
    for i in Players:
        # print('oust token',remtok)
        # print('checking color wth',i['playcolor'][3],remtok[0][0][0])
        if i['playcolor'][3]==remtok[0][0][0]:
            for tokintrack in range(len(i['tokens_on_track'])):
                # print('checking track',i['tokens_on_track'][tokintrack][0][0],'to find',remtok[0])
                if i['tokens_on_track'][tokintrack][0][0]==remtok[0]:
                    i['tokens_on_track'][tokintrack]=((i['tokens_on_track'][tokintrack][0][0],i['tokens_on_track'][tokintrack][0][1],0),i['tokens_on_track'][tokintrack][1],0)
                    sendback=i['tokens_on_track'].pop(tokintrack)
                    i['tokens_in_field'].append(sendback[0])
                    # print('sending back to field',sendback[0])
                    col=b[remtok[1][0]][remtok[1][1]][-1]
                    # print('tile color',col)
                    b[remtok[1][0]][remtok[1][1]]='pla'+remtok[0]+col
                    # print('field is now',b[remtok[1][0]][remtok[1][1]])
                    for tra in track:
                        if tra[0]==trackpos:
                            # print('remove',remtok,'from',tra)
                            tra.remove(remtok)
                            return
def oust(destination,temp,token):
    # print('we are going to check oust in this',temp)
    for i in Players:
        if i['playcolor']==defturn:
            player=i
    if len(temp)>2:
        for i in range(1,len(temp)):
            # print('the token we are checking for oust',temp[i][0])
            if temp[i][0][0]==token[0][0]:
                comingtok=temp[i][0]
                # print('this is the killer',comingtok)
                if 's' not in destination:
                    for j in range(1,len(temp)):
                        # print('temp[j][0][0]',temp[j][0][0])
                        if temp[j][0][0]!=comingtok[0][0]:
                            # print('this will be ousted (temp[j])',temp[j][0][0],'by',comingtok[0][0],temp)
                            # print(temp[j])
                            removetoken(temp[j],temp[0])
                            player['ousted'] = True
                            return True
    return False
      
def checkhomelane(token,temp):
    for i in Players:
        if i['playcolor']==defturn:
            player=i
    for i in range(len(temp)): 
        if temp[i][0][0]==token[0][0]:
            if temp[i][0][2]==46 and player['ousted']==True:
                for tile in track:
                    if tile==temp:
                        player['home'].append(tile.pop(i))
                        return True
    return False
def reachedhome(token):
    for i in Players:
        if i['playcolor']==defturn:
            player=i
            player['tokens_won']+=1
def plawon(token):
    for i in Players:
        if i['playcolor']==defturn:
            player=i
            if player['tokens_won']==4:
                # print('player '+token[0][0]+' won!')
                return True
