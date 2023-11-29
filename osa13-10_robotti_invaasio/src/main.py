# TEE RATKAISUSI TÄHÄN:
import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

nopeus = 5

kello = pygame.time.Clock()

# lisätään listaan 20 robotin lähtökoordinaatit ja arvotaan suunta mihin robotti lähtee laskeutuddutaan
robots = []
for i in range(20):
    robots.append([random.randint(0, 640-robo.get_width()),
                  random.randint(-6000, -200), random.randint(0, 1)])


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    for robotti in robots:
        naytto.blit(robo, (robotti[0], robotti[1]))

        if robotti[1]+robo.get_height() <= 480:
            robotti[1] += nopeus
        if robotti[1]+robo.get_height() >= 480:
            if robotti[2] == 1:
                robotti[0] += nopeus
            if robotti[2] == 0:
                robotti[0] -= nopeus

    pygame.display.flip()

    kello.tick(60)
