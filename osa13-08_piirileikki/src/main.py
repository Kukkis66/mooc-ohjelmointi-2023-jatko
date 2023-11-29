# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

kulma = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    vali = 360 / 10

    x0 = 320+math.cos(kulma+vali+vali+vali+vali+vali+vali +
                      vali+vali+vali+vali)*100-robo.get_width()/2
    y0 = 240+math.sin(kulma+vali+vali+vali+vali+vali+vali +
                      vali+vali+vali+vali)*100-robo.get_height()/2
    x1 = 320+math.cos(kulma+vali)*100-robo.get_width()/2
    y1 = 240+math.sin(kulma+vali)*100-robo.get_height()/2
    x2 = 320+math.cos(kulma+vali+vali)*100-robo.get_width()/2
    y2 = 240+math.sin(kulma+vali+vali)*100-robo.get_height()/2
    x3 = 320+math.cos(kulma+vali+vali+vali)*100-robo.get_width()/2
    y3 = 240+math.sin(kulma+vali+vali+vali)*100-robo.get_height()/2
    x4 = 320+math.cos(kulma+vali+vali+vali+vali)*100-robo.get_width()/2
    y4 = 240+math.sin(kulma+vali+vali+vali+vali)*100-robo.get_height()/2
    x5 = 320+math.cos(kulma+vali+vali+vali+vali+vali)*100-robo.get_width()/2
    y5 = 240+math.sin(kulma+vali+vali+vali+vali+vali)*100-robo.get_height()/2
    x6 = 320+math.cos(kulma+vali+vali+vali+vali+vali+vali) * \
        100-robo.get_width()/2
    y6 = 240+math.sin(kulma+vali+vali+vali+vali+vali+vali) * \
        100-robo.get_height()/2
    x7 = 320+math.cos(kulma+vali+vali+vali+vali+vali +
                      vali+vali)*100-robo.get_width()/2
    y7 = 240+math.sin(kulma+vali+vali+vali+vali+vali +
                      vali+vali)*100-robo.get_height()/2
    x8 = 320+math.cos(kulma+vali+vali+vali+vali+vali +
                      vali+vali+vali)*100-robo.get_width()/2
    y8 = 240+math.sin(kulma+vali+vali+vali+vali+vali+vali +
                      vali+vali)*100-robo.get_height()/2
    x9 = 320+math.cos(kulma+vali+vali+vali+vali+vali+vali +
                      vali+vali+vali)*100-robo.get_width()/2
    y9 = 240+math.sin(kulma+vali+vali+vali+vali+vali+vali +
                      vali+vali+vali)*100-robo.get_height()/2

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x0, y0))
    naytto.blit(robo, (x1, y1))
    naytto.blit(robo, (x2, y2))
    naytto.blit(robo, (x3, y3))
    naytto.blit(robo, (x4, y4))
    naytto.blit(robo, (x5, y5))
    naytto.blit(robo, (x6, y6))
    naytto.blit(robo, (x7, y7))
    naytto.blit(robo, (x8, y8))
    naytto.blit(robo, (x9, y9))
    pygame.display.flip()

    kulma += 0.01
    kello.tick(60)
