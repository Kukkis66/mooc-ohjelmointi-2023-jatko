# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()
naytto.fill((0, 0, 0))

rivi = 1

for x in range(10):
    naytto.blit(robo, (leveys + (x * leveys/1.25), korkeus))
    naytto.blit(robo, (leveys * 1.25 + (x * leveys/1.25), korkeus * 1.25))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
