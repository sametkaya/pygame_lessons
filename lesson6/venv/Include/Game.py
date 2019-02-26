#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random


pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)



clock = pygame.time.Clock()

 #ekranı her framede tekrar çizdiriyoruz
gamePlane=Plane(gameDisplay)
gameTargets=[]
def generateTarget():
    gameTargets.append(TargetOne(gameDisplay))
def drawTargets():
    for target in gameTargets:
        target.draw(gameDisplay)
        for bullet in gamePlane.bullets:
            #eğer eşleşme varsa
            if target.rectangle.colliderect(bullet.rectangle):
                #target hit almış demektir.
                target.hit()
                #mermi kaybolmalı
                gamePlane.bullets.remove(bullet)

        # if not gameDisplay.get_rect().contains(target.rectangle):
        #     gameTargets.remove(target)



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
            if event.key==pygame.K_a:
                generateTarget()
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
    drawTargets()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

