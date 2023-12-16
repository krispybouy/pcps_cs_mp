import pygame
pygame.init()
w=1366
h=768
dice1=pygame.image.load("dice1.png")
dice2=pygame.image.load("dice2.png")
dice3=pygame.image.load("dice3.png")
dice4=pygame.image.load("dice4.png")
dice5=pygame.image.load("dice5.png")
dice6=pygame.image.load("dice6.png")
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)

def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        GD.blit(a,(300,500))
        pygame.display.update()