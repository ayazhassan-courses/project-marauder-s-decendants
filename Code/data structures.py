
#creating the game track consisting of a list with 48 sub-lists aka tiles
#does not consist of the home column
track = []
for i in range(48):
    track.append([])

#dictionaries for each player
# p1_1 = 0
# p1_2 = 0
# p1_3 = 0
# p1_4 = 0

track[0].append(('p1_1',0,0))
track[0].append(('p1_2',0,0))
track[0].append(('p1_3',0,0))
track[0].append(('p1_4',0,0))
track[12].append(('p2_1',0,0))
track[12].append(('p2_2',0,0))
track[12].append(('p2_3',0,0))
track[12].append(('p2_4',0,0))
track[24].append(('p3_1',0,0))
track[24].append(('p3_2',0,0))
track[24].append(('p3_3',0,0))
track[24].append(('p3_4',0,0))
track[36].append(('p4_1',0,0))
track[36].append(('p4_2',0,0))
track[36].append(('p4_3',0,0))
track[36].append(('p4_4',0,0))

P1 = {
    'ID' : 'Player 1',
    'tokens_on_track' : [],
    'tokens_in_field' : [('p1_1',0,0),('p1_2',0,0),('p1_3',0,0),('p1_4',0,0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 0,
    'last' : 46

}

P2 = {
    'ID' : 'Player 2',
    'tokens_on_track' : [],
    'tokens_in_field' : [('p2_1',12,0),('p2_2',12,0),('p2_3',12,0),('p2_4',12,0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 12,
    'last' : 10

}

P3 = {
    'ID' : 'Player 3',
    'tokens_on_track' : [],
    'tokens_in_field' : [('p3_1',24,0),('p3_2',24,0),('p3_3',24,0),('p3_4',24,0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 24,
    'last' : 22

}

P4 = {
    'ID' : 'Player 4',
    'tokens_on_track' : [],
    'tokens_in_field' : [('p4_1',36,0),('p4_2',36,0),('p4_3',36,0),('p4_4',36,0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : [],
    'first' : 36,
    'last' : 34

}

#dice rolls stack
dice_roll = []
#tile indexes for stops
stops = [0,7,12,19,24,31,36,43]

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

def exceeds_track_length(spaces, tile_no):
    new_tile = tile_no + spaces
    if new_tile > 46:
        return True
    else:
        return False

def new_position(player,pos,spaces):
    if player != P1 and pos + spaces > 46: #checking if track list index is exceeded
        new_pos = (pos+spaces)-46 #bring token to beginning of list again
    else:
        new_pos = pos + spaces
    return new_pos

def oust(player,new_pos,track):
    if track[new_pos] != []:
        for i in track[new_pos]:
            if i not in player['tokens_on_track']:
                track[new_pos].remove(i)
                player['ousted'] == True

def move_token(player, spaces, track):   
    if len(player['tokens_on_track']) == 1: 
        full_token = player['tokens_on_track'][0]
        token,pos,tile_no = player['tokens_on_track'][0] 
        if not exceeds_track_length(spaces,tile_no):
            new_pos = new_position(player,pos,spaces)
            track[pos].remove(full_token)
            track[new_pos].append((token,new_pos,tile_no+spaces))
            player['tokens_on_track'].pop()
            player['tokens_on_track'].append((token,new_pos,tile_no+spaces))
            oust(player,new_pos,track)
        else:
            if player['ousted'] and (pos+spaces)-46 <= 6: #check ousted & available space
                player['tokens_on_track'].pop() #pop from tokens_on_track
                player['home'].append((token,(pos+spaces)-46,tile_no+spaces)) #append to home
                track[pos].remove((token,pos,tile_no))  #remove from track
            else:
                print('Cannot move this token.')
    else:
        while True:
            for i in player['tokens_on_track']:
                print(i[0])
            to_move = input('Which token do you want to move?')
            for i in player['tokens_on_track']:
                if i[0] == to_move:
                    token,pos,tile_no = i
                    if not exceeds_track_length(spaces,tile_no):
                        new_pos = new_position(player,pos,spaces)
                        track[pos].remove(i)
                        track[new_pos].append((token,new_pos,tile_no+spaces))
                        player['tokens_on_track'].remove(i)
                        player['tokens_on_track'].append((token,new_pos,tile_no+spaces))
                        oust(player,new_pos,track)
                        False
                    else:
                        if player['ousted'] and (pos+spaces)-46 <= 6: #check ousted & available space
                            player['tokens_on_track'].pop() #pop from tokens_on_track
                            player['home'].append((token,(pos+spaces)-46,tile_no+spaces)) #append to home
                            track[pos].remove((token,pos,tile_no))  #remove from track
                            False
                        else:
                            print('Cannot move this token. Choose another.')




while True: #while the game is going on
    for player in Players:
        print(player['ID'])
        num = 6 #roll dice
        
        while num == 6:
            #roll dice
            num = int(input('Enter num (1-6):  '))
            dice_roll.append(num)
        
        #checking for 3 sixes
        count = 0
        for i in dice_roll:
            if i == 6:
                count += 1
        if count == 3:
            while 6 in dice_roll:
                dice_roll.remove(6)

        # moving
        for i in dice_roll:
            if i == 6 and len(player['tokens_on_track']) == 0:
                player['tokens_on_track'].append(player['tokens_in_field'].pop())
            elif i == 6 and len(player['tokens_on_track']) > 0 and len(player['tokens_in_field']) > 0:
                # print(player['tokens_on_track'])
                # break
                user = input('Take out token or move current token? (out/move) ')
                if user == 'out':
                    player['tokens_on_track'].append(player['tokens_in_field'].pop())
                elif user == 'move':
                    move_token(player,i,track)
            elif player['tokens_on_track'] == []:
                print('Cannot move')
            elif len(player['tokens_on_track']) >= 1:
                move_token(player,i,track)
            dice_roll.remove(i)
        print(track)
    


        

