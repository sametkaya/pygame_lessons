#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
class Bullet():
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü

        self.rectangle=pygame.rect.Rect(plane.rectangle[0] + plane.rectangle[2], plane.rectangle[1] + int(plane.rectangle[3] / 2), int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (5).png"),(self.rectangle[2],self.rectangle[3]))]
    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%5
        self.rectangle[0]=self.rectangle[0]+self.mx*3
        self.rectangle[1]=self.rectangle[1]+self.my*3
        #self.rectange.clamp_ip(screen.get_rect())
        ##mermi objesini ekran karesi içinden çıkarsa silinir
        ##bunu planeden kontrol edeceğiz.

        screen.blit(self.images[self.imageOrder], self.rectangle)


class Plane():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü
        width=screen.get_width()
        height=screen.get_height()
        self.rectangle=pygame.rect.Rect(10,int(height/2)-int(height/5/2),int(width/5),int(height/5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (2).png"),(self.rectangle[2],self.rectangle[3]))]
        self.bullets=[]

    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%2
        self.rectangle[0]=self.rectangle[0]+self.mx*2
        self.rectangle[1]=self.rectangle[1]+self.my*2
        self.rectangle.clamp_ip(screen.get_rect())# plane objesini ekran karesi içinde tutar

        screen.blit(self.images[self.imageOrder], self.rectangle)
        for bullet in self.bullets:
            bullet.draw(screen)
            #rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür. 
            #biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            #ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet) #foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                                            #ancak burada python kabul etti :D
    def fire(self):

        nbullet=Bullet(self)
        nbullet.mx=1
        self.bullets.append(nbullet)

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
            if event.key == pygame.K_SPACE:
                gamePlane.fire()
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

