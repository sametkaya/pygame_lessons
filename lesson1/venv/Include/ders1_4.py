import pygame #pygame kütüphanesini ekliyoruz
import sys

pygame.init() #tüm pygame modüllerini başlatıyor

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))

pygame.display.set_caption('Gamemaker')

crashed = False

clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz



#pygame kütüphanesinde renkler tuple formatındadır
#renkler rgb (red green blue) formatında yazılır.
#üç anarengin karışım oranına göre diğer renkler ortaya çıkar.
black = (0,0,0)
white = (255, 255,255)
blue =  (0,0,255)
green = (0,255,0)
red =   (255,0,0)
backGroundColor=  (255,255,0)

gameDisplay.fill(backGroundColor) # ekran arkaplan rengi değişimi için
pygame.draw.rect(gameDisplay, black, pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(gameDisplay, white, pygame.Rect(60, 60, 60, 60))
pygame.draw.rect(gameDisplay, blue, pygame.Rect(90, 90, 60, 60))
pygame.draw.rect(gameDisplay, green, pygame.Rect(120, 120, 60, 60))
pygame.draw.rect(gameDisplay, red, pygame.Rect(150, 150, 60, 60))

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
