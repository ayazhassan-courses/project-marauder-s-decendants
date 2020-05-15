
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

track[0].append(('p1_1',0))
track[0].append(('p1_2',0))
track[0].append(('p1_3',0))
track[0].append(('p1_4',0))
track[12].append(('p2_1',0))
track[12].append(('p2_2',0))
track[12].append(('p2_3',0))
track[12].append(('p2_4',0))
track[24].append(('p3_1',0))
track[24].append(('p3_2',0))
track[24].append(('p3_3',0))
track[24].append(('p3_4',0))
track[36].append(('p4_1',0))
track[36].append(('p4_2',0))
track[36].append(('p4_3',0))
track[36].append(('p4_4',0))

P1 = {
    'tokens_on_track' : [],
    'tokens_in_field' : [('p1_1',0),('p1_2',0),('p1_3',0),('p1_4',0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : []

}

P2 = {
    'tokens_on_track' : [],
    'tokens_in_field' : [('p2_1',0),('p2_2',0),('p2_3',0),('p2_4',0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : []

}

P3 = {
    'tokens_on_track' : [],
    'tokens_in_field' : [('p3_1',0),('p3_2',0),('p3_3',0),('p3_4',0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : []

}

P4 = {
    'tokens_on_track' : [],
    'tokens_in_field' : [('p4_1',0),('p4_2',0),('p4_3',0),('p4_4',0)],
    'tokens_won' : 0,
    'ousted' : False,
    'home' : []

}

#dice rolls stack
dice_roll = []

Players = [P1,P2,P3,P4]

def move_token(player, spaces):
    if len(player['tokens_on_track']) == 1:
        token,pos = player['tokens_on_track'][0]
        if pos+spaces <= 47:
            temp = pos+spaces
        else:
            temp = (pos+spaces) - 47
        
        # if player == P1 and pos+spaces >= 46:
        #     if player['ousted'] == False:
        #         print('Cannot move inside home column')
        #         track[pos].remove(player['tokens_on_track'][0])
        #         track[temp].append((token,temp))
        #         player['tokens_on_track'][0] = (token,temp)
        #     else:
        #         temp = (pos+spaces) - 46
        #         if temp <= 6:
        #             track[pos].remove(player['tokens_on_track'][0])
        #             player['home'].append((token,temp))
        #             player['tokens_on_track'].pop()
        

    else:
        for i in player['tokens_on_track']:
            print(i[0])
        to_move = input('Which token do you want to move?')
        for i in player['tokens_on_track']:
            if i[0] == to_move:
                token,pos = i
                track[pos].remove(i)
                track[pos+spaces].append((token,pos+spaces))

while True: #while the game is going on
    for player in Players:
        num = 0 #roll dice
        
        while num == 6:
            #roll dice
            num = int(input('enter num'))
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
                    move_token(player,i)
            elif player['tokens_on_track'] == []:
                print('Cannot move')
            elif len(player['tokens_on_track']) >= 1:
                move_token(player,i)
        break
    break


        
# print(track)
