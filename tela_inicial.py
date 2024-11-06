import pygame
from pygame.locals import *
from sys import exit 
from os import path
import constantes
from classes import *
import classes

# Inicialização do Pygame
pygame.init()

# Música de fundo
musica_de_fundo = pygame.mixer.music.load('assets/fundo.mp3')
pygame.mixer.music.play(-1) 

# Configuração da tela
screen = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
pygame.display.set_caption(constantes.TITULO)

# Texto de start
font = pygame.font.SysFont(None, 50)
text_color = (constantes.BRANCO)
messagem_to_start = "Aperte qualquer botão para iniciar!"

texto = font.render(messagem_to_start, True, text_color)
text_rect = texto.get_rect(center=(constantes.LARGURA // 2, constantes.ALTURA - 45))

# Carregar e redimensionar imagem de fundo
image = pygame.image.load('assets/tomb_of_foxy_inicio.png').convert()
image = pygame.transform.scale(image, (constantes.LARGURA, constantes.ALTURA)) 

# Loop principal do jogo
game = True
while game:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN():
            if event.key == pygame.K_LEFT:
                movimentacao = Jogador.movimentar("esquerda")
            elif event.key == pygame.K_RIGHT:
                movimentacao = Jogador.movimentar("direita")
            elif event.key == pygame.K_UP:
                movimentacao = Jogador.movimentar("cima")
            elif event.key == pygame.K_DOWN:
                movimentacao = Jogador.movimentar("baixo")
    # Desenhar a imagem de fundo
    screen.blit(image, (0, 0)) 

    # Desenhar o texto de início
    screen.blit(texto, text_rect) 

    # Atualizar a tela
    pygame.display.update()

#movimentação do personagem 
