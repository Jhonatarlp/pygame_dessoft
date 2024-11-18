from pathlib import Path
import pygame
from mapas import *

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent / 'assets'
# Dados gerais do jogo.
TITULO = 'Tomb of Foxy'

LARGURA = 1000 # Largura da tela
ALTURA = 800 # Altura da tela
TAMANHO_QUADRADO = 20 # Tamanho de cada quadrado (tile)
#varoiavel para ajuste de velocidade


linha_inicial, coluna_inicial = 30, 15  # Posição inicial em um tile `p`
x_inicial = coluna_inicial *TAMANHO_QUADRADO
y_inicial = linha_inicial *TAMANHO_QUADRADO 

#tela de morte
WIDTH, HEIGHT = 800, 600

clock = pygame.time.Clock()
FPS = 30 
loop_time = 1/FPS
# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

#lista de mapas
lista_mapas = [MAPA1, MAPA2, MAPA3]
mapa = MAPA1