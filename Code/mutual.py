import pygame
import data_f
def startgame():
    pygame.init()
    screen=pygame.display.set_mode((data_f.screenwidth,data_f.screenheight))
    pygame.display.set_caption(data_f.title)
    Icon=pygame.image.load(data_f.logo)
    pygame.display.set_icon(Icon)
    return screen
def makeboard():
    board=[]
    file = open('board.txt', 'r')
    f=file.read()
    r=f.splitlines()
    file.close()
    for i in r:
        board.append(i.split(','))
    return board
def maketrack():
    t=[]
    file = open('track.txt', 'r')
    f=file.read()
    r=f.splitlines()
    file.close()
    for i in r:
        s=i.split()
        # print(s)
        t.append([(int(s[0]),int(s[1]))])
    return t
def turn(n):
    players=['plar','plab','plag','play']
    return players[n]
    
screen=startgame()
b=makeboard()
track=maketrack()