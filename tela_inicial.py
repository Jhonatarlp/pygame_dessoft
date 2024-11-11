import pygame
from constantes import *

# Inicializa o Pygame e cria a janela
pygame.init()
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

# Carregar e redimensionar a imagem de fundo
imagem_fundo = pygame.image.load(IMG_DIR / 'tomb_of_foxy_inicio.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

# Texto de start
font = pygame.font.SysFont(None, 50)
text_color = BRANCO
mensagem = "Aperte qualquer botão para iniciar!"
texto = font.render(mensagem, True, text_color)
text_rect = texto.get_rect(center=(LARGURA // 2, ALTURA - 45))

# Desenhar a imagem de fundo e o texto
janela.blit(imagem_fundo, (0, 0))
janela.blit(texto, text_rect)

# Atualiza a tela para mostrar a tela inicial
pygame.display.flip()

# Aguarda um evento de tecla para continuar
esperando = True
while esperando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esperando = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            esperando = False
