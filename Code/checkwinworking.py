import pygame
import data_f
import mutual
from mutual import * 
def texto(text, font): #button text
    textS = font.render(text, True, data_f.black)
    return textS, textS.get_rect()
def game():
    running=True
    end=False
    start=(True,False)
    while running:
        for event in pygame.event.get(): #to quit the game
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if start==(True,False):
                    xp,yp,wp,hp=(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50
                    xq,yq,wq,hq=(data_f.screenwidth/2)+50,(data_f.screenheight/2)+50,150,50
                    if mouse[0]>xp and mouse[0]<xp+wp and mouse[1]>yp and mouse[1]<yp+hp:
                        start=(True,True)
                    elif mouse[0]>xq and mouse[0]<xq+wq and mouse[1]>yq and mouse[1]<yq+hq:
                        pygame.quit()
                print('hello')
                end=True
                x,y,w,h=(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50
                if end==True:
                    if mouse[0]>x and mouse[0]<x+w and mouse[1]>y and mouse[1]<y+h:
                        end=False
                        game()
        if start==(True,False):
            screen.fill((255,255,255))
            title = pygame.font.Font(data_f.titlefont,data_f.titlefsize)
            title_text, title_textbox = texto(data_f.title, title)
            title_textbox.center = ((data_f.screenwidth/2),(data_f.screenheight/2))
            screen.blit(title_text, title_textbox) 
            p, p2=button('Play',(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50,data_f.boardgreen,screen, 'menu')
            q, q2=button('Quit',(data_f.screenwidth/2)+50,(data_f.screenheight/2)+50,150,50,data_f.boardred,screen, 'menu')
            pygame.display.update()
        elif end==True:
            screen.fill((0,0,0))
            title = pygame.font.Font(data_f.titlefont,data_f.titlefsize)
            title_text, title_textbox = texto('Won!', title)
            title_textbox.center = ((data_f.screenwidth/2),(data_f.screenheight/2))
            screen.blit(title_text, title_textbox) 
            p, p2=button('Play Again',(data_f.screenwidth/2)-250,(data_f.screenheight/2)+50,150,50,data_f.boardgreen,screen, 'menu')
            # print(pygame.mouse.get_pos())
            if p==True and p2 == False:
                end=False
            q, q2=button('Quit',(data_f.screenwidth/2)+50,(data_f.screenheight/2)+50,150,50,data_f.boardred,screen, 'menu')
            if q==True and q2 == False:
                pygame.quit()
            pygame.display.update()
        else:
            screen.fill(data_f.screencolor)
        pygame.display.update()
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
def m():
    # mainmenu needs to be fixed
    # if mainmenu()==True:
    game()
    # else:
    pygame.quit()
if __name__=='__main__':
    m()
