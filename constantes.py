from pathlib import Path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent / 'assets'

# Dados gerais do jogo.
TITULO = 'Tomb of Foxy'
LARGURA = 1000  # Largura da tela
ALTURA = 700  # Altura da tela
TAMANHO_QUADRADO = 40  # Tamanho de cada quadrado (tile)

# Variável para ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define os tipos de tiles
MCBD = 0
MCBE = 1
MCB = 2
MC = 3
MB = 4
E = 5
MTL = 6
V = 7
