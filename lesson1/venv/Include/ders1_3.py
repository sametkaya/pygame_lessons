import pygame #pygame kütüphanesini ekliyoruz
import sys

pygame.init() #tüm pygame modüllerini başlatıyor

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))

pygame.display.set_caption('Gamemaker')
crashed = False

clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
#pygame.draw verilen ekrana çizim yapar
#rect içine ekran, renk, pygame.Rect alır.
#pygame.Rect içine x, y, genişlik, yükseklik bilgilerini alır.

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
