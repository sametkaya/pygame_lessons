import pygame
import sys
import math
import random
import TargetOne
import Plane
import Bullet
class ChapterOne():
    def __init__(self,screen):
        self.name="Let's Start"
        self.plane= Plane(screen)
        self.targets=[]
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/png/BG.png"),(screen.get_width(), screen.get_height()))
        self.backGroundImageX=0
        self.backGroundImageY=0

    def start(self,screen):
        pass

    def draw(self,screen):
        
