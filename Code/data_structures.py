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
# print (track)
# print(bdata)
#dictionaries for each player
# p1_1 = 0
# p1_2 = 0
# p1_3 = 0
# p1_4 = 0

P1 = {
    'playcolor':'plar',
    'tokens_on_track' : [],
    'tokens_in_field' : [('r1',(1,1),0),('r2',(1,3),0),('r3',(3,1),0),('r4',(3,3),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 0,
    'last' : 46

}

P2 = {
    'playcolor':'plab',
    'tokens_on_track' : [],
    'tokens_in_field' : [('b1',(1,9),0),('b2',(1,11),0),('b3',(3,9),0),('b4',(3,11),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 12,
    'last' : 10

}

P3 = {
    'playcolor':'plag',
    'tokens_on_track' : [],
    'tokens_in_field' : [('g1',(9,9),0),('g2',(9,11),0),('g3',(11,9),0),('g4',(11,11),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 24,
    'last' : 22

}

P4 = {
    'playcolor':'play',
    'tokens_on_track' : [],
    'tokens_in_field' : [('y1',(9,1),0),('y2',(9,3),0),('y3',(11,1),0),('y4',(11,3),0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 36,
    'last' : 34

}

#dice rolls stack
dice_roll = []
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

# def exceeds_track_length(spaces, tile_no):#might need it to shorten the length of move code
#     new_tile = tile_no + spaces
#     if new_tile > 46:
#         return True
#     else:
#         return False

# def new_position(player,pos,spaces): #dont need it as of the moment
#     if player != P1 and pos + spaces > 46: #checking if track list index is exceeded
#         new_pos = (pos+spaces)-46 #bring token to beginning of list again
#     else:
#         new_pos = pos + spaces
#     return new_pos
def removetoken(remtok,trackpos):
    for i in Players:
        print('oust token',remtok)
        print('checking color wth',i['playcolor'][3],remtok[0][0][0])
        if i['playcolor'][3]==remtok[0][0][0]:
            for tokintrack in range(len(i['tokens_on_track'])):
                print('checking track',i['tokens_on_track'][tokintrack][0][0],'to find',remtok[0][0])
                if i['tokens_on_track'][tokintrack][0][0]==remtok[0][0]:
                    i['tokens_on_track'][tokintrack]=((i['tokens_on_track'][tokintrack][0][0],i['tokens_on_track'][tokintrack][0][1],0),i['tokens_on_track'][tokintrack][1],0)
                    sendback=i['tokens_on_track'].pop(tokintrack)
                    i['tokens_in_field'].append(sendback[0])
                    print('sending back to field',sendback[0])
                    col=b[remtok[0][1][0]][remtok[0][1][1]][-1]
                    print('tile color',col)
                    b[remtok[0][1][0]][remtok[0][1][1]]='pla'+remtok[0][0]+col
                    print('field is now',b[remtok[0][1][0]][remtok[0][1][1]])
                    break
            for tra in track:
                if tra[0]==trackpos:
                    print('remove',remtok,'from',tra)
                    tra.remove(remtok)
                    break
def oust(destination,temp,token):
    for i in Players:
        if i['playcolor']==defturn:
            player=i
    if len(temp)>2:
        for i in range(1,len(temp)):
            print('the token we are checking for oust',temp[i][0])
            if temp[i][0][0]==token[0]:
                comingtok=temp[i][0]
                print(comingtok)
                if 's' not in destination:
                    for j in range(1,len(temp)):
                        if temp[j][0][0][0][0]!=comingtok[0][0]:
                            print('this will be ousted (temp[j])',temp[j][0][0][0][0],'by',comingtok[0][0],temp)
                            print(temp[j])
                            removetoken(temp[j],temp[0])
                            player['ousted'] = True
                            return True
    return False
        # if track[new_pos] != []:
            # for i in track[new_pos]:
            #     if i not in player['tokens_on_track']:
def checkhomelane(token,temp):
    for i in data_structures.Players:
        if i['playcolor']==data_structures.defturn:
            player=i
    for i in range(1,len(temp)):
        if temp[i][0][0]==token[0][0]:
            if temp[i][0][2]==46 and player['ousted']==True:
                for tile in track:
                    if tile==temp:
                        player['home'].append(tile.pop(i))
                        return True
    return False
def reachedhome(token):
    for i in data_structures.Players:
        if i['playcolor']==data_structures.defturn:
            player=i
            player['tokens_won']+=1
def plawon(token):
    for i in data_structures.Players:
        if i['playcolor']==data_structures.defturn:
            player=i
            if player['tokens_won']==4:
                print('player '+token[0][0]+' won!')


# def move_token(player, spaces, track):   
#     if len(player['tokens_on_track']) == 1: 
#         full_token = player['tokens_on_track'][0]
#         token,pos,tile_no = player['tokens_on_track'][0] 
#         if not exceeds_track_length(spaces,tile_no):
#             new_pos = new_position(player,pos,spaces)
#             track[pos].remove(full_token)
#             track[new_pos].append((token,new_pos,tile_no+spaces))
#             player['tokens_on_track'].pop()
#             player['tokens_on_track'].append((token,new_pos,tile_no+spaces))
#             oust(player,new_pos,track)
#         else:
#             if player['ousted'] and (pos+spaces)-46 <= 6: #check ousted & available space
#                 player['tokens_on_track'].pop() #pop from tokens_on_track
#                 player['home'].append((token,(pos+spaces)-46,tile_no+spaces)) #append to home
#                 track[pos].remove((token,pos,tile_no))  #remove from track
#             else:
#                 print('Cannot move this token.')
#     else:
#         while True:
#             for i in player['tokens_on_track']:
#                 print(i[0])
#             to_move = input('Which token do you want to move?')
#             for i in player['tokens_on_track']:
#                 if i[0] == to_move:
#                     token,pos,tile_no = i
#                     if not exceeds_track_length(spaces,tile_no):
#                         new_pos = new_position(player,pos,spaces)
#                         track[pos].remove(i)
#                         track[new_pos].append((token,new_pos,tile_no+spaces))
#                         player['tokens_on_track'].remove(i)
#                         player['tokens_on_track'].append((token,new_pos,tile_no+spaces))
#                         oust(player,new_pos,track)
#                         False
#                     else:
#                         if player['ousted'] and (pos+spaces)-46 <= 6: #check ousted & available space
#                             player['tokens_on_track'].pop() #pop from tokens_on_track
#                             player['home'].append((token,(pos+spaces)-46,tile_no+spaces)) #append to home
#                             track[pos].remove((token,pos,tile_no))  #remove from track
#                             False
#                         else:
#                             print('Cannot move this token. Choose another.')




# while True: #while the game is going on
#     for player in Players:
#         print(player['ID'])
#         num = 6 #roll dice
        
#         while num == 6:
#             #roll dice
#             num = int(input('Enter num (1-6):  '))
#             dice_roll.append(num)
        
#         #checking for 3 sixes
#         count = 0
#         for i in dice_roll:
#             if i == 6:
#                 count += 1
#         if count == 3:
#             while 6 in dice_roll:
#                 dice_roll.remove(6)

#         # moving
#         for i in dice_roll:
#             if i == 6 and len(player['tokens_on_track']) == 0:
#                 player['tokens_on_track'].append(player['tokens_in_field'].pop())
#             elif i == 6 and len(player['tokens_on_track']) > 0 and len(player['tokens_in_field']) > 0:
#                 # print(player['tokens_on_track'])
#                 # break
#                 user = input('Take out token or move current token? (out/move) ')
#                 if user == 'out':
#                     player['tokens_on_track'].append(player['tokens_in_field'].pop())
#                 elif user == 'move':
#                     move_token(player,i,track)
#             elif player['tokens_on_track'] == []:
#                 print('Cannot move')
#             elif len(player['tokens_on_track']) >= 1:
#                 move_token(player,i,track)
#             dice_roll.remove(i)
#         print(track)
    

# print(bdata)
