import pygame
pygame.init()
w=1366
h=768
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
white=(250,250,250)
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)  