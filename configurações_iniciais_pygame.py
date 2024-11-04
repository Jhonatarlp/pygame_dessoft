import pygame
from pygame.locals import *
from sys import exit 

# inicia while do jogo
game = True

# Configuração inicial
pygame.init()

musica_de_fundo = pygame.mixer.music.load('fundo.mp3')
pygame.mixer.music.play(-1)
largura = 1200
altura = 800
screen = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Tomb of the Mask")
# image = pygame.image.load('assets\tomb_of_foxy_inicio.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update
