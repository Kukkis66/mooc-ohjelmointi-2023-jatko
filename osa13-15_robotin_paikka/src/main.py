# TEE RATKAISUSI TÄHÄN:
import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x1 = random.randint(0, 640-robo.get_width())
y1 = random.randint(0, 480-robo.get_height())

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x = tapahtuma.pos[0]
            y = tapahtuma.pos[1]

            if x >= x1 and x <= x1+robo.get_width():
                if y >= y1 and y <= y1+robo.get_height():
                    x1 = random.randint(0, 640-robo.get_width())
                    y1 = random.randint(0, 480-robo.get_height())

            naytto.fill((0, 0, 0))
            naytto.blit(robo, (x1, y1))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit()
