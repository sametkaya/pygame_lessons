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

    def draw(self,screen,mposition):
        self.imageOrder=self.imageOrder%2+1
        self.image=pygame.image.load("images/png/Plane/Fly ("+str(self.imageOrder)+").png")
        self.image= pygame.transform.scale(self.image, (self.rectange[2],self.rectange[3]))
        angle = math.atan2((self.rectange[1]+int(self.rectange[3]/2) - mposition[1]), (mposition[0] - self.rectange[0])) / math.pi


        self.rectange[1]=self.rectange[1]+angle*-10
        self.image = pygame.transform.rotate(self.image, math.degrees(angle))

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
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.blit(backGroundImage,(0,0))
    mouse_position = pygame.mouse.get_pos()
    gamePlane.draw(gameDisplay,mouse_position)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

