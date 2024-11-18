
import constantes 
import pygame
from pygame.locals import QUIT, KEYDOWN

def tela_final(janela, timer):
    # Define o fundo preto
    janela.fill((0, 0, 0))

    # Configura fontes e mensagens
    fonte_grande = pygame.font.SysFont(None, 72)
    fonte_pequena = pygame.font.SysFont(None, 36)

    mensagem_parabens = fonte_grande.render("Parabéns!", True, (255, 255, 255))
    mensagem_tempo = fonte_pequena.render(f"Você terminou em {timer:.2f} segundos!", True, (255, 255, 255))
    mensagem_sair = fonte_pequena.render("Pressione qualquer tecla para sair.", True, (255, 255, 255))

    # Centraliza as mensagens na tela
    rect_parabens = mensagem_parabens.get_rect(center=(constantes.LARGURA// 2, constantes.ALTURA// 3))
    rect_tempo = mensagem_tempo.get_rect(center=(constantes.LARGURA // 2, constantes.ALTURA // 2))
    rect_sair = mensagem_sair.get_rect(center=(constantes.LARGURA // 2, constantes.ALTURA // 1.5))

    # Desenha as mensagens na janela
    janela.blit(mensagem_parabens, rect_parabens)
    janela.blit(mensagem_tempo, rect_tempo)
    janela.blit(mensagem_sair, rect_sair)

    pygame.display.flip()
     # Espera que o jogador pressione uma tecla para sair
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                return  # Voltar para a tela inicial ou reiniciar

def tela_game_over(janela):
    # Carrega a imagem de "game over"
    imagem_game_over = pygame.image.load('assets/gameover.jfif').convert()
    imagem_game_over = pygame.transform.scale(imagem_game_over, (constantes.LARGURA, constantes.ALTURA))
    
    # Exibe a imagem na janela
    janela.blit(imagem_game_over, (0, 0))
    pygame.display.flip()
    
    # Espera que o jogador pressione uma tecla para sair
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                return  # Voltar para a tela inicial ou reiniciar
    
# Classe Tile (representa um caminho)
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, linha, coluna, tipo_quadrado, deslocamento_x=0, deslocamento_y=0):
        super().__init__()
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.x = coluna * constantes.TAMANHO_QUADRADO + deslocamento_x
        self.rect.y = linha * constantes.TAMANHO_QUADRADO + deslocamento_y
        self.tipo_quadrado = tipo_quadrado
        
class Espinho(pygame.sprite.Sprite):
    def __init__(self, x, y, asset,deslocamento_x=0, deslocamento_y=0):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Tamanho do espinho
        self.image.fill(constantes.VERMELHO)  # Cor vermelha para representar o espinho
        self.rect = self.image.get_rect()
        self.rect.x = x + deslocamento_x
        self.rect.y = y + deslocamento_y
        #

    def desenhar(self, janela):
        """Desenha o espinho na tela."""
        janela.blit(self.image, self.rect)


class Moeda(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_moeda, deslocamento_x=0, deslocamento_y=0):
        super().__init__()
        self.image = pygame.image.load(constantes.IMG_DIR / 'ponto_com_caminho.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()  # Cria o retângulo para a moeda
        self.rect.x = x + deslocamento_x
        self.rect.y = y + deslocamento_y

class Jogador:
    def __init__(self, x, y, velocidade, assets):
        self.posicao = pygame.Vector2(x, y)
        self.posicao_inicial = pygame.Vector2(x, y)
        self.velocidade = velocidade
        self.direcao = 'parado'
        self.tempo = 0
        self.imagem_atual = 0
        self.imagens = assets['anim foxy']
        self.bolinha = assets['bolinha']
        self.vida = 3
        self.i = 0
        

        # Carrega a imagem do jogador
        self.image = self.imagens[self.imagem_atual]

        # Define o rect com base na posição inicial
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicao.x, self.posicao.y)
        
    def resetar_posicao(self, x, y):
        self.posicao = pygame.Vector2(x, y)
        self.posicao_inicial = pygame.Vector2(x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicao.x, self.posicao.y)

    def verificar_colisao_espinho(self, grupo_espinhos):
        # Verifica colisão com os espinhos
        colisao_espinho = pygame.sprite.spritecollide(self, grupo_espinhos, False)
        if colisao_espinho:
            self.vida -= 1 
            self.posicao = self.posicao_inicial
            self.rect.topleft = (self.posicao.x, self.posicao.y)
        return colisao_espinho    

    def verificar_colisao_fim(self, group_fim, lista_mapas):  
        colisao_fim = pygame.sprite.spritecollide(self, group_fim, False)
        mapa = lista_mapas[self.i]
        if colisao_fim:
            self.i += 1
            mapa = lista_mapas[self.i]
        return mapa    


    def movimentar(self,mapa):
        self.tempo+=1
        if self.direcao == 'parado':
            if self.tempo >= 5:
                self.tempo = 0
                self.imagem_atual = (self.imagem_atual + 1) % 4
                self.image = self.imagens[self.imagem_atual]
        else:
            self.image = self.bolinha

        # Calcula a nova posição com base na direção
        nova_posicao = pygame.Vector2(self.posicao)
        # Movimenta o jogador com base na direção atual
        if self.direcao == "cima":
            nova_posicao.y -= self.velocidade
        elif self.direcao == "baixo":
            nova_posicao.y += self.velocidade
        elif self.direcao == "esquerda":
            nova_posicao.x-= self.velocidade
        elif self.direcao == "direita":
            nova_posicao.x += self.velocidade
        # Converte a nova posição para coordenadas da matriz
   

        self.posicao = nova_posicao
        self.rect.topleft = (self.posicao.x, self.posicao.y)
       
        colisao = pygame.sprite.spritecollide(self, mapa, False)
        if colisao:
            if self.direcao == "cima":
                nova_posicao.y += self.velocidade
            elif self.direcao == "baixo":
                nova_posicao.y -= self.velocidade
            elif self.direcao == "esquerda":
                nova_posicao.x += self.velocidade
            elif self.direcao == "direita":
                nova_posicao.x -= self.velocidade
            self.direcao = 'parado'


        #self.posicao = nova_posicao
        self.rect.topleft = (self.posicao.x, self.posicao.y)
        
                
    def desenhar(self, screen):
        # 'Desenha' o jogador 
        screen.blit(self.image, self.rect)
        
        
    def verificar_colisao(self, obstaculos):
        # Verifica colisão com os obstáculos
        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo.rect):
                return True  # Retorna verdadeiro se houver colisão
        return False    
    
    def verificar_colisao_moeda(self,moedas): 
        for moeda in moedas:
            if self.rect.colliderect(moeda.rect):
                moeda.kill()
                return True  # Retorna verdadeiro se a moeda foi coletada
        return False

class Fim(pygame.sprite.Sprite):
    def __init__(self, x, y, assets, deslocamento_x=0, deslocamento_y=0):
        super().__init__()
        self.imagem_atual = 0
        self.tempo = 0
        self.images = assets['fim anim']
        self.image = self.images[self.imagem_atual]
        self.rect = self.image.get_rect()
        self.rect.x = x * constantes.TAMANHO_QUADRADO + deslocamento_x
        self.rect.y = y * constantes.TAMANHO_QUADRADO + deslocamento_y

    def movimenta_fim(self):
        self.tempo += 1
        if self.tempo >= 30:
            self.tempo = 0
            self.imagem_atual = (self.imagem_atual + 1) % 2
            self.image = self.images[self.imagem_atual]

    def desenhar(self, screen):
        # 'Desenha' o jogador 
        screen.blit(self.image, self.rect)