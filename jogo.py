# Importando as bibliotecas necessárias.
import pygame
from pygame.locals import QUIT, KEYDOWN  # Certifique-se de importar QUIT
from constantes import *
import tela_inicial
from mapa1 import MAPA1
from mapa2 import MAPA2
from classes import Tile, Jogador, Obstaculo  

# Função para inicializar os assets do jogo
def carrega_assets():
    assets = {
        'muro': pygame.image.load(IMG_DIR / 'muro.png').convert_alpha(),
        'ponto': pygame.image.load(IMG_DIR / 'ponto_com_caminho.png').convert_alpha(),
        'vacuo': pygame.image.load(IMG_DIR / 'vacuo.png').convert_alpha(),
        'caminho': pygame.image.load(IMG_DIR / 'caminho.png').convert_alpha(),
        'fim': pygame.image.load(IMG_DIR / 'fim1.png').convert_alpha(),
        'inicio': pygame.image.load(IMG_DIR / 'tomb_of_foxy_inicio.png').convert_alpha(),
        'espinho': pygame.image.load(IMG_DIR / 'espinhos.PNG').convert_alpha(),
    }
    # Redimensiona as imagens para o tamanho do tile
    for key in assets:
        assets[key] = pygame.transform.scale(assets[key], (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    return assets

# Loop principal do jogo
def game_loop(janela, assets):
    mapa_tiles = pygame.sprite.Group()
    for linha in range(len(MAPA1)):
        for coluna in range(len(MAPA1[linha])):
            tipo_quadrado = MAPA1[linha][coluna]
            if tipo_quadrado in assets:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna)
                mapa_tiles.add(quadrado)

    jogador = Jogador(100, 100, 5)  # Posição inicial e velocidade
    game_started = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                game_started = True

        # Desenha a tela de início ou o jogo
        if not game_started:
            tela_inicial.tela_inicial(janela)
        else:
            janela.fill(PRETO)
            jogador.desenhar(janela)  # Desenha o jogador
            mapa_tiles.draw(janela)  # Desenha o mapa

        # Atualiza a tela e controla o FPS
        pygame.display.flip()
        clock.tick(FPS)

# Executa o jogo
if __name__ == '__main__':
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    
    assets = carrega_assets()
    
    game_loop(janela, assets)
