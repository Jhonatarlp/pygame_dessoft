# Importando as bibliotecas necessárias.
import pygame
from pygame.locals import QUIT, KEYDOWN  
from constantes import *
import tela_inicial
from mapas  import *
from classes import *


# Função para inicializar os assets do jogo
def carrega_assets():
    assets = {
        'muro': pygame.image.load(IMG_DIR / 'muro.png').convert_alpha(),
        'ponto': pygame.image.load(IMG_DIR / 'ponto_com_caminho.png').convert_alpha(),
        'vacuo': pygame.image.load(IMG_DIR / 'vacuo.png').convert_alpha(),
        'fim': pygame.image.load(IMG_DIR / 'fim1.png').convert_alpha(),
        'caminho': pygame.image.load(IMG_DIR / 'caminho.png').convert_alpha(),
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

    fim_anim = []
    for i in range(1,3):
        fim = f'fim{i}.PNG'
        img =  pygame.image.load(IMG_DIR / fim).convert_alpha()
        img = pygame.transform.scale(img, (20, 20))  # Redimensiona 
        fim_anim.append(img)
    assets['fim anim'] = fim_anim

    return assets

timer = 0
# Loop principal do jogo
def carregar_mapa(mapa, assets, largura_tela, altura_tela):
    mapa_tiles = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()
    grupo_moedas = pygame.sprite.Group()
    group_fim = pygame.sprite.Group()
    grupo_espinhos = pygame.sprite.Group()
    grupo_inicios = pygame.sprite.Group()

    # Calcula tamanho do mapa
    altura_mapa = len(mapa) * constantes.TAMANHO_QUADRADO
    largura_mapa = len(mapa[0]) * constantes.TAMANHO_QUADRADO

    # Calcula o deslocamento para centralizar o mapa na tela
    deslocamento_x = (LARGURA - largura_mapa) // 2
    deslocamento_y = (ALTURA - altura_mapa) // 2

    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            tipo_quadrado = mapa[linha][coluna]
            x = coluna * constantes.TAMANHO_QUADRADO
            y = linha * constantes.TAMANHO_QUADRADO

            if tipo_quadrado == 'ponto' or tipo_quadrado == 'inicio':
                quadrado = Tile(assets['caminho'], linha, coluna, tipo_quadrado, deslocamento_x, deslocamento_y)
            else:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna, tipo_quadrado, deslocamento_x, deslocamento_y)
            mapa_tiles.add(quadrado)

            if tipo_quadrado == 'muro': 
                grupo_obstaculos.add(quadrado)
            elif tipo_quadrado == 'ponto':  
                moeda = Moeda(x, y, assets['ponto'], deslocamento_x, deslocamento_y)
                grupo_moedas.add(moeda)
            elif tipo_quadrado == 'espinho':
                espinho = Espinho(x, y, deslocamento_x, deslocamento_y)
                grupo_espinhos.add(espinho)
            elif tipo_quadrado == 'fim':
                fim = Fim(x // constantes.TAMANHO_QUADRADO, y // constantes.TAMANHO_QUADRADO, assets, deslocamento_x, deslocamento_y)
                group_fim.add(fim)
            elif tipo_quadrado == 'inicio':  # Encontra o ponto inicial
                grupo_inicios.add(quadrado)

    return mapa_tiles, grupo_obstaculos, grupo_moedas, grupo_espinhos, group_fim, grupo_inicios


def game_loop(janela, assets, lista_mapas):
    global timer
    index_mapa = 0  # Índice do mapa atual
    
    MAPA_tiles, grupo_obstaculos, grupo_moedas, grupo_espinhos, group_fim, grupo_inicios = carregar_mapa(lista_mapas[index_mapa], assets, constantes.LARGURA, constantes.ALTURA)
    
    start = grupo_inicios.sprites()[0]

    jogador = Jogador(start.rect.x, start.rect.y, 20, assets)
    # Carrega o primeiro mapa
  
    running = True
    moedas_coletadas = 0

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
        jogador.movimentar(grupo_obstaculos)

        # Dentro do loop do jogo, logo após movimentar o jogador
        if jogador.verificar_colisao_moeda(grupo_moedas):  # Passa os grupos
            moedas_coletadas += 1  # Incrementa o contador de moedas coletadas
        if jogador.verificar_colisao_espinho(grupo_espinhos):
            jogador.direcao = 'parado'

        # Verifica vida do jogador
        if jogador.vida == 0:
            tela_game_over(janela)
            return  # Sai do loop do jogo
        
        # Verifica colisão com o ponto final
        if pygame.sprite.spritecollide(jogador, group_fim, False):
            index_mapa += 1
            if index_mapa < len(lista_mapas):
                # Carrega o próximo mapa
                MAPA_tiles, grupo_obstaculos, grupo_moedas, grupo_espinhos, group_fim, grupo_inicios = carregar_mapa(lista_mapas[index_mapa], assets, constantes.LARGURA, constantes.ALTURA)
  
                start = grupo_inicios.sprites()[0]
                jogador.posicao = pygame.Vector2(start.rect.x, start.rect.y) 
                jogador.rect.topleft = (jogador.posicao.x, jogador.posicao.y)
            else:
                tela_game_over(janela)
                return
            

    
        
        janela.fill(PRETO)
        MAPA_tiles.draw(janela)
        grupo_moedas.draw(janela)
        jogador.desenhar(janela)
        for fim in group_fim:
            fim.desenhar(janela)

        # Desenha informações de status
        fonte = pygame.font.SysFont(None, 36)
        texto_moedas = fonte.render(f"Moedas: {moedas_coletadas}", True, (255, 255, 255))
        janela.blit(texto_moedas, (10, 10))  # Desenha no canto superior esquerdo

        timer += loop_time
        texto_tempo = f"Tempo: {timer:.2f} segundos"
        imagem_texto = pygame.font.Font(None, 20).render(texto_tempo, True, (255, 255, 255))
        text_rect_TEMP = imagem_texto.get_rect(center=(LARGURA // 2, ALTURA - 45))
        janela.blit(imagem_texto, text_rect_TEMP)

        pygame.display.flip()
        clock.tick(FPS)


# Executa o jogo
if __name__ == '__main__':
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    assets = carrega_assets()
    lista_mapas = [MAPA1, MAPA2, MAPA3]  # Adicione todos os seus mapas aqui
    game_loop(janela, assets, lista_mapas)
   
