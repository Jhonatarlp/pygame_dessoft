import pygame
from pygame.locals import *
from sys import exit 
from os import path

# Inicialização do Pygame
pygame.init()

# Música de fundo
musica_de_fundo = pygame.mixer.music.load('assets/fundo.mp3')
pygame.mixer.music.play(-1) 

# Configuração da tela
largura = 1200
altura = 800
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tomb of the Mask")

# Texto de start
font = pygame.font.SysFont(None, 22)
text_color = (255, 255, 255)
messagem_to_start = "Aperte qualquer botão para iniciar!"

texto = font.render(messagem_to_start, True, text_color)
text_rect = texto.get_rect(center=(largura // 2, altura - 203))

# Carregar e redimensionar imagem de fundo
image = pygame.image.load('assets/tomb_of_foxy_inicio.png').convert()
image = pygame.transform.scale(image, (largura, altura)) 

# Loop principal do jogo
game = True
while game:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:  
            game = False  

    # Desenhar a imagem de fundo
    screen.blit(image, (0, 0)) 

    # Desenhar o texto de início
    screen.blit(texto, text_rect) 

    # Atualizar a tela
    pygame.display.update()
