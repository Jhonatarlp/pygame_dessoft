# Importando as bibliotecas necessárias.
import pygame
from pygame.locals import QUIT, KEYDOWN  
from constantes import *
import tela_inicial
from mapa1 import MAPA1
from mapa2 import MAPA2
from classes import Tile, Jogador, Obstaculo  

# Função para inicializar os assets do jogo
def carrega_assets():
    assets = {
        'muro': pygame.image.load(IMG_DIR / 'muro.png').convert_alpha(),
        'ponto': pygame.image.load(IMG_DIR / 'vazio.png').convert_alpha(),
        'vacuo': pygame.image.load(IMG_DIR / 'vazio.png').convert_alpha(),
        'caminho': pygame.image.load(IMG_DIR / 'espinhos.png').convert_alpha(),
        'fim': pygame.image.load(IMG_DIR / 'fim.png').convert_alpha(),
        'jogador': pygame.image.load(IMG_DIR / 'jogador.png').convert_alpha(),  
    }
    # Redimensiona as imagens para o tamanho do tile, se necessário
    for key in assets:
        assets[key] = pygame.transform.scale(assets[key], (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    return assets

# Loop principal do jogo
def game_loop(janela, assets):
    mapa_tiles = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()  

    for linha in range(len(MAPA1)):
        for coluna in range(len(MAPA1[linha])):
            tipo_quadrado = MAPA1[linha][coluna]
            if tipo_quadrado in assets:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna)
                mapa_tiles.add(quadrado)
                # Adiciona ao grupo de obstáculos os muros
                if tipo_quadrado == 'muro':
                    grupo_obstaculos.add(quadrado)

    jogador = Jogador(100, 100, 5, assets['jogador'])  # Posição inicial, velocidade e sprite do jogador
    game_started = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                game_started = True
                if event.key == pygame.K_UP:
                    jogador.direcao = "cima"
                elif event.key == pygame.K_DOWN:
                    jogador.direcao = "baixo"
                elif event.key == pygame.K_LEFT:
                    jogador.direcao = "esquerda"
                elif event.key == pygame.K_RIGHT:
                    jogador.direcao = "direita"

            if event.type == pygame.KEYUP:
                jogador.direcao = None  

        if game_started:
            jogador.movimentar(grupo_obstaculos)  
            janela.fill(PRETO)
            jogador.desenhar(janela)
            mapa_tiles.draw(janela)

        pygame.display.flip()
        clock.tick(FPS)

# Executa o jogo
if __name__ == '__main__':
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    
    assets = carrega_assets()
    
    game_loop(janela, assets)
