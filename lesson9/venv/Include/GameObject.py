import pygame
import sys

class GameObject():
    def __init__(self,screen,width,height,location=[0,0]):
        self.screen= screen
        self.width=width
        self.height=height
        self.location=location
        self.rectangle=pygame.rect.Rect(self.location[0],self.location[1],self.width,self.height)



    def Draw(self):
        raise NotImplementedError

