# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
vaaka = 1
pysty = 0
kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    x += vaaka
    y += pysty
    if vaaka > 0 and x+robo.get_width() >= 640:
        vaaka = 0
        pysty = 1
    if pysty > 0 and y+robo.get_height() >= 480:
        pysty = 0
        vaaka -= 1
    if vaaka < 0 and x <= 0:
        vaaka = 0
        pysty -= 1
    if pysty < 1 and y <= 0:
        pysty = 0
        vaaka = 1

    kello.tick(60)
