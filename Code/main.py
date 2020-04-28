def makeboard():
    board=[]
    file = open('board.txt', 'r')
    f=file.read()
    r=f.splitlines()
    file.close()
    for i in r:
        board.append(i.split(','))
    return board
print(makeboard())