import pygame
import datetime

pygame.init()

naytto = pygame.display.set_mode((640, 480))


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))

    fontti = pygame.font.SysFont("Arial", 24)
    teksti = fontti.render("Moikka!", True, (255, 0, 0))
    naytto.blit(teksti, (100, 50))

    aika = datetime.timedelta

    pygame.display.set_caption(aika)
    pygame.display.flip()
