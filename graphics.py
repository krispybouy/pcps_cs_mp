import pygame
pygame.init()
w=1366
h=768
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("Snakes-and-Ladders-Bigger.jpg")
dice1=pygame.image.load("dice1.png")
dice2=pygame.image.load("dice2.png")
dice3=pygame.image.load("dice3.png")
dice4=pygame.image.load("dice4.png")
dice5=pygame.image.load("dice5.png")
dice6=pygame.image.load("dice6.png")

redgoti=pygame.image.load("redgoti.png")
yellowgoti=pygame.image.load("yellowgoti.png")
greengoti=pygame.image.load("greengoti.png")
bluegoti=pygame.image.load("bluegoti.png")
menubg=pygame.image.load("menu.jpg")
p=pygame.image.load("playbg.jpg")
intbg=pygame.image.load("intropic.png")
intbg2=pygame.image.load("intropic2.jpg")
intbg3=pygame.image.load("intropic3.jpg")
intbg4=pygame.image.load("intropic4.jpg")
intbg5=pygame.image.load("intropic5.jpg")
credits1=pygame.image.load("credits.jpg")

pygame.mixer.music.load("music.wav")
snakesound=pygame.mixer.Sound("snake.wav")
win=pygame.mixer.Sound("Win.wav")
lose=pygame.mixer.Sound("lose.wav")
ladder=pygame.mixer.Sound("ladder.wav")