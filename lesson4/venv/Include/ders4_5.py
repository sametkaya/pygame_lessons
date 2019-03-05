#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
class Plane():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü
        width=screen.get_width()
        height=screen.get_height()
        self.rectange=pygame.rect.Rect(10,int(height/2)-int(height/5/2),int(width/5),int(height/5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (1).png"),(self.rectange[2],self.rectange[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (2).png"),(self.rectange[2],self.rectange[3]))]





    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%2
        self.rectange[0]=self.rectange[0]+self.mx*2
        self.rectange[1]=self.rectange[1]+self.my*2
        self.rectange.clamp_ip(screen.get_rect())# plane objesini ekran karesi içinde tutar

        screen.blit(self.images[self.imageOrder], self.rectange)


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
x=0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gamePlane.my=-1
            if event.key == pygame.K_DOWN:
                gamePlane.my=1
            if event.key == pygame.K_LEFT:
                gamePlane.mx=-1
            if event.key == pygame.K_RIGHT:
                gamePlane.mx=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                gamePlane.my=0
            if event.key == pygame.K_DOWN:
                gamePlane.my=0
            if event.key == pygame.K_LEFT:
                gamePlane.mx=0
            if event.key == pygame.K_RIGHT:
                gamePlane.mx=0
    #arkaplan resmini scroll şekilde ilerletmek için
    #çizilen resmin x ekseni azalarak devam edecek şekilde çizdiriyoruz
    gameDisplay.blit(backGroundImage,(x,0))
    x=x-1
    #daha sonra aynı resmi ekranın sonunda tekrar çizdiriyoruz.
    gameDisplay.blit(backGroundImage,(gameDisplay.get_width()+x,0))
    #resim dönüşünde x değerini sıfırlıyoruz
    if gameDisplay.get_width() == -x:
        x=0
    gamePlane.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

