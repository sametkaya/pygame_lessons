#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
class TargetOne():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=1 #x haraket yönü
        self.my=0 #y haraket yönü
        self.life=100
        width=screen.get_width()
        height=screen.get_height()
        self.y=random.randint(10,height-int(height/5))
        self.rectangle=pygame.rect.Rect(width+int(width/20)/2,self.y+int(height/10)/2,int(width/20),int(height/10))

        self.flyImageOrder=0
        self.flyImages=[]
        for i in range(1,11):
            self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Idle ("+str(i)+").png"),(self.rectangle[2],self.rectangle[3])))

        self.explosionImageOrder=-1
        self.explosionImages=[]
        for i in range(1,10):
            self.explosionImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo ("+str(i)+").png"),(self.rectangle[2]*4,self.rectangle[2]*4)))

    def draw(self,screen):
        if self.explosionImageOrder==-1:
            self.flyImageOrder=(self.flyImageOrder+1)%10
            self.rectangle[0]=self.rectangle[0]-self.mx*2
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            #self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder], [self.rectangle[0]-int(self.flyImages[self.flyImageOrder].get_width()/2),self.rectangle[1]-int(self.flyImages[self.flyImageOrder].get_height()/2)])
        else:
            self.explosionImageOrder=(self.explosionImageOrder+1)%9
            #self.rectangle[0]=self.rectangle[0]-self.mx*2
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx= self.rectangle.centerx-self.mx*2

            screen.blit(self.explosionImages[self.explosionImageOrder], [self.rectangle[0]-int(self.explosionImages[self.explosionImageOrder].get_width()/2),self.rectangle[1]-int(self.explosionImages[self.explosionImageOrder].get_height()/2)])
            if self.explosionImageOrder==8:
                self.explosionImageOrder=-1

    def explosion(self):
        if self.life<=0:
            self.explosionImageOrder=0

class Bullet():
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü

        self.rectangle=pygame.rect.Rect(plane.rectangle[0] + int(plane.rectangle[2]/12*8), plane.rectangle[1] +  int(plane.rectangle[3]/12*8), int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
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
        self.flyImageOrder=0
        self.flyImages=[pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (1).png"), (self.rectangle[2], self.rectangle[3])), pygame.transform.scale(pygame.image.load("images/png/Plane/Fly (2).png"), (self.rectangle[2], self.rectangle[3]))]
        self.shootImageOrder=0
        self.shootImages=[pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot (5).png"),(self.rectangle[2],self.rectangle[3]))]

        self.bullets=[]

    def draw(self,screen):

        self.rectangle[0]=self.rectangle[0]+self.mx*2
        self.rectangle[1]=self.rectangle[1]+self.my*2
        self.rectangle.clamp_ip(screen.get_rect())# plane objesini ekran karesi içinde tutar
        if self.shootImageOrder==-1:
            self.flyImageOrder=(self.flyImageOrder+1)%2
            screen.blit(self.flyImages[self.flyImageOrder], self.rectangle)
        else:
            self.shootImageOrder= self.shootImageOrder+1
            screen.blit(self.shootImages[self.shootImageOrder], self.rectangle)
            if self.shootImageOrder==4:
                self.shootImageOrder=-1

        for bullet in self.bullets:
            bullet.draw(screen)
            #rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür. 
            #biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            #ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet) #foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                                            #ancak burada python kabul etti :D
    def fire(self,screen):

        nbullet=Bullet(self)
        nbullet.mx=1
        self.bullets.append(nbullet)
        #her ateş edilişinde bir ateş edilme animasyonu devreye girmelidir
        #bu işlem farklı yollarla yapılabilir
        # burada yaprığımız normalde -1 olan shoot değerini 0  yapıyoruz ve nesnenin çizim fonksiyonunda bir if yapısıyla bu durumu kontrol ediyoruz.
        self.shootImageOrder=0


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
gameTarget1=TargetOne(gameDisplay)
x=0
while not crashed:
    #arkaplan resmini scroll şekilde ilerletmek için
    #çizilen resmin x ekseni azalarak devam edecek şekilde çizdiriyoruz
    gameDisplay.blit(backGroundImage,(x,0))
    x=x-1
    #daha sonra aynı resmi ekranın sonunda tekrar çizdiriyoruz.
    gameDisplay.blit(backGroundImage,(gameDisplay.get_width()+x,0))
    #resim dönüşünde x değerini sıfırlıyoruz
    if gameDisplay.get_width() == -x:
        x=0
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
                gamePlane.fire(gameDisplay)
                gameTarget1.explosion()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                gamePlane.my=0
            if event.key == pygame.K_DOWN:
                gamePlane.my=0
            if event.key == pygame.K_LEFT:
                gamePlane.mx=0
            if event.key == pygame.K_RIGHT:
                gamePlane.mx=0

    gamePlane.draw(gameDisplay)
    gameTarget1.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

