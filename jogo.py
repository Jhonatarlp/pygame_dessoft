# Importando as bibliotecas necessárias.
import pygame
from pygame.locals import QUIT, KEYDOWN  
from constantes import *
import tela_inicial
from mapa1 import MAPA1
from mapa2 import MAPA2
from mapa3 import MAPA3
from mapa1  import m, p, v, c, f
from classes import *
import constantes 

# Função para inicializar os assets do jogo
def carrega_assets():
    assets = {
        'muro': pygame.image.load(IMG_DIR / 'muro.png').convert_alpha(),
        'ponto': pygame.image.load(IMG_DIR / 'ponto_com_caminho.png').convert_alpha(),
        'vacuo': pygame.image.load(IMG_DIR / 'vacuo.png').convert_alpha(),
        'caminho': pygame.image.load(IMG_DIR / 'caminho.png').convert_alpha(),
        'fim': pygame.image.load(IMG_DIR / 'fim1.png').convert_alpha(),
        'espinho': pygame.image.load(IMG_DIR / 'espinhos.png').convert_alpha(),
        'atirador': pygame.image.load(IMG_DIR / 'atirador_tiro.png').convert_alpha(),
        # 'jogador': pygame.image.load(IMG_DIR / 'foxy1.png').convert_alpha(),  
    }
    # Redimensiona as imagens para o tamanho do tile
    for key in assets:
        assets[key] = pygame.transform.scale(assets[key], (TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    foxy_anim = []
    for i in range(1,5):
        filename = f'foxy{i}.png'
        img =  pygame.image.load(IMG_DIR / filename).convert_alpha()
        img = pygame.transform.scale(img, (20, 20))  # Redimensiona 
        foxy_anim.append(img)
    assets['anim foxy'] = foxy_anim

    bolinha = 'bolinha.PNG'
    img =  pygame.image.load(IMG_DIR / bolinha).convert_alpha()
    img = pygame.transform.scale(img, (20, 20))  # Redimensiona 
    assets['bolinha'] = img

    return assets

timer = 0
# Loop principal do jogo
def game_loop(janela, assets):
    global timer
    mapa_tiles = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()
    grupo_espinhos = pygame.sprite.Group()

    for linha in range(len(MAPA1)):
        for coluna in range(len(MAPA1[linha])):
            tipo_quadrado = MAPA1[linha][coluna]
            if tipo_quadrado in assets:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna, tipo_quadrado)
                mapa_tiles.add(quadrado)
                if tipo_quadrado == 'muro': 
                    grupo_obstaculos.add(quadrado)
                elif tipo_quadrado == 'espinho':
                    espinho = Espinho(coluna * constantes.TAMANHO_QUADRADO, linha * constantes.TAMANHO_QUADRADO)
                    grupo_espinhos.add(espinho)

    jogador = Jogador(x_inicial, y_inicial, 20, assets)
    #game_started = True 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                #print(f"Tecla pressionada: {event.key}")  # Adicione esta linha para verificar o teclado
                
                if jogador.direcao == 'parado': 
                    if event.key == pygame.K_UP:
                        jogador.direcao = "cima"
                    elif event.key == pygame.K_DOWN:
                        jogador.direcao = "baixo"
                    elif event.key == pygame.K_LEFT:
                        jogador.direcao = "esquerda"
                    elif event.key == pygame.K_RIGHT:
                        jogador.direcao = "direita"
        timer += loop_time
        texto_tempo = f"Tempo: {timer:.2f} segundos"
        imagem_texto = pygame.font.Font(None, 20).render(texto_tempo, True, (255, 255, 255))  # T exto em branco
        text_rect_TEMP = imagem_texto.get_rect(center=(LARGURA // 2, ALTURA - 45))

        #desenha mapa e jogador e espinho
        #if game_started:
        jogador.movimentar(grupo_obstaculos)  ####obs###
        variavel = jogador.verificar_colisao_espinho(grupo_espinhos) ###obs###
        if variavel:
            jogador.direcao = 'parado'
        if jogador.vida == 0:
            exit()

        janela.fill(PRETO)
        mapa_tiles.draw(janela) 
        jogador.desenhar(janela)              
        janela.blit(imagem_texto, text_rect_TEMP)

        pygame.display.flip()
        clock.tick(FPS)


# Executa o jogo
if __name__ == '__main__':
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    
    assets = carrega_assets()
    
    game_loop(janela, assets)
