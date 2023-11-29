# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
asteroid = pygame.image.load("kivi.png")
x = (640-robo.get_width())/2
y = 480-robo.get_height()
nopeus = 3
pisteet = 0
fontti = pygame.font.SysFont("Arial", 24)
teksti = fontti.render(f"Pisteet: {pisteet}", True, (255, 0, 0))
the_end = fontti.render(
    f"PELI LOPPU!", True, (255, 0, 0))
kello = pygame.time.Clock()
oikealle = False
vasemmalle = False
# lisätään listaan 20 robotin lähtökoordinaatit ja arvotaan suunta mihin asteroidi lähtee laskeutuddutaan
asteroids = []
for i in range(20):
    asteroids.append([random.randint(0, 640-robo.get_width()),
                      random.randint(-6000, -200)])


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))
    teksti = fontti.render(f"Pisteet: {pisteet}", True, (255, 0, 0))
    naytto.blit(teksti, (500, 10))
    naytto.blit(robo, (x, y))

    for asteroidi in asteroids:
        naytto.blit(asteroid, (asteroidi[0], asteroidi[1]))

        if asteroidi[1]+asteroid.get_height() <= 480:
            asteroidi[1] += nopeus
        if asteroidi[1]+asteroid.get_height() >= y:

            if asteroidi[0]+asteroid.get_width() >= x and asteroidi[0] <= x+robo.get_width():
                asteroidi[1] = -2000
                pisteet += 1
        if asteroidi[1]+asteroid.get_height() >= 480:

            naytto.fill((0, 0, 0))
            naytto.blit(the_end, (640/3, 480/2))

    if oikealle:
        x += 5
    if vasemmalle:
        x -= 5
    pygame.display.flip()

    kello.tick(60)
