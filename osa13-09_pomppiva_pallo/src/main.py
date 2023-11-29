# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

pallo = pygame.image.load("pallo.png")

x = 0
y = 0
vaaka = 4
pysty = 4
kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(pallo, (x, y))
    pygame.display.flip()

    x += vaaka
    y += pysty
    if vaaka > 0 and x+pallo.get_width() >= 640:
        vaaka = -vaaka

    if pysty > 0 and y+pallo.get_height() >= 480:
        pysty = -pysty

    if vaaka < 0 and x <= 0:
        vaaka = -vaaka

    if pysty < 0 and y <= 0:
        pysty = -pysty

    kello.tick(60)
