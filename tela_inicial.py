import pygame
from pygame.locals import *
from sys import exit
from constantes import *
from classes import *

# Inicialização do Pygame
pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
pygame.display.set_caption(constantes.TITULO)
clock = pygame.time.Clock()  # Controle de FPS 
      
# Música de fundo
musica_de_fundo = pygame.mixer.music.load('assets/fundo.mp3')
pygame.mixer.music.play(-1) 



# Texto de start
font = pygame.font.SysFont(None, 50)
text_color = (constantes.BRANCO)
messagem_to_start = "Aperte qualquer botão para iniciar!"
texto = font.render(messagem_to_start, True, text_color)
text_rect = texto.get_rect(center=(constantes.LARGURA // 2, constantes.ALTURA - 45))

# Carregar e redimensionar imagem de fundo
image = pygame.image.load('assets/tomb_of_foxy_inicio.png').convert()
image = pygame.transform.scale(image, (constantes.LARGURA, constantes.ALTURA)) 
# Inicializar o jogador
jogador_o = Jogador(100, 100, 5)  # Posição inicial e velocidade do jogador   
                                                           
# Variável de controle do jogo
game = True
game_started = False  # Controla se o jogo começou

# #movimentação do personagem 
while game:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # Iniciar o jogo ao pressionar qualquer tecla
        if event.type == KEYDOWN:
            game_started = True
            if event.key == pygame.K_LEFT:
                jogador_o.direcao = "esquerda"
            elif event.key == pygame.K_RIGHT:
                jogador_o.direcao = "direita"
            elif event.key == pygame.K_UP:
                jogador_o.direcao = "cima"
            elif event.key == pygame.K_DOWN:
                jogador_o.direcao = "baixo"
        # Para o jogador quando a tecla é solta
        if event.type == KEYUP:
            jogador_o.direcao = None

    # Desenhar a tela de início ou o jogo
    if not game_started:
        screen.blit(image, (0, 0))  # Desenhar a imagem de fundo
        screen.blit(texto, text_rect)  # Desenhar o texto de início
    else:
        screen.fill(constantes.PRETO)  # Limpa a tela para desenhar o jogo
        
        # Atualizar a movimentação e desenhar o jogador
        jogador_o.movimentar()
        jogador_o.desenhar(screen)  # Desenha o jogador na tela
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(constantes.FPS)  # Controle de FPS
    
