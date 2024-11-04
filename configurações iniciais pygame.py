import pygame
from pygame.locals import *
from sys import exit 

# Configuração inicial
pygame.init()
largura = 640
altura = 480
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tomb of the Mask")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update
