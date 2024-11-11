
import constantes 
import pygame
from mapa1 import MAPA1
from mapa2 import MAPA2
from mapa1  import m, p, v, c, f
    
# Classe Tile (representa um caminho)
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, linha, coluna):
        super().__init__()
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.x = coluna * constantes.TAMANHO_QUADRADO
        self.rect.y = linha * constantes.TAMANHO_QUADRADO    #
        
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
        
class Jogador:
    def __init__(self, x, y, velocidade,imagem):
        self.posicao = pygame.Vector2(x, y)
        self.velocidade = velocidade
        self.direcao = None
        
        # Carrega a imagem do jogador
        self.image = pygame.image.load(constantes.IMG_DIR / 'foxy1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))  # Redimensiona 

        # Define o rect com base na posição do jogador e na imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicao.x, self.posicao.y)  # A posição inicial do jogador no jogo


    def movimentar(self,mapa):
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
        linha = int(nova_posicao.y // constantes.TAMANHO_QUADRADO)
        coluna = int(nova_posicao.x // constantes.TAMANHO_QUADRADO) 
        print(f"Verificando posição: ({linha}, {coluna})")
        print(f"Valor no mapa: {mapa[linha][coluna]}, p: {p}, c: {c}")

        
        #PRECISA TER ALGO QUE VÊ SE TA DENTRO DOS LIMITES DO MAPA
        if 0 <= linha < len(mapa) and 0 <= coluna < len(mapa[0]):
            if mapa[linha][coluna] == p  or  mapa[linha][coluna] == c :
            # Atualiza a posição do jogador se o próximo quadrado for "c"
                self.posicao = nova_posicao
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
            
    
    
