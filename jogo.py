# Importando as bibliotecas necessárias.
import pygame
from pygame.locals import QUIT, KEYDOWN  
from constantes import *
import tela_inicial
from mapa1 import MAPA1
from mapa1  import m, p, v, c, f
from mapa2 import MAPA2
from classes import *  

# Função para inicializar os assets do jogo
def carrega_assets():
    assets = {
        'muro': pygame.image.load(IMG_DIR / 'muro.png').convert_alpha(),
        'ponto': pygame.image.load(IMG_DIR / 'ponto_com_caminho.png').convert_alpha(),
        'vacuo': pygame.image.load(IMG_DIR / 'vacuo.png').convert_alpha(),
        'caminho': pygame.image.load(IMG_DIR / 'caminho.png').convert_alpha(),
        'fim': pygame.image.load(IMG_DIR / 'fim1.png').convert_alpha(),
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
    return assets

# Loop principal do jogo
def game_loop(janela, assets):
    mapa_tiles = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()
    grupo_moedas = pygame.sprite.Group()  
    
    for linha in range(len(MAPA1)):
        for coluna in range(len(MAPA1[linha])):
            tipo_quadrado = MAPA1[linha][coluna]
            if tipo_quadrado in assets:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna, tipo_quadrado)
                mapa_tiles.add(quadrado)
                if tipo_quadrado == 'muro': 
                    grupo_obstaculos.add(quadrado)
                elif tipo_quadrado == 'ponto':  
                    moeda = Moeda(coluna *TAMANHO_QUADRADO, linha *TAMANHO_QUADRADO, assets['ponto'])
                    grupo_moedas.add(moeda)
    
    moedas_coletadas = 0

    jogador = Jogador(x_inicial, y_inicial, 10, assets['anim foxy'])
    #game_started = True 
    running = True
    
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                print(f"Tecla pressionada: {event.key}")  # Adicione esta linha para verificar o teclado
                if jogador.direcao == 'parado':
                    if event.key == pygame.K_UP:
                        jogador.direcao = "cima"
                    elif event.key == pygame.K_DOWN:
                        jogador.direcao = "baixo"
                    elif event.key == pygame.K_LEFT:
                        jogador.direcao = "esquerda"
                    elif event.key == pygame.K_RIGHT:
                        jogador.direcao = "direita"

        #desenha mapa e jogador
        
        #if game_started:
        
        jogador.movimentar(MAPA1)  ####obs###
        # Dentro do loop do jogo, logo após movimentar o jogador
        if jogador.verificar_colisao_moeda(grupo_moedas.sprites()):  # Passa os grupos
            moedas_coletadas += 1  # Incrementa o contador de moedas coletadas
            # for moeda in grupo_moedas:
            #     moeda.kill()  # Remove TODAS
       # print(moedas_coletadas)        
            

        jogador.movimentar(grupo_obstaculos)  ####obs###
        janela.fill(PRETO)
        mapa_tiles.draw(janela) 
        jogador.desenhar(janela)  
        grupo_moedas.draw(janela)  # Desenha as moedas
        
        fonte = pygame.font.SysFont(None, 36)
        texto_moedas = fonte.render(f"Moedas: {moedas_coletadas}", True, (255, 255, 255))
        janela.blit(texto_moedas, (10, 10))  # Desenha o texto no canto superior esquerdo

        pygame.display.flip()
        clock.tick(FPS)


# Executa o jogo
if __name__ == '__main__':
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    
    assets = carrega_assets()
    
    game_loop(janela, assets)

