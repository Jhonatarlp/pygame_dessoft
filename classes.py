
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
        
<<<<<<< Updated upstream
class Jogador:
    def __init__(self, x, y, velocidade,imagem):
        self.posicao = pygame.Vector2(x, y)
=======
class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidade, image):
        super().__init__()
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
>>>>>>> Stashed changes
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
            self.rect.y -= self.velocidade
        elif self.direcao == "baixo":
            self.rect.y += self.velocidade
        elif self.direcao == "esquerda":
            self.rect.x -= self.velocidade
        elif self.direcao == "direita":
<<<<<<< Updated upstream
            self.posicao.x += self.velocidade
            
            # Atualizando o rect com a nova posição
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
            
    
    



        
=======
            self.rect.x += self.velocidade

    def desenhar(self, screen):
        # Desenha o jogador na tela
        screen.blit(self.image, self.rect)
>>>>>>> Stashed changes
