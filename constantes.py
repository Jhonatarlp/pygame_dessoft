from pathlib import Path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent / 'assets'
# Dados gerais do jogo.
TITULO = 'Tomb of Foxy'
<<<<<<< Updated upstream
LARGURA = 1000 # Largura da tela
ALTURA = 800 # Altura da tela
TAMANHO_QUADRADO = 20 # Tamanho de cada quadrado (tile)
#varoiavel para ajuste de velocidade

#tela de morte
WIDTH, HEIGHT = 800, 600
=======
LARGURA = 1000  # Largura da tela
ALTURA = 700  # Altura da tela
TAMANHO_QUADRADO = 20  # Tamanho de cada quadrado (tile)
>>>>>>> Stashed changes

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
# Os underscores no final são apenas para manter todas as variáveis com o mesmo tamanho.
MCBD = 0
MCBE = 1
MCB = 2
MC = 3
MB = 4
E = 5
MTL = 6
V = 7