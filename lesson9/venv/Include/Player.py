import pygame
import sys
from pTimer import pTimer
from GameObject import GameObject

class Player(GameObject,pygame.sprite.Sprite):
    def __init__(self,screen):
        GameObject.__init__(self,screen,100,150,[50,screen.get_height()-150])
        self.imagesIdle=[]
        for i in range(9):
            self.imagesIdle.append(pygame.transform.scale(pygame.image.load("images/player/Idle__00"+str(i)+".png"), (self.width, self.height)))
        self.imagesRight=[]
        for i in range(9):
            self.imagesRight.append(pygame.transform.scale(pygame.image.load("images/player/Run__00"+str(i)+".png"), (self.width, self.height)))

        self.imagesLeft=[]
        for i in range(9):
            self.imagesLeft.append(pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/player/Run__00"+str(i)+".png"), True, False), (self.width, self.height)))
        
        self.imagesThrow=[]
        for i in range(9):
            self.imagesThrow.append(pygame.transform.scale(pygame.image.load("images/player/Throw__00"+str(i)+".png"), (self.width, self.height)))

        se
        self.animationImages=[self.imagesIdle,self.imagesRight,self.imagesLeft,self.imagesThrow]
        
        self.sira=0
        self.animationTime=0.01
        self.animationTimer=pTimer(self.animationTime,self.move)
        self.status=0
        self.mx=0
        self.my=0

    def start(self):
        self.animationTimer.start()
        


    def key_down(self, key):
        self.sira=0
        #self.animationTimer.interval=0.01
        if key==pygame.K_RIGHT:
            self.status=1
            self.mx=10
        if key==pygame.K_LEFT:
            self.status=2
            self.mx=-10
        if key==pygame.K_SPACE:
            self.status=3

            
            
    def key_up(self,key):
        if(self.status!=3):
            self.sira=0
            self.status=0
        self.mx=0
        self.my=0
        #self.animationTimer.interval=0.1
        
    def move(self):
        if(self.status==3 and self.sira==8):
            self.sira=0
            self.status=0
            
        self.sira=(self.sira+1)%9
        self.rectangle[0]= self.rectangle[0]+self.mx
        self.rectangle[1]=self.rectangle[1]+self.my


    def draw(self):
        self.screen.blit(self.animationImages[self.status][self.sira], self.rectangle)
        
        
        
            

