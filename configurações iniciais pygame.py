import pygame
from pygame.locals import *
from sys import exit 

# Configuração inicial
pygame.init()

musica_de_fundo = pygame.mixer.music.load('fundo.mp3')
pygame.mixer.music.play(-1)
largura = 1200
altura = 800
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tomb of the Mask")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update
