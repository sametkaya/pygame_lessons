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
green = ( 0,255,0)
red =   (255,0,0)


gameDisplay.fill(white) # ekran arkaplan rengi değişimi için

pygame.draw.line(gameDisplay, green, [0,0], [50,30], 1)
##draw.line (ekran,renk, başlangıç_noktası[x,y], bitiş_noktası[x,y], kalınlık) değerleri alır

#pygame.draw.lines(gameDisplay, black, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
##draw.lines (ekran,renk,uçların_birleşme_durumu(closed), [başlangıç_noktası[x,y], bitiş_noktası[x,y]] listesi, kalınlık) değerleri alır
#pygame.draw.lines(gameDisplay, green, True, [[100, 180], [150, 190], [300, 380], [320, 130]], 5)


#pygame.draw.aaline(gameDisplay, red, [0, 50],[50, 80], True)
#draw.aaline antialiased cizgi cizer. (ekran,renk, başlangıç_noktası[x,y], bitiş_noktası[x,y], yumuşatma_durumu) değerleri alır
#antialiasing cizgilerin bulur geçişler yapmasını sağlar, böylece görüntüler keskin değil, yumuşak hatlara sahip olur. ancak bu durum işlem yükünü artırır.
#kalınlık ayarı yok :(

#pygame.draw.aalines(gameDisplay, black, False,  [[100, 180], [150, 190], [300, 380], [320, 130]],True)
#draw.aalines antialiased cizgiler cizer. (ekran,renk, uçların_birleşme_durumu(closed), [başlangıç_noktası[x,y], bitiş_noktası[x,y]] listesi, yumuşatma_durumu) değerleri alır

#pygame.draw.rect(gameDisplay, black, [75, 10, 50, 20], 1)
#draw.rect dikdörtgen cizer. (ekran, renk, [x, y, genişlik, yükseklik], çizgi_kalınlığı)

#ygame.draw.rect(gameDisplay, black, [150, 10, 50, 20])
#draw.rect çizgi_kalınlığı parametresi girilmezse içi dolu dikdörtgen cizer. (ekran, renk, [x, y, genişlik, yükseklik])

pygame.draw.ellipse(gameDisplay, red, [225, 10, 50, 20], 2)
#draw.ellipse elips cizer. (ekran, renk, [x, y, genişlik, yükseklik], çizgi_kalınlığı)

# pygame.draw.ellipse(gameDisplay, red, [300, 10, 50, 20])
#draw.ellipse çizgi_kalınlığı parametresi girilmezse içi dolu elips çizer. (ekran, renk, [x, y, genişlik, yükseklik])

#pygame.draw.circle(gameDisplay, blue, [60, 250], 40,3)
#draw.circle halka cizer. (ekran, renk, [x, y], çap, çizgi_kalınlığı)

#pygame.draw.circle(gameDisplay, blue, [160, 350], 40)
#draw.circle içidolu halka cizer. (ekran, renk, [x, y], çap)


#pygame.draw.polygon(gameDisplay, black, [[100, 100], [0, 200], [200, 200], [350, 250]], 5)
#draw.polygon verilen nokları birleşren bir poligon çizer.(ekran,renk,[[x1,y1],[x2,y2],...], kalınlık)

#pygame.draw.polygon(gameDisplay, black, [[100, 100], [0, 200], [200, 200], [350, 250]])
#draw.polygon verilen nokları birleşren içi dolu bir poligon çizer.(ekran,renk,[[x1,y1],[x2,y2],...])


pygame.draw.arc(gameDisplay, black,[210, 75, 150, 125], 0, 3/2, 2)
pygame.draw.arc(gameDisplay, green,[210, 75, 150, 125], 3/2, 3, 2)
pygame.draw.arc(gameDisplay, blue, [210, 75, 150, 125], 3,3*3/2, 2)
pygame.draw.arc(gameDisplay, red,  [210, 75, 150, 125], 3*3/2, 2*3, 2)
#draw.arc yay çizer. (ekran, renk, dikdörtgen, başlangıç_açısı, bitiş_açısı, kalınlık)


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
