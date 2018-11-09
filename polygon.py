import pygame, sys, time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((400, 300), 32, 32)
pygame.display.set_caption("Shape")
WHITE = (255, 255, 255)
GREEN = (  0, 255,   255)

window.fill(WHITE)
pygame.draw.polygon(window, GREEN, ((146, 10), (236, 277), (56, 277)))

# Game logic
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()