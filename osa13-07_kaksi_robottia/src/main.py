# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
x2 = 0
nopeus = 1
nopeus2 = nopeus * 2
kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y + robo.get_height()))
    naytto.blit(robo, (x2, y + 2 * robo.get_height()))

    pygame.display.flip()

    x += nopeus
    x2 += nopeus2

    if nopeus > 0 and x+robo.get_width() >= 640:
        nopeus = -nopeus
    if nopeus2 > 0 and x2+robo.get_width() >= 640:
        nopeus2 = -nopeus2

    if nopeus < 0 and x <= 0:
        nopeus = -nopeus
    if nopeus2 < 0 and x2 <= 0:
        nopeus2 = -nopeus2

    kello.tick(60)
