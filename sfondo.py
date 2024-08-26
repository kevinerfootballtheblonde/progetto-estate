import pygame, sys
from pygame.locals import *

class sfondo:
    def __init__(self, screen, pos, size, color) -> None:
        self.screen=screen
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.size=size
        self.pos=pos
    def move(self):
        self.rect.y+=5
    def draw(self):
        term=pygame.image.load("space.png")
        term=pygame.transform.scale(term,(self.rect.width,self.rect.height))
        self.image=pygame.Surface((self.rect.width,self.rect.height))
        self.image.blit(term,(0,0))
        self.screen.blit(self.image,self.rect)