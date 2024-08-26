import pygame, sys
from pygame.locals import *
from astronave import astronave
from razzo import razzo
from random import randint
from sfondo import sfondo
import os
os.system("cls")
pygame.init()
dimensionifinestra=(1100,600)
screen=pygame.display.set_mode(dimensionifinestra,0,32)
pygame.display.set_caption("pygame")
clock=pygame.time.Clock()
fps=120
bianco=(0,0,0)
size=(100,100)
pos=(dimensionifinestra[0]/2-(size[0]/1.5),dimensionifinestra[1]-size[1]-120)
ship=astronave(screen,pos,size,bianco)
array=[]
sfondo1=sfondo(screen,(0,0),(1100,600),bianco)
sfondo2=sfondo(screen,(0,601),(1100,600),bianco)
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    for rocket in array:       
        if ship.rect.colliderect(rocket.rect):
            pygame.quit()
            sys.exit()
    key=pygame.key.get_pressed()
    if key[K_LEFT]:
        ship.moveleft(10)
    if key[K_RIGHT]:
        ship.moveright(10)
    
    cond=randint(1,12)
    if(cond==1):
        rand=randint(10,1090)
        posr=(rand,-150)
        rocket=razzo(screen,posr,(30,150),bianco,randint(5,15))
        array.append(rocket)
    for rocket in array:
        if rocket.pos[1]>=800:
            array.remove(rocket)
        else:
            rocket.move()
    if(sfondo1.rect.y>=601):
    
        sfondo1.rect.y=-600
    if(sfondo2.rect.y>=601):
    
        sfondo2.rect.y=-600

    sfondo1.move()
    sfondo2.move()
    sfondo1.draw()
    sfondo2.draw()
    ship.draw()
    for rocket in array:
        rocket.draw()
    pygame.display.flip()
    clock.tick(fps)