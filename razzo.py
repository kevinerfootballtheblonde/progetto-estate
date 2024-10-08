import pygame, sys
from pygame.locals import *

class razzo:
    def __init__(self, screen, pos, size, color,velocity) -> None:
        self.screen=screen
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.size=size
        self.velocity=velocity
        self.pos=pos
    def move(self):
        self.rect.y+=self.velocity
    def draw(self):
        term=pygame.image.load("rocket.png")
        term=pygame.transform.scale(term,(self.rect.width,self.rect.height))
        self.image=pygame.Surface((self.rect.width,self.rect.height))
        self.image.blit(term,(0,0))
        self.screen.blit(self.image,self.rect)