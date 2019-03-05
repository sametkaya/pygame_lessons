#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
class Plane():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.imageOrder=0
        width=screen.get_width()
        height=screen.get_height()
        self.rectange=[10,int(height/2)-int(height/5/2),int(width/5),int(height/5)]

    def draw(self,screen,mx,my):
        self.imageOrder=self.imageOrder%2+1
        self.image=pygame.image.load("images/png/Plane/Fly ("+str(self.imageOrder)+").png")
        self.rectange[0]=self.rectange[0]+mx*2
        self.rectange[1]=self.rectange[1]+my*2
        self.image= pygame.transform.scale(self.image, (self.rectange[2],self.rectange[3]))


        screen.blit(self.image, self.rectange)


pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)



clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/png/BG.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))

 #ekranı her framede tekrar çizdiriyoruz
gamePlane=Plane(gameDisplay)
mx=0 #x haraket yönü
my=0 #y haraket yönü
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my=-1
            if event.key == pygame.K_DOWN:
                my=1
            if event.key == pygame.K_LEFT:
                mx=-1
            if event.key == pygame.K_RIGHT:
                mx=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                my=0
            if event.key == pygame.K_DOWN:
                my=0
            if event.key == pygame.K_LEFT:
                mx=0
            if event.key == pygame.K_RIGHT:
                mx=0
    gameDisplay.blit(backGroundImage,(0,0))
    mouse_position = pygame.mouse.get_pos()
    gamePlane.draw(gameDisplay,mx,my)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

