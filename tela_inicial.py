import pygame
from constantes import *

def tela_inicial(janela):
    # Carregar e redimensionar a imagem de fundo
    imagem_fundo = pygame.image.load(IMG_DIR / 'tomb_of_foxy_inicio.png').convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

    # Desenhar a imagem de fundo e o texto
    janela.blit(imagem_fundo, (0, 0))
    font = pygame.font.SysFont(None, 50)
    mensagem = "Aperte qualquer botão para iniciar!"
    
    texto = font.render(mensagem, True, BRANCO)
    text_rect = texto.get_rect(center=(LARGURA // 2, ALTURA - 45))
    janela.blit(texto, text_rect)
    pygame.display.flip()
