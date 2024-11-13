
import constantes 
import pygame
from mapa1 import MAPA1
from mapa2 import MAPA2
from mapa1  import m, p, v, c, f
    
# Classe Tile (representa um caminho)
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, linha, coluna, tipo_quadrado):
        super().__init__()
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.x = coluna * constantes.TAMANHO_QUADRADO
        self.rect.y = linha * constantes.TAMANHO_QUADRADO    #
        self.tipo_quadrado = tipo_quadrado
        
# Classe Obstáculo (obstáculo que "morre" ao colidir)
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Tamanho do obstáculo
        self.image.fill(constantes.VERMELHO)   # Cor do obstáculo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # def morrer(self):
    #     self.kill()  # Remove o obstáculo do grupo de sprites
class Moeda(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_moeda):
        super().__init__()
        self.image = pygame.image.load(constantes.IMG_DIR / 'ponto_com_caminho.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()  # Cria o retângulo para a moeda
        self.rect.x = x
        self.rect.y = y
        
class Jogador:
    def __init__(self, x, y, velocidade,assets):
        self.posicao = pygame.Vector2(x, y)
        self.velocidade = velocidade
        self.direcao = 'parado'
        self.tempo = 0
        self.imagem_atual = 0
        self.imagens = assets['anim foxy']
        self.bolinha = assets['bolinha']
        
        # Carrega a imagem do jogador
        self.image = self.imagens[self.imagem_atual]  # Redimensiona 

        # Define o rect com base na posição do jogador e na imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicao.x, self.posicao.y)  # A posição inicial do jogador no jogo


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
            print('colidiu')
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
        # pygame.draw.rect(screen, (255,255,255), self.rect)
        
        
    def verificar_colisao(self, obstaculos):
        # Verifica colisão com os obstáculos
        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo.rect):
                return True  # Retorna verdadeiro se houver colisão
        return False    
    
    def verificar_colisao_moeda(self,moedas): 
        for moeda in moedas:
            if self.rect.colliderect(moeda.rect):
                print(moeda.rect)
                moeda.kill()
                return True  # Retorna verdadeiro se a moeda foi coletada
        return False

        # def novo_jogo(self):
        #     self.all.sprites = pygame.sprite.Group()
        #     self.rodar()
        
        # #loop do jogo    
        # def rodar(self):
        #     self.jogando = True 
        #     while self.jogando:
        #         self.clock.ticket(constantes.FPS)
        #         self.eventos()
        #         self.refresh_sprites()
        #         self.desenhar_sprites()
            
    
